import logger
import keyboard
import mes_constructors
import const
import str_const
from str_const import DbNames
from str_const import Buttons
from str_const import Messages
from str_const import NameCase
from litedb import LiteDB
from quest import Quest

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime


class PlayerManager():
    def __init__(self):
        self.count = 0
        self.duel_links = { }

    def hero(self, vk, event, database):#Вызов профиля
        logger.log("hero", event.user_id)
        vk.messages.send(user_id=event.user_id, message=mes_constructors.hero_message(event.user_id, database), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def stop(self, vk, event):#Остановка бота, тестовый функционал
        if event.text == DbNames.stop:
            if event.user_id in const.admins:
                vk.messages.send(user_id=event.user_id, message=Messages.ok, random_id = random.randrange(1, 10000, 1))
                logger.log("Stop", event.user_id)
                return False
            else:
                vk.messages.send(user_id=event.user_id, message=Messages.admin_func, random_id = random.randrange(1, 10000, 1))
                return True
        else:
            return True

    def registrate(self, vk, event, database):#Регистрация пользователя
        cur = database.select(DbNames.countryid, DbNames.id, event.user_id)
        if cur == []:
            vk.messages.send(user_id=event.user_id, message=Messages.select_frac, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(1, event.user_id))
            database.insert_new(event.user_id)
        elif cur == [(0,)]:
            if event.text in str_const.fracs1:
                database.set(DbNames.countryid, str_const.fracs1[event.text], event.user_id)
                vk.messages.send(user_id=event.user_id, message=Messages.you_faction + event.text, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
                logger.log("registration", event.user_id)
            else:
                vk.messages.send(user_id=event.user_id, message=Messages.select_frac, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(1, event.user_id))

    def is_registered(self, user_id, database):#Проверка, зарегистрирован ли пользователь
        cur = database.select(DbNames.countryid, DbNames.id, user_id)
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
                messages = {False : Messages.lose, True : Messages.win}

                if cube:
                    database.set(DbNames.winscounter, DbNames.winscounter + str_const.plus, event.user_id)
                else:
                    database.set(DbNames.winscounter, DbNames.winscounter + str_const.plus, id)

                vk.messages.send(user_id = event.user_id, message = mes_constructors.duel_message(cube, id, event.text, vk), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
                vk.messages.send(user_id = id, message = mes_constructors.duel_message(not cube, event.user_id, event.text, vk), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, id))
            else:
                vk.messages.send(user_id=event.user_id, message=Messages.fight_yourself, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def get_battle_stats(self, vk, event, database):
        vk.messages.send(user_id = event.user_id, message=Messages.wins + str(database.select(DbNames.winscounter, DbNames.id, event.user_id)[0][0]), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def event_handling(self, vk, event, database, quest):
        if self.is_registered(event.user_id, database):
            if event.text == Buttons.quest: #switch?
                quest.quest(vk, event, database)
            elif event.text == Buttons.stats:
                self.hero(vk, event, database)
            elif event.text == Buttons.top:
                self.get_battle_stats(vk, event, database)
            elif  event.text == Buttons.duel:
                self.get_battle_link(vk, event, database)
            else:
                self.check_battle_link(vk, event, database)
        else:
            self.registrate(vk, event, database)