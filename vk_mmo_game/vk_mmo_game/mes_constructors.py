import str_const
from str_const import Strs, NameCase, Messages, Words, DbNames
from const import PlayersFields, States
from litedb import LiteDB
import time

def hero_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    if info[0][PlayersFields.state] != int(States.normal):
        status = str(str_const.states[info[0][PlayersFields.state]] + str(int(info[0][PlayersFields.quest_end] - time.time())) + Words.seconds)
    else:
        status = str(str_const.states[info[0][PlayersFields.state]])
    return (str_const.fracs0[info[0][PlayersFields.countryId]] + " " + str_const.Words.guild_name + "\n" +
        Strs.lvl + str(info[0][PlayersFields.lvl]) + "\n" +
        Strs.exp + str(info[0][PlayersFields.exp]) + "\n" +
        Strs.gold + str(info[0][PlayersFields.gold]) + "\n" +
        Strs.health + str(info[0][PlayersFields.health]) + "\n" +
        Strs.attack + str(info[0][PlayersFields.attack])+ "\n" +
        Strs.status + status)


def link_name(user_id, vk_api, name_case = NameCase.nom):
    user = vk_api.users.get(user_ids = [user_id], name_case = name_case)[0]
    return ("[id"
           + str(user_id)
           + "|" 
           + user["first_name"] 
           + " " 
           + user["last_name"] 
           + "]"
           )
           
def duel_top(database, vk_api):
    top = database.select_order(DbNames.id + " , " + DbNames.winscounter, DbNames.winscounter)
    top_mes = ""
    for i in range(0, 10):
        top_mes = top_mes + "#" + str(i + 1) + " " + str(link_name(top[i][0], vk_api)) + " :" + str(top[i][1]) + "\n"
    return(top_mes)

def duel_message(is_win, opp_id, duel_link, vk_api):
    if is_win:
        win_str = Messages.win
    else:
        win_str = Messages.lose
    return win_str + ' ' + Messages.in_duel_with + ' ' + link_name(opp_id, vk_api, NameCase.ins) + ' ' + Messages.with_link + ' ' + duel_link