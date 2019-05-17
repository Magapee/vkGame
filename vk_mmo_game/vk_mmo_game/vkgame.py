import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#from litedb import LiteDatabase
#from player import Player
from vk_token import token


class Game(object):
    def __init__(self):
        print('Starting...') #заменить на логгер
        self.is_running = False

        self.vk_session = vk_api.VkApi(token = token)
        self.vk_session._auth_token()
        self.vk = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)

        self.is_running = True

        print('Started!')

    def process(self):
        while self.is_running:
            event = self.lonlongpoll.check()
            if event:
                _proc_event(event)
           
    def _proc_event(self, event):
        if not event.from_me:
            if event.type == VkEventType.MESSAGE_NEW and event.text: