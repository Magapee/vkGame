from const import PlayersFields
from const import LvlsFields
from str_const import UsersColumns


class PlayerInterface():

    @staticmethod
    def add_exp(exp, user_id, database):
        lvl = database.get(UsersColumns.lvl, user_id)[0][0]
        new_lvl = lvl
        new_exp = database.get(UsersColumns.exp, user_id)[0][0] + exp

        while new_exp >= database.select(UsersColumns.exp, UsersColumns.lvl, new_lvl, "lvls")[0][0]:
            new_exp -= database.select(UsersColumns.exp, UsersColumns.lvl, new_lvl, "lvls")[0][0]
            new_lvl += 1

        while new_lvl - lvl > 0:
            PlayerInterface._level_up(user_id, database)
            new_lvl -= 1
        
        database.set(UsersColumns.exp, new_exp, user_id)

    @staticmethod
    def _level_up(user_id, database):
        lvl = database.get(UsersColumns.lvl, user_id)[0][0]
        database.set(UsersColumns.lvl, lvl + 1, user_id)

