import sqlite3
import const




class LiteDB():
    def __init__(self):
        self.conn = sqlite3.connect(const.db_name)
        self.cursor = self.conn.cursor()

    def update(self, field, value, where, condition):
        self.cursor.execute("""UPDATE users SET """ + str(field) + """ = """ + str(value) + """ WHERE """ + str(where) + """ = """ + str(condition))
        self.conn.commit()
        return self.cursor.fetchall()

    def select(self, field0, field1, value, database = """users"""):
        self.cursor.execute("""SELECT """ + str(field0) + """ FROM """ + database + """ WHERE """ + str(field1) + """ = """ + str(value))
        self.conn.commit()
        return self.cursor.fetchall()

    def select_wcondition(self, field0, field1, condition, database):
        self.cursor.execute("""SELECT """ + str(field0) + """ FROM """ + database + """ WHERE """ + str(field1) + """ """ + str(condition))
        self.conn.commit()
        return self.cursor.fetchall()

    def set(self, field, value, user_id):
        self.update(field, value, """id""", user_id)
        return self.cursor.fetchall()

    def get(self, field, user):
        return self.select(field, """id""", user)
    
    def insert_new(self, user_id):
        message = """INSERT INTO users VALUES ( """ + str(user_id) + """, """ + const.begin_gold + """, """ + const.beging_exp + """, """ + const.begin_lvl +  """, """ + const.begin_country +  """, """  + const.begin_win +  """, """ + const.begin_state +  """, """ + const.begin_atk +  """, """ + const.begin_health +  """, """ + const.begin_quest_end + """ )"""
        self.cursor.execute(message)
        self.conn.commit()
