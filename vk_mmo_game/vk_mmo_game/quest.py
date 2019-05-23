import logger
import keyboard
import mes_constructors
import const
from const import States
import str_const
from str_const import DbNames
from str_const import EventCalls
from str_const import Messages
from litedb import LiteDB
from player_interface import PlayerInterface
import time

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime

class Quest():
    def __init__(self):
        self.quest_duration = 10

    def quest(self, vk, event, database):#Квест
        logger.log("quest", event.user_id)
        database.set(DbNames.quest_end,  time.time() + self.quest_duration, event.user_id)#вот тут к time.time() нужно прибавить количество секунд в квесте
        #print(datetime.datetime.now() + datetime.timedelta(seconds = 10))
        database.set(DbNames.state, States.quest, event.user_id)
        vk.messages.send(user_id=event.user_id, message=Messages.quest + str(self.quest_duration) + Messages.seconds, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def check_quest(self, vk, database):
        players_on_quests = database.select(DbNames.id + " , " + DbNames.quest_end, DbNames.state, States.quest)
        if players_on_quests != []:
            for users in players_on_quests:
                id = users[0]
                timenow = float(users[1])
                if time.time() > timenow:
                    database.set(DbNames.state, States.normal, id)
                    database.set(DbNames.quest_end,  "NULL", id)
                    cube = random.randrange(0, 4, 1)
                    vk.messages.send(user_id=id, message=Messages.quest_stop + str(cube), random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, id))
                    PlayerInterface.add_exp(cube, id, database)
                    logger.log("quest stop", id)