import str_const
from str_const import Strs, NameCase, Messages, Words, DbNames
import const
from const import PlayersFields, States
from litedb import LiteDB
import time
import logger

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
    users = vk_api.users.get(user_ids = user_id, name_case = name_case)
    links = []
    for i in users:
        links.append("[id" + str(i['id']) + "|" + i["first_name"] + " " + i["last_name"] + "]")
    return (links)
           
def duel_top(database, vk_api):
    top = database.select_order(DbNames.id + " , " + DbNames.winscounter, DbNames.winscounter)
    ids = str(top[0][0]) 
    for i in range(1, const.top_range):
        ids = ids + "," +  str(top[i][0])
    links = link_name(ids, vk_api)
    top_mes = ""
    for i in range(0, const.top_range):
        if i < 3:
            top_mes = top_mes + str_const.Emoji.Medals[i + 1] + "#" + str(i + 1) + " " + str(links[i]) + ": " + str(top[i][1]) + "\n"
        else:
            top_mes = top_mes + "#" + str(i + 1) + " " + str(links[i]) + ": " + str(top[i][1]) + "\n"
    return(top_mes)

def duel_message(is_win, opp_id, duel_link, vk_api):
    if is_win:
        win_str = Messages.win
    else:
        win_str = Messages.lose
    return win_str + ' ' + Messages.in_duel_with + ' ' + link_name(opp_id, vk_api, NameCase.ins)[0] + ' ' + Messages.with_link + ' ' + duel_link