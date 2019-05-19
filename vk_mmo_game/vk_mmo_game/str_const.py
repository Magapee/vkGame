
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
fracs0 = {1:'Сумрачный замок', 2:'Мятный замок', 3:'Пидорский замок'}
fracs1 = { }

def set_fracs_list():
    for i in range(1, fracs_quantity):
        fracs1[i] = fracs0[i]