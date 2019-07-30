import queue
import datetime
import const
import vk
from vk_api.longpoll import VkEventType
from multiprocessing import RLock
import logger
from player import Player
from litedb import DB
from str_const import UsersColumns
from top import Top
from const import Begin


class PlayerManager:
    def __init__(self, eventsQueue):
        self.eventsQueue = eventsQueue

        self.db = DB(const.db_name)
        self.messenger = vk.Messenger()
        self._init_player_dict()

    def process_ans(self):
        a = datetime.datetime.now()
        events = []
        try:
            while True:
                events.append(self.eventsQueue.get(block=False))
        except queue.Empty:
            pass
        for el in events:
            self._proc_event(el)
            print((datetime.datetime.now() - a).microseconds)

    def _proc_event(self, event):
        with RLock() as lock:
            if event.user_id in self.players:
                self.players[event.user_id].process(event.text)
            else:
                self._register_player(id)

    def _register_player(self, id):
        self.players[id] = Player(self.db,
                                  self.messenger,
                                  (id, Begin.gold, Begin.exp, Begin.lvl, Begin.country, Begin.win,
                                   Begin.state, Begin.attack, Begin.health, Begin.quest_end))
        self.players[id].commit()

    def _init_player_dict(self):
        self.players = {}
        raw_players = self.db.get_players() #list 
        self.top = Top(raw_players, self.messenger)
        for player in raw_players:
            self.players[player[UsersColumns.id.value.number]] = Player(self.db,
                                                                  self.messenger,
                                                                  self.top,
                                                                  player)
        