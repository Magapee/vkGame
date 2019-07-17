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
        _init_users_tb()

    def _init_users_tb(self): #initializing users db, creating it if not exists
        request = """CREATE TABLE IF NOT EXISTS users ("""
        for key in UsersColumns:
            request += key + ' ' + UsersColumns[key] + ', '
        request = request[0:-2]
        request += ')'
        self.cursor.execute(request)
        self.db.commit()

    def get_users(self): #returns array of users
        self.cursor.execute("""SELECT * FROM""" + str_const.users_tb)
        self.db.commit()
        return self.cursor.fetchall()

    def update(self, field, value, where, condition): #comment
        self.cursor.execute("""UPDATE users SET """
                           + str(field) 
                           + """ = """ 
                           + str(value) 
                           + """ WHERE """ 
                           + str(where) 
                           + """ = """ 
                           + str(condition))
        self.db.commit()
        return self.cursor.fetchall() #comment

    def select(self, field0, field1, value, database = """users"""): #what is it field0 and field1? TODO better naming and comments
        return self.select_wcond(field0, field1, """ = """ + str(value), database)

    def select_wcond(self, field0, field1, condition, database): #comment
        self.cursor.execute("""SELECT """ 
                            + str(field0) 
                            + """ FROM """ 
                            + database 
                            + """ WHERE """ 
                            + str(field1) 
                            + """ """ 
                            + str(condition))
        self.db.commit()
        return self.cursor.fetchall()

    def set(self, field, value, user_id): #comment
        self.update(field, value, """id""", user_id)
        return self.cursor.fetchall()

    def get(self, field, user): #comment
        return self.select(field, """id""", user)
    
    def insert_new(self, user_id): #comment
        self.cursor.execute("""INSERT INTO users VALUES ( """ 
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
        self.db.commit()