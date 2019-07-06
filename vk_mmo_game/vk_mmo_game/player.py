from const import Begin
from const import State
from str_const import Buttons


class Player(object):
    def __init__(self, id, lock, database, #required params
                 lvl = int(Begin.lvl), exp = int(Begin.exp),
                 gold = int(Begin.gold), health = int(Begin.health),
                 attack = int(Begin.attack), winscounter = int(Begin.win),
                 state = State.unregistered, countryid = int(Begin.country)):

        #requred args
        self.id = id #id of player, for vk = vk id
        self.lock = lock #multiprossesing.Lock
        self.database = database #database for players

        #unrequred args
        self.lvl = lvl
        self.exp = exp
        self.gold = gold
        self.health = health
        self.attack = attack
        self.state = state
        self.countryid = countryid

    #orm

    def push(self): #not sure, if needed
        raise NotImplementedError

    def pull(self): #not sure, if needed
        raise NotImplementedError

    def synchronize(self): #oRm method, to synchronize object with DB uses pull and push
        raise NotImplementedError

    #player interfaces, used by prosess

    def show_stats(self): 
        raise NotImplementedError

    def go_to_quest(self):
        raise NotImplementedError

    def show_top(self):
        raise NotImplementedError

    def generate_dlink(self):
        raise NotImplementedError

    def std_ans(self):
        raise NotImplementedError

    #programm interfaces

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
            std_ans()

    def add_exp(self, exp):
        raise NotImplementedError

    #private metods

    def _level_up(self):
        raise NotImplementedError