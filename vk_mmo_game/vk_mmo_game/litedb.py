import sqlite3
import const




class LiteDB():
    def __init__(self):
        self.conn = sqlite3.connect(const.db_name)
        self.cursor = self.conn.cursor()
    
    def selectlvls(self, exp):
        self.cursor.execute("""SELECT lvl FROM lvls WHERE exp<""" + str(exp))
        self.conn.commit()
        return self.cursor.fetchall()

    def update(self, field, value, where, condition):
        self.cursor.execute("""UPDATE users SET """ + str(field) + """ = """ + str(value) + """ WHERE """ + str(where) + """ = """ + str(condition))
        self.conn.commit()
        return self.cursor.fetchall()
    
    def select(self, field0, field1, value):
        self.cursor.execute("""SELECT """ + str(field0) + """ FROM users WHERE """ + str(field1) + """ = """ + str(value))
        self.conn.commit()
        return self.cursor.fetchall() 

    def set(self, field, value, user_id):
        self.update(field, value, """id""", user_id)
        return self.cursor.fetchall()

    def get(self, field, user):
        return self.select(field, """id""", user)
    
    def insert_new(self, user_id):
        message = """INSERT INTO users VALUES ( """ + str(user_id) + """, """ + const.begin_gold + """, """ + const.beging_exp + """, """ + const.begin_lvl +  """, """ + const.begin_country +  """, """ + """NULL""" +  """, """ + const.begin_win + """ )"""
        self.cursor.execute(message)
        self.conn.commit()

    def checklvl(self, exp, user_id):
        return self.selectlvls(exp)[0][0]
