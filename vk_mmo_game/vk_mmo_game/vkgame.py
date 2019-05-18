import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

from litedatabase import LiteDatabase
from player import Player
import keyboard
import logger
import constants

class Game():
    def __init__(self):
        logger.logger()
        vk_session = vk_api.VkApi(token = constants.token)
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
        while self.is_running:
            #print(len(self.longpoll.check()), self.counter)
            #event = self.longpoll.check()[self.counter]
            #if event:
            for event in self.longpoll.listen():
                self._proc_event(event)
                if self.is_running == False:#Временный функционал, для тестов
                    break
           
    def _proc_event(self, event):
        if not event.from_me:
            if event.type == VkEventType.MESSAGE_NEW and event.text:
                #self.counter = self.counter + 1
                random.seed()
                database = LiteDatabase()
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
