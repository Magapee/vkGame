import str_const
from str_const import strs
from const import players_fields
from litedb import LiteDB

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return( str_const.fracs0[info[0][players_fields.countryId]] + str_const.words.guild_name + "\n" +
    strs.lvl + str(info[0][players_fields.lvl]) + "\n" +
    strs.exp + str(info[0][players_fields.exp]) + "\n" +
    strs.gold + str(info[0][players_fields.gold]))
