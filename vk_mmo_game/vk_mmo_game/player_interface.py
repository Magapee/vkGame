from const import PlayersFields
from const import LvlsFields
from str_const import DbNames


class PlayerInterface():

    @staticmethod
    def add_exp(exp, user_id, database):
        lvl = database.get(DbNames.lvl, user_id)[0][0]
        new_lvl = lvl
        new_exp = database.get(DbNames.exp, user_id)[0][0] + exp

        while new_exp >= database.select(DbNames.exp, DbNames.lvl, new_lvl, "lvls")[0][0]:
            new_exp -= database.select(DbNames.exp, DbNames.lvl, new_lvl, "lvls")[0][0]
            new_lvl += 1

        while new_lvl - lvl > 0:
            PlayerInterface._level_up(user_id, database)
            new_lvl -= 1
        
        database.set(DbNames.exp, new_exp, user_id)

    @staticmethod
    def _level_up(user_id, database):
        lvl = database.get(DbNames.lvl, user_id)[0][0]
        database.set(DbNames.lvl, lvl + 1, user_id)

