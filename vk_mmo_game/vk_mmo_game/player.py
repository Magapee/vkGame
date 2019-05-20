import logger
import keyboard
import getheromessage
import const
import str_const
from str_const import db_names
from str_const import event_calls
from str_const import messages
from litedb import LiteDB

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime


class PlayerManager():
    def __init__(self):
        self.count = 0
        self.duel_links = { }
        self.players_on_quests = { }

    def quest(self, vk, event, database):#Квест
        logger.log("quest", event.user_id)
        self.players_on_quests[event.user_id] = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        vk.messages.send(user_id=event.user_id, message=messages.ok, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def check_quest(self, vk, database):
        #print(datetime.datetime.now().strftime("%H:%M:%S"))
        self.players_on_quests_b = self.players_on_quests.copy()
        for id in self.players_on_quests:
            if id != None:
                time = self.players_on_quests_b.get(id, None) - datetime.datetime.now()
                if time.days < 0:
                    self.players_on_quests_b.pop(id, None)
                    database.set(db_names.exp, db_names.exp + str_const.plus, id)
                    database.set(db_names.lvl, database.checklvl(database.select(db_names.exp, db_names.id, id)[0][0], id), id)
                    vk.messages.send(user_id=id, message="Квест окончен", random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, id))
        self.players_on_quests = self.players_on_quests_b.copy()


    def hero(self, vk, event, database):#Вызов профиля
        logger.log("hero", event.user_id)
        vk.messages.send(user_id=event.user_id, message=getheromessage.get_message(event.user_id, database), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def stop(self, vk, event):#Остановка бота, тестовый функционал
        if event.text == db_names.stop:
            if event.user_id in const.admins:
                vk.messages.send(user_id=event.user_id, message=messages.ok, random_id = random.randrange(1, 10000, 1))
                logger.log("Stop", event.user_id)
                return False
            else:
                vk.messages.send(user_id=event.user_id, message=messages.admin_func, random_id = random.randrange(1, 10000, 1))
                return True
        else:
            return True

    def reg(self, vk, event, database):#Регистрация пользователя
        cur = database.select(db_names.countryid, db_names.id, event.user_id)
        if cur == []:
            vk.messages.send(user_id=event.user_id, message=messages.select_frac, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(1, event.user_id))
            database.insert_new(event.user_id)
        elif cur == [(0,)]:
            if event.text in str_const.fracs1:
                database.set(db_names.countryid, str_const.fracs1[event.text], event.user_id)
                vk.messages.send(user_id=event.user_id, message=messages.you_faction + event.text, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
                logger.log("registration", event.user_id)
            else:
                vk.messages.send(user_id=event.user_id, message=messages.select_frac, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(1, event.user_id))

    def is_registered(self, user_id, database):#Проверка, зарегистрирован ли пользователь
        cur = database.select(db_names.countryid, db_names.id, user_id)
        if cur != []:
            if cur[0][0] != 0:
                return(True)
            else:
                return(False)
        return(False)

    def get_battle_link(self, vk, event, database): #генерация ссылки для дуэли
        logger.log("battle", event.user_id)
        link = "duel_" + str(self.count)
        self.count = self.count + 1
        self.duel_links[link] = event.user_id
        vk.messages.send(user_id=event.user_id, message=link, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
    
    def check_battle_link(self, vk, event, database): #дуэль по ссылке
        id = self.duel_links.pop(event.text, None)
        if id != None:
            if id != event.user_id:
                cube = random.randrange(0, 2, 1)
                cube1 = {-1:messages.win, 0:messages.lose, 1:messages.win}
                if cube == 1:
                    database.set(db_names.winscounter, db_names.winscounter + str_const.plus, event.user_id)
                if cube == 0:
                    database.set(db_names.winscounter, db_names.winscounter + str_const.plus, id)
                vk.messages.send(user_id=event.user_id, message=cube1[cube], random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
                vk.messages.send(user_id=id, message=cube1[cube - 1], random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, id))
            else:
                vk.messages.send(user_id=event.user_id, message=messages.fight_yourself, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def get_battle_stats(self, vk, event, database):
        vk.messages.send(user_id=event.user_id, message=messages.wins + str(database.select(db_names.winscounter, db_names.id, event.user_id)[0][0]), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def event_handling(self, vk, event, database):
        if self.is_registered(event.user_id, database):
            if event.text == event_calls.quest:
                self.quest(vk, event, database)
            elif event.text == event_calls.hero:
                self.hero(vk, event, database)
            elif event.text == event_calls.stat:
                self.get_battle_stats(vk, event, database)
            elif  event.text == event_calls.duel:
                self.get_battle_link(vk, event, database)
            else:
                self.check_battle_link(vk, event, database)
        else:
            self.reg(vk, event, database)