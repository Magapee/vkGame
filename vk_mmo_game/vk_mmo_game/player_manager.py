from multiprocessing import RLock

class PlayerManager(object):
    def __init__(self, db, messenger):
        self.db = db
        self.messenger

    def proc_event(self, text, id):
        with RLock() as lock:
            if id in self.players:
                self.players[id].process(text)
            else:
                _create_user(id)

    def get_users(self):
        with RLock() as lock:
            return self.players

    def _create_user(self, id):
        raise NotImplementedError

    def _init_player_dict(self):
        raise NotImplementedError