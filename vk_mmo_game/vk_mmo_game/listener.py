from vk import Messenger

class Listener(object):
    def __init__(self, queue, game_is_running):
        self.messenger  = Messenger()
        self.queue = queue
        self.game_is_running = game_is_running

    def process(self):
        while self.game_is_running:
            self._check()

    def _check(self):
        events = self.messenger.check()
        for event in events:
            self.queue.put(event)


