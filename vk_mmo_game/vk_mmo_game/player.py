from const import Begin
from const import State
import str_const
import const
from str_const import UsersColumns, Buttons, Strs, Messages
import datetime

class Player(object): 
    def __init__(self, database, messenger, raw_player):
        #requred args
        self.database = database #database for players
        self.messenger = messenger

        self.id = raw_player[UsersColumns.id.value.number] # id of player
        self.gold = raw_player[UsersColumns.gold.value.number] # исправила туть
        self.exp = raw_player[UsersColumns.exp.value.number]
        self.lvl = raw_player[UsersColumns.lvl.value.number]
        self.countryid = raw_player[UsersColumns.countryid.value.number]
        self.winscounter = raw_player[UsersColumns.winscounter.value.number]
        self.state = raw_player[UsersColumns.state.value.number]
        self.attack = raw_player[UsersColumns.attack.value.number]
        self.health = raw_player[UsersColumns.health.value.number]
        self.quest_end = raw_player[UsersColumns.quest_end.value.number]
        
        #std values
        self.last_message = None
        #self.answers = {Buttons.stats : self.show_stats()}
               #Buttons.quest : self.go_to_quest(),
               #Buttons.top : self.show_top(),
               #Buttons.duel : self.generate_dlink()}
        self.time_finish_quest = None
        self.count_duels = 0
        self.in_duel = False

    #orm (NOT FINAL!!!!)

    def commit(self): #oRm method
        raw_user = [self.id,
                    self.gold,
                    self.exp,
                    self.lvl,
                    self.countryid,
                    self.winscounter,
                    self.state,
                    self.attack,
                    self.health,
                    self.quest_end]
        self.db.update_user(raw_user)

    def pull(self):
        raise NotImplementedError

    #player interfaces, used by process

    def _send(self, text):
        self.messenger.send_mes(self.id, text)

    def show_stats(self): 
        message = (str_const.frac_by_number[self.countryid] + " " + str_const.Words.guild_name + "\n" +
                    Strs.lvl + str(self.lvl) + "\n" +
                    Strs.exp + str(self.exp) + "\n" +
                    Strs.gold + str(0) + "\n" +
                    Strs.health + str(self.health) + "\n"
                    )
        self._send(message)

    def go_to_quest(self):
        self.time_finish_quest = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        self._send(Messages.ok)

    def show_top(self):
        raise NotImplementedError

    def generate_dlink(self):
        #link = "duel_" + str(self.id) + str(self.count_duels)
        #self.count_duels += 1
        #self._send(link)
        #self.in_duel = True
        raise NotImplementedError

    def customtxt(self):
        raise NotImplementedError

    #programm interfaces

    def process(self, message):
        self.last_message = message
        if message == Buttons.stats:
            self.show_stats()
        elif message == Buttons.quest and self.time_finish_quest is None and not self.in_duel:
            self.go_to_quest()
        elif message == Buttons.top:
            self.show_top()
        elif message == Buttons.duel and self.time_finish_quest is None and not self.in_duel:
            self.generate_dlink()
        else:
            self.customtxt()


    def add_exp(self, exp):
        self.exp += exp
        exp_next_lvl = str_const.level_exp[self.lvl - 1]
        while self.exp >= exp_next_lvl:
            self.exp -= exp_next_lvl
            self._level_up()
            exp_next_lvl = str_const.level_exp[self.lvl - 1]


    def check_quest(self):
        if self.time_finish_quest is not None and datetime.datetime.now() >= self.time_finish_quest:
            self._return_from_quest()

    #private metods

    def _level_up(self):
        self.lvl += 1
    
    def _return_from_quest(self):
        self.add_exp(const.quest_exp)
        self.time_finish_quest = None
        self._send(Messages.finish_quest)

    def _check_dlink(self):
        raise NotImplementedError