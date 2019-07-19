import const
import vk
from vk_api.longpoll import VkEventType
from multiprocessing import RLock
from player import Player
from litedb import DB
from str_const import UsersColumnsNames, UsersColumns


class PlayerManager(object):
    def __init__(self):
        self.db = DB(const.db_name)
        #self.messenger = vk.Messenger()
        self._init_player_dict(self)

    def procces_ans(self):
        events = self.messenger.check()
        for el in events:
            self._proc_event(el)

    def _proc_event(self, event):
        with RLock() as lock:
            if not event.from_me:
                if event.type == VkEventType.MESSAGE_NEW and event.text:
                    if event.user_id in self.players:
                        self.players[event.user_id].process(event.text)
                    else:
                        self._register_player(id)

    def _register_player(self, id):
        raise NotImplementedError

    def _init_player_dict(self, a):
        self.players = {}
        raw_players = self.db.get_players() #list
        for player in raw_players:
            self.players[UsersColumns.id.number] = Player(self.db,
                                                          self.messenger,
                                                          player)
