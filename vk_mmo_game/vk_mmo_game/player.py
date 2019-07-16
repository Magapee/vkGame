from const import Begin
from const import State
from str_const import Buttons


class Player(object):

    answers = {
                Buttons.stats : show_stats(),
                Buttons.quest : go_to_quest(),
                Buttons.top : show_top(),
                Buttons.duel : generate_dlink()}

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

        #std values
        self.last_message = None

    #orm (NOT FINAL!!!!)

    def push(self): #not sure, if needed
        raise NotImplementedError

    def pull(self): #not sure, if needed
        raise NotImplementedError

    def synchronize(self): #oRm method, to synchronize object with DB uses pull and push
        raise NotImplementedError

    #player interfaces, used by process

    def show_stats(self): 
        raise NotImplementedError

    def go_to_quest(self):
        raise NotImplementedError

    def show_top(self):
        raise NotImplementedError

    def generate_dlink(self):
        raise NotImplementedError

    def customtxt(self):
        raise NotImplementedError

    #programm interfaces

    def process(self, message):
        self.last_message = message
        Player.answers.get(message, customtxt())()

    def add_exp(self, exp):
        raise NotImplementedError

    def check_quest(self):
        raise NotImplementedError

    #private metods

    def _level_up(self):
        raise NotImplementedError
    
    def _return_from_quest(self):
        raise NotImplementedError

    def _check_dlink(self):
        raise NotImplementedError