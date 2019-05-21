import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType #не используется на данный момент
from litedb import LiteDB
from player import PlayerManager
import keyboard
import logger
import const
import vk_token
import str_const
from quest import Quest

__version__="0.0.1a"

class Game():
    def __init__(self):
        logger.logger()
        logger.log("Initialization...")
        str_const.set_fracs_list()
        vk_session = vk_api.VkApi(token = vk_token.token)

        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session, wait = const.wait)
        self.is_running = True
        #self.counter = 0
        self.player = PlayerManager()
        self.database = LiteDB() 
        self.quest = Quest()
        logger.log("Initialization complete!")

    def process(self):
        while self.is_running:
            self.quest.check_quest(self.vk, self.database)
            events = self.longpoll.check()
            if len(events) != 0:
                for i in range(len(events)):
                    event = events[i]
                    if event:
                        self._proc_event(event)

           
    def _proc_event(self, event):
        if not event.from_me:
            if event.type == VkEventType.MESSAGE_NEW and event.text:
                random.seed()
                #---------------------------------------------------------------stop
                self.is_running = self.player.stop(self.vk, event)
                #---------------------------------------------------------------stop
                self.player.event_handling(self.vk, event, self.database, self.quest) 