import random
import multiprocessing as mp
from multiprocessing import managers as mn
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType #не используется на данный момент
from litedb import DB
from player_manager import PlayerManager
import keyboard
import logger
import const
import vk_token
import str_const
from quest import Quest

__version__="0.1.0a" #object update


class Manager(mn.BaseManager):
    pass

Manager.register('PlayersManager', PlayerManager)




class Game():
    def __init__(self):
        logger.logger() #I fuck that shit
        logger.log("Initialization...")
        

        vk_session = vk_api.VkApi(token = vk_token.token)
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session, wait = const.wait)
        str_const.set_fracs_list()
        self.database = DB(const.db_name)

        with Manager() as manager:
            self.player_manager = manager.PlayerManager()
            self.is_running = manager.Value('i', 1)

        logger.log("Initialization complete!")



    def ans_thread(self, manager):
        raise NotImplementedError

    def not_ans_thread(self, manager):
        raise NotImplementedError


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