import logger
import random
import keyboard
import getheromessage
import constants
from litedatabase import LiteDatabase

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


class Player():
    def __init__(self):
        self.flag = True

    def quest(self, vk, event, database):#Квест, надо допилить
        if event.text == "exp +1":
            database.update("""exp""", """exp + 1""", event.user_id)
            logger.log("+1 exp", event.user_id)
            database.update("""lvl""", database.checklvl(database.select("""exp""", """id""", event.user_id)[0][0], event.user_id), event.user_id)
            vk.messages.send(user_id=event.user_id, message='Ok', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKeyOne())

    def hero(self, vk, event, database):#Вызов профиля
        if event.text == 'hero':
            logger.log("hero", event.user_id)
            vk.messages.send(user_id=event.user_id, message=getheromessage.get_message(event.user_id, database), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKeyOne())

    def stop(self, vk, event):#Остановка бота, тестовый функционал
        if event.text == 'Stop':
            if event.user_id in constants.admins:
                vk.messages.send(user_id=event.user_id, message='Ok', random_id = random.randrange(1, 10000, 1))
                logger.log("Stop", event.user_id)
                return(False)
            else:
                vk.messages.send(user_id=event.user_id, message='Функционал для админов', random_id = random.randrange(1, 10000, 1))
                return(True)
        else:
            return(True)

    def reg(self, vk, event, database):#Регистрация пользователя
        cur = database.select("""countryid""", """id""", event.user_id)
        if cur == []:
            vk.messages.send(user_id=event.user_id, message='Выберите фракцию', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKeyTwo())
            user = vk.users.get(user_ids = event.user_id)[0]
            database.insert(event.user_id, str(user['last_name']) + ' ' + str(user['first_name']))
        elif cur == [(0,)]:
            if event.text in constants.fracs1:
                database.update("""countryid""", constants.fracs1[event.text], event.user_id)
                vk.messages.send(user_id=event.user_id, message='Вами выбрана фракция: ' + event.text, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKeyOne())
            else:
                vk.messages.send(user_id=event.user_id, message='Выберите фракцию', random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKeyTwo())
            logger.log("registration", event.user_id)

    def is_registered(self, user_id, database):#Проверка, зарегистрирован ли пользователь
        cur = database.select("""countryid""", """id""", user_id)
        if cur[0][0] != 0:
            return(True)
        else:
            return(False)