import random
import multiprocessing as mp
from multiprocessing import managers as mn
import vk
from litedb import DB
from player_manager import PlayerManager
import logger
import const
import str_const

__version__="0.1.0a" #object update


class Manager(mn.BaseManager):
    pass

Manager.register('PlayerManager', PlayerManager)




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

    def _proc_event(self, event):
        if not event.from_me:
            if event.type == VkEventType.MESSAGE_NEW and event.text:
                random.seed()
                #---------------------------------------------------------------stop
                self.is_running = self.player.stop(self.vk, event)
                #---------------------------------------------------------------stop
                self.player.event_handling(self.vk, event, self.database, self.quest) 

    def __init__(self):
        logger.logger() #I fuck that shit
        logger.log("Initialization...")
        
        str_const.set_fracs_list()
        
        messenger = vk.Messenger()
        #for i in const.admins:
            #messenger.send_mes(i, "Game is running!")

        with Manager() as manager:
            self.player_manager = manager.PlayerManager()
            self.listner_thread = mp.Process(target = self.ans_proc,
                                        args = (self.player_manager,))
            self.ans_thread.start()
            logger.log("Initialization complete!")
            self.ans_thread.join()