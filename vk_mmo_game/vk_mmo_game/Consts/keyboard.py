import json
import const


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
