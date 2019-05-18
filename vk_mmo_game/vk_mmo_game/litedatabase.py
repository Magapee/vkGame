import sqlite3

class LiteDatabase():
    def __init__(self):
        self.conn = sqlite3.connect("Users.db")
        self.cursor = self.conn.cursor()
    
    def checklvl(self, exp, user_id):
        if self.selectlvls(exp) == []:
            return 1
        else:
            return(self.selectlvls(exp)[0][0])
        
    def selectlvls(self, exp):
        self.cursor.execute("""SELECT lvl FROM lvls WHERE exp<""" + str(exp))
        self.conn.commit()
        return(self.cursor.fetchall())
    
    def select(self, field0, field1, value):
        self.cursor.execute("""SELECT """ + str(field0) + """ FROM users WHERE """ + str(field1) + """= """ + str(value))
        self.conn.commit()
        return(self.cursor.fetchall())

    def update(self, field, value, user_id, param = "id"):
        self.cursor.execute("""UPDATE users SET """ + str(field) + """ = """ + str(value) + """ WHERE """ + param + """ = """ + str(user_id))
        self.conn.commit()
        return(self.cursor.fetchall())

    def insert(self, user_id, name):
        self.cursor.execute("""INSERT INTO users VALUES ( """ + str(user_id) + """, '""" + str(name) + """', 0, 0, 1, 0, NULL, 0)""")
        self.conn.commit()
