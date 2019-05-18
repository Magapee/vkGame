import json

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def getKeyOne():
    keyboard1 = {
        "one_time": False,
        "buttons": [
        [get_button(label="hero", color="positive"), get_button(label="exp +1", color="positive")],
        [get_button(label="Дуэль", color="positive"), get_button(label="Статистика", color="positive")],
        [get_button(label="Stop", color="negative")]
        ]
    }
    keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
    keyboard1 = str(keyboard1.decode('utf-8'))
    return(keyboard1)

def getKeyTwo():
    keyboard2 = {
        "one_time": True,
        "buttons": [
        [get_button(label="Сумрачный замок", color="primary")],
        [get_button(label="Мятный замок", color="positive")],
        [get_button(label="Пидорский замок", color="negative")]
        
        ]
    }
    keyboard2 = json.dumps(keyboard2, ensure_ascii=False).encode('utf-8')
    keyboard2 = str(keyboard2.decode('utf-8'))
    return(keyboard2)
