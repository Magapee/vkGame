import str_const
from const import db_fields
from litedb import LiteDB

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return( str_const.fracs0[info[0][db_fields.countryId]] + str_const.guild_name + "\n" +
    str_const.lvl_str + str(info[0][db_fields.lvl]) + "\n" +
    str_const.exp_str + str(info[0][db_fields.exp]) + "\n" +
    str_const.gold_str + str(info[0][db_fields.gold]))
