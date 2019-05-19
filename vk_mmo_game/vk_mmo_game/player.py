import logger
import random
import keyboard
import getheromessage
import const
import str_const
from litedb import LiteDB

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


class PlayerManager():
    def __init__(self):
        self.count = 0

    def quest(self, vk, event, database):#Квест, надо допилить
        database.update("""exp""", """exp + 1""", event.user_id)
        logger.log("+1 exp", event.user_id)
        database.update("""lvl""", database.checklvl(database.select("""exp""", """id""", event.user_id)[0][0], event.user_id), event.user_id)
        vk.messages.send(user_id=event.user_id, message='Ok', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def hero(self, vk, event, database):#Вызов профиля
        logger.log("hero", event.user_id)
        vk.messages.send(user_id=event.user_id, message=getheromessage.get_message(event.user_id, database), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def stop(self, vk, event):#Остановка бота, тестовый функционал
        if event.text == 'Stop':
            if event.user_id in const.admins:
                vk.messages.send(user_id=event.user_id, message='Ok', random_id = random.randrange(1, 10000, 1))
                logger.log("Stop", event.user_id)
                return False
            else:
                vk.messages.send(user_id=event.user_id, message='Функционал для админов', random_id = random.randrange(1, 10000, 1))
                return True
        else:
            return True

    def reg(self, vk, event, database):#Регистрация пользователя
        cur = database.select("""countryid""", """id""", event.user_id)
        if cur == []:
            vk.messages.send(user_id=event.user_id, message='Выберите фракцию', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(1, event.user_id))
            user = vk.users.get(user_ids = event.user_id)[0]
            database.insert(event.user_id, str(user['last_name']) + ' ' + str(user['first_name']))
        elif cur == [(0,)]:
            if event.text in str_const.fracs1:
                database.update("""countryid""", str_const.fracs1[event.text], event.user_id)
                vk.messages.send(user_id=event.user_id, message='Вами выбрана фракция: ' + event.text, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
            else:
                vk.messages.send(user_id=event.user_id, message='Выберите фракцию', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
            logger.log("registration", event.user_id)

    def is_registered(self, user_id, database):#Проверка, зарегистрирован ли пользователь
        cur = database.select("""countryid""", """id""", user_id)
        if cur[0][0] != 0:
            return(True)
        else:
            return(False)

    def get_battle_link(self, vk, event, database): #генерация ссылки для дуэли
        logger.log("battle", event.user_id)
        link = """duel_""" + str(self.count)
        self.count = self.count + 1
        database.update("""battlelink""", """'""" + link + """'""", event.user_id)
        vk.messages.send(user_id=event.user_id, message=link, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
    
    def check_battle_link(self, vk, event, database): #дуэль по ссылке
        cur = database.select("""*""", """battlelink""", """'""" + event.text + """'""")
        if cur != []:
            if cur[0][0] != event.user_id:
                database.update("""battlelink""", """NULL""", cur[0][0])
                database.update("""battlelink""", """NULL""", event.user_id)
                cube = random.randrange(0, 2, 1)
                cube1 = {-1:"Победа", 0:"Поражение", 1:"Победа"}
                if cube == 1:
                    database.update("""winscounter""", """winscounter + 1""", event.user_id)
                if cube == 0:
                    database.update("""winscounter""", """winscounter + 1""", cur[0][0])
                vk.messages.send(user_id=event.user_id, message=cube1[cube], random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
                vk.messages.send(user_id=cur[0][0], message=cube1[cube - 1], random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
            else:
                vk.messages.send(user_id=event.user_id, message="Нельзя драться с собой", random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def get_battle_stats(self, vk, event, database):
        database.select("""winscounter""", """id""", event.user_id)
        vk.messages.send(user_id=event.user_id, message="Побед:" + str(database.select("""winscounter""", """id""", event.user_id)[0][0]), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))
        return True

    def event_handling(self, vk, event, database):
        if self.is_registered(event.user_id, database): #Проверка для инвентов maga: точно не так, мы n раз сравниваем строку
            if event.text == "exp +1":
                self.quest(vk, event, database)
            elif event.text == "hero":
                self.hero(vk, event, database)
            elif event.text == "Статистика":
                self.get_battle_stats(vk, event, database)
            #elif  event.text == "Дуэль":
            #    self.get_battle_link(vk, event, database)
            else:
                self.hero(vk, event, database)
        else:
            self.reg(vk, event, database)