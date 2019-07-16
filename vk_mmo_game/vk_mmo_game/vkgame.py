import random
import multiprocessing as mp
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

__version__="0.1.0a" #object update

class Game():
    def __init__(self):
        logger.logger() #I've fuck that shit
        logger.log("Initialization...")
        

        vk_session = vk_api.VkApi(token = vk_token.token)
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session, wait = const.wait)

        str_const.set_fracs_list()
        self.is_running = True
        with mp.Manager() as manager:
            self.database = LiteDB(const.db_name)
            self.players_list = manager.Array(
            self.player_manager, self.players_list = PlayerManager()

        logger.log("Initialization complete!")

    def process(self):
        while self.is_running:
            self.quest.check_quest(self.vk, self.database)
            #logger.log("Begin check")
            events = self.longpoll.check()
            #logger.log("End check")
            if len(events) != 0:
                for i in range(len(events)): #TODO: solve useless "if"
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