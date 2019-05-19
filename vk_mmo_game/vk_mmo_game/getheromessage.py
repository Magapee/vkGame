import const
from const import db_fields
from litedb import LiteDB

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return(const.fracs0[database.select("""countryid""", """id""", user_id)[0][db_fields.id]] + """[Имя гильдии]""" + """
    &#9889;Уровень:""" + str(info[0][db_fields.lvl]) + """
    &#128293;Опыт:""" + str(info[0][db_fields.exp]) + """
    &#128176;""" + str(info[0][db_fields.gold]))