
lvl = "Уровень"
lightning_emoji = "&#9889;"
lvl_str = lightning_emoji + lvl + ":"

exp = "Опыт"
fire_emoji = "&#128293;"
exp_str = fire_emoji + exp + ":"

gold = "Золото"
gold_emoji = "&#128176;"
gold_str = gold_emoji + gold + ":"

guild_name = "[Имя гильдии]"

fracs_quantity = 3
fracs0 = {1:"Сумрачный замок", 2:"Мятный замок", 3:"Пидорский замок"}
fracs1 = { }

class db_names():
    id = "id"
    exp = "exp"
    lvl = "lvl"
    countryid = "countryid"
    quest = "exp +1"
    winscounter = "winscounter"
    stop = "Stop"

class event_calls():
    hero = "hero"
    quest = "exp +1"
    stat = "Статистика"
    duel = "Дуэль"

class messages():
    ok = 'Ok'
    admin_func = 'Функционал для админов'
    select_frac = 'Выберите фракцию'
    you_faction = "Вами выбрана фракция: "
    win = "Победа"
    lose = "Поражение"
    fight_yourself = "Нельзя драться с собой"
    wins = "Побед:"

plus = " + 1"

def set_fracs_list():
    for i in range(1, fracs_quantity + 1):
        fracs1[fracs0[i]] = i