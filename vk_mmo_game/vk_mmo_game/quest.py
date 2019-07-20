import logger
import keyboard
#import mes_constructors
import const
from str_const import Messages
from litedb import DB

from vk import Messenger
import random
import datetime

class Quest():
    def __init__(self):
        self.players_on_quests = { }

    def quest(self, event, database):#Квест
        logger.log("quest", event.user_id)
        self.players_on_quests[event.user_id] = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        messenger = Messenger()
        messenger.send_mes(user_id = event.user_id, message = Messages.ok, keyboard = keyboard.ListButtons.list_buttons, one_time = False)\

    def check_quest(self, database):
        #print(datetime.datetime.now().strftime("%H:%M:%S"))
        players_on_quests_b = self.players_on_quests.copy()
        for id in self.players_on_quests:
            if id != None:
                time = players_on_quests_b.get(id, None) - datetime.datetime.now()
                if time.days < 0:
                    players_on_quests_b.pop(id, None)
                    PlayerInterface.add_exp(2, id, database)
                    messenger = Messenger()
                    messenger.send_mes(user_id = id, message = "Квест окончен", keyboard = keyboard.ListButtons.list_buttons, one_time = False)
        self.players_on_quests = players_on_quests_b.copy()