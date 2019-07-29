import random
import multiprocessing as mp
import vk
from litedb import DB
from player_manager import PlayerManager
import logger
import const
import str_const

__version__="0.1.0a" #object update



class Game():
    
    def listner_proc(self, manager):
        while True:
            manager.procces_ans()

    #def process(self):
    #    while self.is_running:
    #        self.quest.check_quest(self.vk, self.database)
    #        #logger.log("Begin check")
    #        events = self.longpoll.check()
    #        #logger.log("End check")
    #        if len(events) != 0:
    #            for i in range(len(events)): #TODO: solve useless "if"
    #                event = events[i]
    #                if event:
    #                    self._proc_event(event

    def __init__(self):
        logger.logger() #I fuck that shit
        logger.log("Initialization...")
        
        str_const.set_fracs_list()
        eventsQueue = mp.Queue()
        self.player_manager = PlayerManager(eventsQueue)

        logger.log("Initialization complete!")
        self.ans_thread.join()