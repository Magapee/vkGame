from const import Begin
from const import State
import str_const
from str_const import UsersColumns
from str_const import Buttons
from str_const import UsersColumnsNames
from str_const import Strs

class Player(object):

    

    def __init__(self, database, messenger, raw_player):

        #requred args
        self.id = raw_player[UsersColumns[UsersColumnsNames.id][1]] #id of player, for vk = vk id
        self.database = database #database for players
        self.messenger = messenger

        self.exp = UsersColumns[UsersColumnsNames.exp][1]
        self.lvl = UsersColumns[UsersColumnsNames.lvl][1]
        self.countryid = UsersColumns[UsersColumnsNames.countryid][1]
        self.winscounter = UsersColumns[UsersColumnsNames.winscounter][1]
        self.state = UsersColumns[UsersColumnsNames.state][1]
        self.health = UsersColumns[UsersColumnsNames.health][1]
        self.quest_end = UsersColumns[UsersColumnsNames.quest_end][1]
        
        #std values
        self.last_message = None
        #self.answers = {Buttons.stats : self.show_stats()}
               #Buttons.quest : self.go_to_quest(),
               #Buttons.top : self.show_top(),
               #Buttons.duel : self.generate_dlink()}

    #orm (NOT FINAL!!!!)

    def commit(self): #oRm method
        raw_user = [self.id,
                   self.exp,
                   self.lvl,
                   self.countryid,
                   self.winscounter,
                   self.state,
                   self.health,
                   self.quest_end]
        self.db.update_user(raw_user)

    def pull(self):
        raise NotImplementedError

    #player interfaces, used by process

    def _send(self, text):
        self.messenger.send_mes(self.id, text)

    def show_stats(self): 
        message = (str_const.fracs0[self.countryid] + " " + str_const.Words.guild_name + "\n" +
                    Strs.lvl + str(self.lvl) + "\n" +
                    Strs.exp + str(self.exp) + "\n" +
                    Strs.gold + str(0) + "\n" +
                    Strs.health + str(self.health) + "\n"
                    )
        self._send(message)

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
        if message == Buttons.stats:
            self.show_stats


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