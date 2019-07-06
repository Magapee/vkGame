from const import Begin
from const import State
from str_const import Buttons


class Player(object):
    def __init__(self, id, lock, database, #required params
                 lvl = int(Begin.lvl), exp = int(Begin.exp),
                 gold = int(Begin.gold), health = int(Begin.health),
                 attack = int(Begin.attack), winscounter = int(Begin.win),
                 state = State.unregistered, countryid = int(Begin.country)):
        self.lvl = lvl
        self.exp = exp
        self.gold = gold
        self.health = health
        self.attack = attack
        self.state = state
        self.countryid = countryid

        self.id = id #id of player, for vk = vk id
        self.lock = lock #multiprossesing.Lock
        self.database = database #database for players

    def prosess(self, message):
        if message == Buttons.stats:
            show_stats()
        elif message == Buttons.quest:
            go_to_quest()
        elif message == Buttons.top:
            show_top()
        elif message == Buttons.duel:
            generate_dlink(self)
        else:
            pass

    
    def push(self): #not sure, if needed
        raise NotImplemented

    def get(self):
        raise NotImplemented

    def synchronize(self): #oRm method, to synchronize object with DB
        raise NotImplemented

    def show_stats(self):
        raise NotImplemented

    def go_to_quest(self):
        raise NotImplemented

    def show_top(self):
        raise NotImplemented

    def add_exp(self, exp):
        raise NotImplemented

    def _level_up(self):
        raise NotImplemented

    def generate_dlink(self):
        raise NotImplemented

    def std_ans(self):
        raise NotImplemented
