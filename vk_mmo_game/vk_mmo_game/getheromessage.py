import str_const
from litedb import LiteDB

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return(str_const.fracs0[database.select("""countryid""", """id""", user_id)[0][0]] + str_const.guild_name + info[0][1] + "\n" +
    str_const.lvl_str + str(info[0][4]) + "\n" +
    str_const.exp_str + str(info[0][3]) + "\n" +
    str_const.gold_str + str(info[0][2]))