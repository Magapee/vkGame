import const
from litedb import LiteDatabase

def get_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return(constants.fracs0[database.select("""countryid""", """id""", user_id)[0][0]] + """[Имя гильдии]""" + info[0][1] + """
    &#9889;Уровень:""" + str(info[0][4]) + """
    &#128293;Опыт:""" + str(info[0][3]) + """
    &#128176;""" + str(info[0][2]))