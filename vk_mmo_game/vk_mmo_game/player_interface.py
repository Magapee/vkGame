from const import players_fields
from const import lvls_fields
from str_const import db_names


class PlayerInterface():



    @staticmethod
    def add_exp(exp, user_id, database):
        lvl = database.get(db_names.lvl, user_id)[0][0]
        new_exp = database.get(db_names.exp, user_id)[0][0] + exp
        while new_exp >= database.select(db_names.exp, db_names.lvl, lvl, "lvls")[0][0]:
            new_exp -= database.select(db_names.exp, db_names.lvl, lvl, "lvls")[0][0]
            lvl += 1

        database.set(db_names.lvl, lvl, user_id)
        database.set(db_names.exp, new_exp, user_id)
