import random
import json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_token
import const


class Button:
    def __init__(self, label, color):
        self.label = label
        self.color = color


class Messenger:
    def __init__(self): # Подключение к серверу вк для дальнейшей работы
        vk_session = vk_api.VkApi(token = vk_token.token)
        self.vk = vk_session.get_api()
        self.long_poll = VkLongPoll(vk_session)
    
    def send_mes(self, id, mes, list_string_buttons = None, is_one_time = True): # Отправить сообщение mes (и клавиатуру с кнопками list_string_buttons) пользователю id
        keyboard = None
        if list_string_buttons is not None:
            keyboard = self._create_keyboard(list_string_buttons, is_one_time)
        random.seed()
        self.vk.messages.send(user_id = id, message = mes, random_id = random.randrange(1, const.random), keyboard = keyboard)

    def check(self): # Получить события от сервера вк 
        return self.long_poll.check()

    def _create_keyboard(self, list_string_buttons, is_one_time): # Создать клавиатуру с кнопками list_string_buttons
        table_buttons = []
        for raw_string_buttons in list_string_buttons:
            string_buttons = []
            for button in raw_string_buttons:
                string_buttons.append(_create_button(label = button.label, color = button.color))
            table_buttons.append(string_buttons)
        keyboard = {
					"one_time": is_one_time,
					"buttons": table_buttons
					}
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard


class Emoji: # emoji for vk
    gold = "&#128176;"
    fire = "&#128293;"
    lightning = "&#9889;"
    sword = "&#9876;"
    shield = "&#128737;"
    gun = "&#128299;"
    dagger = "&#128481;"
    bow = "&#371771;"
    heart = "&#10084;"

        

def _create_button(label, color, payload=""): # Создать кнопку
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


if __name__ == '__main__':
    messenger = Messenger()
    #a.send_mes(129640173, 'пиз')
    #while True:
    #    events = a.check()
    #    for event in events:
    #        if not event.from_me: 
    #            if event.type == VkEventType.MESSAGE_NEW and event.text:
    #                print(event.text)
    list_string_buttons = [
        [Button("хуй", "negative")],
        [Button("хуй", "primary"), Button("хуй", "primary")],
        [Button("хуй", "secondary"), Button("хуй", "secondary"), Button("хуй", "secondary")],
        [Button("хуй", "positive"), Button("хуй", "positive"), Button("хуй", "positive"), Button("хуй", "positive")],
        [Button("хуй", "primary")]
        ]
    messenger.send_mes(129640173, "выбор", list_string_buttons, False)