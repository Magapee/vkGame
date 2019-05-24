import sqlite3
import const
from const import Begin




class LiteDB():
    def __init__(self):
        self.conn = sqlite3.connect(const.db_name)
        self.cursor = self.conn.cursor()

    def update(self, field, value, where, condition):
        self.cursor.execute("""UPDATE users SET """
                           + str(field) 
                           + """ = """ 
                           + str(value) 
                           + """ WHERE """ 
                           + str(where) 
                           + """ = """ 
                           + str(condition))
        self.conn.commit()
        return self.cursor.fetchall()

    def select(self, field0, field1, value, database = """users"""):
        return self.select_wcondition(field0, field1, """ = """ + str(value), database)

    def select_wcondition(self, field0, field1, condition, database):
        self.cursor.execute("""SELECT """ + str(field0) + """ FROM """ + database + """ WHERE """ + str(field1) + """ """ + str(condition))
        self.conn.commit()
        return self.cursor.fetchall()
    
    def select_order(self, field, order, database = """users"""):
        self.cursor.execute("""SELECT """ + str(field) + """ FROM """ + database + """ ORDER BY """ + order + " DESC")
        self.conn.commit()
        return self.cursor.fetchall()

    def select_all_ids(self):
        self.cursor.execute("""SELECT id FROM users""")
        self.conn.commit()
        return self.cursor.fetchall()

    def set(self, field, value, user_id):
        self.update(field, value, """id""", user_id)
        return self.cursor.fetchall()

    def get(self, field, user):
        return self.select(field, """id""", user)
    
    def insert_new(self, user_id):
        message = """INSERT INTO users VALUES ( """ + str(user_id) + """, """ + Begin.gold + """, """ + Begin.exp + """, """ + Begin.lvl +  """, """ + Begin.country +  """, """  + Begin.win +  """, """ + Begin.state +  """, """ + Begin.attack +  """, """ + Begin.health +  """, """ + Begin.quest_end + """ )"""
        self.cursor.execute(message)
        self.conn.commit()
