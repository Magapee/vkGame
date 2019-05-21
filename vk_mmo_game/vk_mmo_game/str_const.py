class emoji:
    gold = "&#128176;"
    fire = "&#128293;"
    lightning = "&#9889;"
    sword = "&#9876"
    shield = "&#128737"
    gun = "&#128299"
    dagger = "&#128481"
    bow = "&#371771"
    heart = "&#10084"


class words:
    lvl = "Уровень"
    exp = "Опыт"
    gold = "Золото"
    guild_name = "[Имя гильдии]"

class strs:
    lvl = emoji.lightning + words.lvl + ":"
    exp = emoji.fire + words.exp + ":"
    gold = emoji.gold + words.gold + ":"



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