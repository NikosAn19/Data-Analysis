import sqlite3
from os import mkdir


class connection:
    def __init__(self):
        try:
            self.db = sqlite3.connect('Database/equipment.db')
        except sqlite3.OperationalError:
            mkdir('Database')
        finally:
            self.db = sqlite3.connect('Database/equipment.db')
        # self.db = sqlite3.connect('motoparts.db')
        cursor = self.db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS PCs(
                           macAddress TEXT,
                           ip TEXT,
                           section TEXT,
                           service TEXT,
                           user TEXT,
                           pc_name TEXT,
                           processor TEXT,
                           ram DOUBLE,
                           windows_license TEXT,
                           office_licence TEXT,
                           PRIMARY KEY(macAddress)
                 )""")
        self.db.commit()
        print('table created')
        cursor.execute("""CREATE TABLE IF NOT EXISTS Repairs(
                                   macAddress TEXT,
                                   repair TEXT,
                                   update TEXT,
                                   service TEXT,
                                   user TEXT,
                                   pc_name TEXT,
                                   processor TEXT,
                                   ram DOUBLE,
                                   windows_license TEXT,
                                   office_licence TEXT,
                                   PRIMARY KEY(macAddress)
                         )""")
    # def __init__(self):
    #     self.db = mysql.connector.connect(
    #         host='127.0.0.1',
    #         user='nikos',
    #         password='pergaminos007!',
    #         port='3306',
    #         database='MotoParts'
    #     )

    def select_query(self, str_sql):
        cursor = self.db.cursor()
        cursor.execute(str_sql)
        result = cursor.fetchall()
        return result

    def insert_query(self, str_sql, data):
        cursor = self.db.cursor()
        cursor.execute(str_sql, data)
        self.db.commit()

    def delete_query(self, str_sql, data):
        cursor = self.db.cursor()
        cursor.execute(str_sql, data)
        self.db.commit()

    def init_table(self):
        cursor = self.db.cursor()
        return cursor

    def update_query(self, str_sql):
        cursor = self.db.cursor()
        print(str_sql)
        cursor.execute(str_sql)
        self.db.commit()
