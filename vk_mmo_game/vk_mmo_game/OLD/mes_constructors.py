import str_const
from str_const import Strs, NameCase, Messages
from const import PlayersFields
from litedb import DB

def hero_message(user_id, database):
    info = database.select("""*""", """id""", user_id)
    return (str_const.frac_by_number[info[0][PlayersFields.countryId]] + " " + str_const.Words.guild_name + "\n" +
    Strs.lvl + str(info[0][PlayersFields.lvl]) + "\n" +
    Strs.exp + str(info[0][PlayersFields.exp]) + "\n" +
    Strs.gold + str(info[0][PlayersFields.gold]) + "\n" +
    Strs.health + str(info[0][PlayersFields.health]) + "\n" +
    Strs.attack + str(info[0][PlayersFields.attack])
    )


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


def duel_message(is_win, opp_id, duel_link, vk_api):
    if is_win:
        win_str = Messages.win
    else:
        win_str = Messages.lose
    return win_str + ' ' + Messages.in_duel_with + ' ' + link_name(opp_id, vk_api, NameCase.ins) + ' ' + Messages.with_link + ' ' + duel_link