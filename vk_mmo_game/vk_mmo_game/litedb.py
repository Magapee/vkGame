import sqlite3
import const
from const import Begin

#TODO change the order of methods

class LiteDB():
    def __init__(self, db_name):
        self.name = db_name
        if _check_db:
            self.db = sqlite3.connect(const.db_name) #needed to chek for avaliability, and create

        self.cursor = self.db.cursor()

    def update(self, field, value, where, condition):
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

    def select_wcond(self, field0, field1, condition, database):
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

    def set(self, field, value, user_id):
        self.update(field, value, """id""", user_id)
        return self.cursor.fetchall()

    def get(self, field, user):
        return self.select(field, """id""", user)
    
    def insert_new(self, user_id):
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

    def _check_db(self): #check, if db exists
        raise NotImplementedError

    def _create(self):
        raise NotImplementedError