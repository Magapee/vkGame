import logger
import keyboard
import mes_constructors
import const
import str_const
from str_const import DbNames
from str_const import EventCalls
from str_const import Messages
from litedb import LiteDB
from player_interface import PlayerInterface

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime

class Quest():
    def __init__(self):
        self.players_on_quests = { }

    def quest(self, vk, event, database):#Квест
        logger.log("quest", event.user_id)
        self.players_on_quests[event.user_id] = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        vk.messages.send(user_id=event.user_id, message=Messages.ok, random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, event.user_id))

    def check_quest(self, vk, database):
        #print(datetime.datetime.now().strftime("%H:%M:%S"))
        players_on_quests_b = self.players_on_quests.copy()
        for id in self.players_on_quests:
            if id != None:
                time = players_on_quests_b.get(id, None) - datetime.datetime.now()
                if time.days < 0:
                    players_on_quests_b.pop(id, None)
                    PlayerInterface.add_exp(2, id, database)
                    vk.messages.send(user_id=id, message="Квест окончен", random_id = random.randrange(1, 10000, 1), keyboard = keyboard.getKey(2, id))
        self.players_on_quests = players_on_quests_b.copy()