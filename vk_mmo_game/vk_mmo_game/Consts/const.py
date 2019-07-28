admins = 385124486, 308831692, 129640173
db_name = "Game.db"
random = 10 ** 100000
name_table_users = "users"
quest_exp = 1
top_range = 10


class State():
    unregistered = '0'
    normal = '1'
    forest = '2'


class LvlsFields():
    lvl = 0
    exp = 1

wait = 3


class Begin():
    country = '0'
    gold = '0'
    exp = '0'
    lvl = '1'
    win = '0'
    attack = '1'
    health = '10'
    state = State.normal
    quest_end = 'NULL'