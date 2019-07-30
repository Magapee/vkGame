import random
import multiprocessing as mp
import vk
from litedb import DB
from player_manager import PlayerManager
import logger
import const
import str_const
from listener import Listener

__version__="0.1.0a" #object update


def listener_procf(queue, game_is_running):
    listener = Listener(queue, game_is_running)
    listener.process()

class Game():
    

    def __init__(self):
        logger.logger() #I fuck that shit
        logger.log("Initialization...")
        str_const.set_fracs_list()
        self.game_is_running = True
        eventsQueue = mp.Queue()
        self.player_manager = PlayerManager(eventsQueue)
        listener_proc = mp.Process(target=listener_procf, args=(eventsQueue, self.game_is_running))
        listener_proc.start()
        logger.log("Initialization complete!")
        while self.game_is_running:
            self.player_manager.process_ans()