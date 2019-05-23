class Emoji:
    gold = "&#128176;"
    fire = "&#128293;"
    lightning = "&#9889;"
    sword = "&#9876;"
    shield = "&#128737;"
    gun = "&#128299;"
    dagger = "&#128481;"
    bow = "&#371771;"
    heart = "&#10084;"

str_end = ": "
quote = '"'

class Words:
    lvl = "Уровень"
    exp = "Опыт"
    gold = "Золото"
    health = "Здоровье"
    attack = "Атака"
    guild_name = "[Имя гильдии]"
    status = "Состояние"
    seconds = " секунд"

class Strs:
    lvl = Emoji.lightning + Words.lvl + str_end
    exp = Emoji.fire + Words.exp + str_end
    gold = Emoji.gold + Words.gold + str_end
    health = Emoji.heart + Words.health + str_end
    attack = Emoji.dagger + Words.attack + str_end
    status = Words.status + str_end


class NameCase: #падежи
    nom = "nom" #именительный
    gen = "gen" #родительный
    dat = "dat" #дательный
    acc = "acc" #винительный
    ins = "ins" #творительный
    abl = "abl" #предложный




fracs_quantity = 3
fracs0 = {1:"Сумрачный замок", 2:"Мятный замок", 3:"Пидорский замок"}
fracs1 = { }
states = {1:'Отдых', 2:'В поисках пиздюлей, осталось:'}

class DbNames():
    id = "id"
    exp = "exp"
    lvl = "lvl"
    countryid = "countryid"
    quest = "exp +1"
    winscounter = "winscounter"
    stop = "Stop"
    state = "state"
    quest_end = "quest_end"
    health = "health"
    attack = "attack"

class EventCalls():
    hero = "hero"
    quest = "quest"
    stat = "Статистика"
    duel = "Дуэль"

class Messages():
    ok = 'Ok'
    admin_func = 'Функционал для админов'
    select_frac = 'Выберите фракцию'
    you_faction = "Вами выбрана фракция: "
    win = "Победа"
    lose = "Поражение"
    fight_yourself = "Нельзя драться с собой"
    wins = "Побед: "
    in_duel_with = "в сражении с"
    with_link = "по"
    quest = "Ты отправился искать приключения на свою жопу. Нахуя ? не понятно! Это займет "
    seconds = " секунд"
    quest_stop = "Поход нахуй окончен, ты получил exp: "

plus = " + 1"

def set_fracs_list():
    for i in range(1, fracs_quantity + 1):
        fracs1[fracs0[i]] = i