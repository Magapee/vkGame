import json
import const

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def getKey(number, user_id):
    if user_id in const.admins:
        if number == 1:
            keyboard = {
                "one_time": True,
                "buttons": [
                [get_button(label="Сумрачный замок", color="primary")],
                [get_button(label="Мятный замок", color="positive")],
                [get_button(label="Пидорский замок", color="negative")],
                [get_button(label="Stop", color="negative")]
            ]
        }
        elif number == 2:
            keyboard = {
                "one_time": False,
                "buttons": [
                [get_button(label="hero", color="positive"), get_button(label="quest", color="positive")],
                [get_button(label="Дуэль", color="positive"), get_button(label="Статистика", color="positive")],
                [get_button(label="Stop", color="negative")]
                ]
            }
    else:
        if number == 1:
            keyboard = {
                "one_time": True,
                "buttons": [
                [get_button(label="Сумрачный замок", color="primary")],
                [get_button(label="Мятный замок", color="positive")],
                [get_button(label="Пидорский замок", color="negative")]
            ]
        }
        elif number == 2:
            keyboard = {
                "one_time": False,
                "buttons": [
                [get_button(label="hero", color="positive"), get_button(label="quest", color="positive")],
                [get_button(label="Дуэль", color="positive"), get_button(label="Статистика", color="positive")],
                ]
            }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard
