import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from litedb import LiteDB
from player import Player
import keyboard
import logger
import const
import vk_tocken


class Game():
    def __init__(self):
        logger.logger()
        vk_session = vk_api.VkApi(token = vk_tocken.tocken)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            logger.log(error_msg)
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
        self.is_running = True
        #self.counter = 0
        self.player = Player()

    def process(self):
        #counter = 0
        while self.is_running:
            event = self.longpoll.check()[0]
            if event:
                self._proc_event(event)

           
    def _proc_event(self, event):
        if not event.from_me:
            if event.type == VkEventType.MESSAGE_NEW and event.text:
                #self.counter = self.counter + 1
                random.seed()
                database = LiteDB()
                #---------------------------------------------------------------stop
                self.is_running = self.player.stop(self.vk, event)
                #---------------------------------------------------------------stop
                self.player.reg(self.vk, event, database)#Регистрация
                if self.player.is_registered(event.user_id, database):#Проверка для ивентов
                    self.player.quest(self.vk, event, database)
                    self.player.hero(self.vk, event, database)
                    self.player.get_battle_link(self.vk, event, database)
                    self.player.check_battle_link(self.vk, event, database)
                    self.player.get_battle_stats(self.vk, event, database)