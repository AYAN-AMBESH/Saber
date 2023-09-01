import sqlite3

class Database0x:
    
    def __init__(self,datadb:str="model",dbname:str="filedata"):
        self.dbname = dbname
        self.conn = sqlite3.connect(f"{datadb}.db")
        self.cur = self.conn.cursor()
    

    def checkTable(self):
        self.cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.dbname}'")
        existing_table = self.cur.fetchone()
        if existing_table is None:
            self.createTable()


    def createTable(self):
        self.cur.execute(f'CREATE TABLE "{self.dbname}" ("Sno" int PRIMARY KEY,"hash_value_of_file" text,"data" BLOB)')
        self.conn.commit()
        self.conn.close

    