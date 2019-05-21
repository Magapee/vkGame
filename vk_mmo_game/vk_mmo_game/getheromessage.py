import str_const
from str_const import Strs
from const import PlayersFields
from litedb import LiteDB

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return (str_const.fracs0[info[0][PlayersFields.countryId]] + " " + str_const.Words.guild_name + "\n" +
    Strs.lvl + str(info[0][PlayersFields.lvl]) + "\n" +
    Strs.exp + str(info[0][PlayersFields.exp]) + "\n" +
    Strs.gold + str(info[0][PlayersFields.gold]) + "\n" +
    Strs.health + str(info[0][PlayersFields.health]) + "\n" +
    Strs.attack + str(info[0][PlayersFields.attack])
    )
