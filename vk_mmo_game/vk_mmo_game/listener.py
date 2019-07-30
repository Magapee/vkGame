from multiprocessing import RLock
import logger
from vk import Messenger


class Listener(object):
    def __init__(self, queue, game_is_running):
        self._messenger  = Messenger()
        self._queue = queue
        self._game_is_running = game_is_running

    def process(self):
        while self._game_is_running:
            self._check()

    def _check(self):
        events = self._messenger.check()
        for event in events:
            self._queue.put(event)