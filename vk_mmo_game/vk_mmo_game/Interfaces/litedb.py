import sqlite3
import const
import str_const
from const import Begin
from str_const import UsersColumns, LvlColumns, Levels

#TODO change the order of methods

class DB():
    def __init__(self, db_name):
        self.name = db_name
        self.db = sqlite3.connect(const.db_name)
        self.cursor = self.db.cursor()
        self._init_table(const.table_users, UsersColumns)
        self._init_table(const.table_lvl, LvlColumns)
        if not self._execute(f'SELECT * FROM {const.table_lvl}'):
            self._fill_lvl_tb()

    def _init_table(self, table_name, columns_name): # initializing table_name db, creating it if not exists
        request = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        for column in columns_name:
            request += f'{column.value.name} {column.value.type}, '
        request = request[0:-2]
        request += ')'
        self._execute(request)

    def _execute(self, statement):
        self.cursor.execute(statement)
        self.db.commit()
        return self.cursor.fetchall()

    def _fill_lvl_tb(self): # заполняем таблицу уровнями и опытом
        self._execute(f'INSERT INTO {const.table_lvl} VALUES ({Levels.first.value.number}, {Levels.first.value.exp})')
        self._execute(f'INSERT INTO {const.table_lvl} VALUES ({Levels.second.value.number}, {Levels.second.value.exp})')
        self._execute(f'INSERT INTO {const.table_lvl} VALUES ({Levels.third.value.number}, {Levels.third.value.exp})')
        self._execute(f'INSERT INTO {const.table_lvl} VALUES ({Levels.fourth.value.number}, {Levels.fourth.value.exp})')
        self._execute(f'INSERT INTO {const.table_lvl} VALUES ({Levels.fifth.value.number}, {Levels.fifth.value.exp})')


    def get_players(self): # returns array of users
        return self._execute(f'SELECT * FROM {str_const.users_tb}')

    def update_user(self, user):
        request = f'INSERT OR REPLACE INTO {const.table_users}('
        for el in user:
            request += el + ', '
        request = requst[0:-2]
        request += ')'
        return self._execute(request)
        
    def insert_new(self, user_id): #comment
        self._execute(f'INSERT INTO {const.table_users} VALUES ( {user_id}, {Begin.gold}, {Begin.exp}, {Begin.lvl}, ' 
                      + f'{Begin.country}, {Begin.win}, {Begin.state}, {Begin.attack}, {Begin.health}, {Begin.quest_end})')
