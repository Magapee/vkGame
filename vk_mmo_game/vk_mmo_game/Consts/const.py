admins = 385124486, 308831692, 129640173
db_name = "Game.db"
random = 10 ** 100000
table_users = "users"
table_lvl = "lvl"


class Button:
    def __init__(self, label, color):
        self.label = label
        self.color = color


class ListButtons():
    start_list_buttons = [[Button("Сумрачный замок", "primary")],
                          [Button("Мятный замок", "positive")],
                          [Button("Пидорский замок", "negative")]
                          ]
    list_buttons = [[Button("hero", "positive"), Button("exp +1", "positive")],
                    [Button("Дуэль", "positive"), Button("Статистика", "positive")]
                    ]


class State():
    unregistered = '0'
    normal = '1'
    forest = '2'


class LvlsFields():
    lvl = 0
    exp = 1

wait = 3


class Begin():
    country = '0'
    gold = '0'
    exp = '0'
    lvl = '1'
    win = '0'
    attack = '1'
    health = '10'
    state = State.normal
    quest_end = 'NULL'