import sqlite3
import const
import str_const
from const import Begin
from str_const import UsersColumns

#TODO change the order of methods

class DB():
    def __init__(self, db_name):
        self.name = db_name
        self.db = sqlite3.connect(const.db_name)
        self.cursor = self.db.cursor()
        self._init_users_tb()

    def _init_users_tb(self): #initializing users db, creating it if not exists
        request = """CREATE TABLE IF NOT EXISTS users ("""
        for key in UsersColumns:
            request += key + ' ' + UsersColumns[key][0] + ', '
        request = request[0:-2]
        request += ')'
        self._execute(request)

    def _execute(self, statement):
        self.cursor.execute(statement)
        self.db.commit()
        return self.cursor.fetchall()

    def get_players(self): #returns array of users
        return self._execute("""SELECT * FROM """ + str_const.users_tb)

    def update_user(self, user):
        request = """INSERT OR REPLACE INTO users("""
        for el in user:
            request += el + ', '
        request = requst[0:-2]
        request += ')'
        return self._execute(request)
        
    def insert_new(self, user_id): #comment
        self._execute("""INSERT INTO users VALUES ( """ 
                            + str(user_id) + """, """ 
                            + Begin.gold + """, """ 
                            + Begin.exp + """, """ 
                            + Begin.lvl +  """, """ 
                            + Begin.country +  """, """  
                            + Begin.win  +  """, """ 
                            + Begin.state +  """, """ 
                            + Begin.attack +  """, """ 
                            + Begin.health +  """, """ 
                            + Begin.quest_end + """ )""")