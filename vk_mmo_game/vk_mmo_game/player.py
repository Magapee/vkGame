from const import Begin
from const import State
import str_const
import const
from str_const import UsersColumns, Buttons, Strs, Messages
import datetime
import vk

class Player(object): 
    def __init__(self, database, messenger, top, raw_player):
        #requred args
        self.database = database #database for players
        self.messenger = messenger
        self.top = top

        self.id = raw_player[UsersColumns.id.value.number] # id of player
        #self.gold = raw_player[UsersColumns.gold.value.number]
        self.exp = raw_player[UsersColumns.exp.value.number]
        self.lvl = raw_player[UsersColumns.lvl.value.number]
        self.countryid = raw_player[UsersColumns.countryid.value.number]
        self.winscounter = raw_player[UsersColumns.winscounter.value.number]
        self.state = raw_player[UsersColumns.state.value.number]
        #self.attack = raw_player[UsersColumns.attack.value.number]
        #self.health = raw_player[UsersColumns.health.value.number]
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

    #orm

    def commit(self): #oRm method
        raw_user = [self.id,
                    #self.gold,
                    self.exp,
                    self.lvl,
                    self.countryid,
                    self.winscounter,
                    self.state,
                    #self.attack,
                    #self.health,
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
                    Strs.exp + str(self.exp) + "\n"
                    )
        self._send(message)

    def go_to_quest(self):
        self.time_finish_quest = datetime.datetime.now() + datetime.timedelta(seconds = 10)
        self._send(Messages.ok)

    def show_top(self):
        top = self.top.raw_top
        message = ''
        for i in range(1, len(top) + 1):
            message += f'{i} {top[i - 1][0]} {top[i - 1][1]}\n'
        self._send(message)


    def generate_dlink(self):
        #link = "duel_" + str(self.id) + str(self.count_duels)
        #self.count_duels += 1
        #self._send(link)
        #self.in_duel = True
        raise NotImplementedError

    def customtxt(self, message):
        #if (message == Buttons.duel or message == Buttons.quest) and self.in_duel:
        #    self._send(Messages.in_duel)
        #elif (message == Buttons.duel or message == Buttons.quest) and self.time_finish_quest is not None:
        #    self._send(Messages.in_quest)
        #else:
        #    self._send(Messages.wrong_text)
        raise NotImplementedError
    
    #programm interfaces

    def process(self, message):
        self.last_message = message
        if self.last_message == Buttons.stats:
            self.show_stats()
        elif self.last_message == Buttons.quest and self.time_finish_quest is None and not self.in_duel:
            self.go_to_quest()
        elif self.last_message == Buttons.top:
            self.show_top()
        elif self.last_message == Buttons.duel and self.time_finish_quest is None and not self.in_duel:
            self.generate_dlink()
        else:
            self.customtxt(self.last_message)


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
        #self._change_top()
        raise NotImplementedError
        
    def _change_top(self):
        ind = 0
        while (top_range - 1 - ind >= 0 
               and self.winscounter > self.top.raw_top[top_range - 1 - ind][1]):
            ind += 1
        if top_range - 1 - ind < 0:
            self.top.raw_top.insert(0, (self.id, self.winscounter))
        elif ind != 0:
            self.top.raw_top.insert(top_range - ind, (self.id, self.winscounter))
        if len(self.top.raw_top) > top_range:
            del self.top.raw_top[-1]
        