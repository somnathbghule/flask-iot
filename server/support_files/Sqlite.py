#!/usr/bin/python3

import sqlite3

class SqliteDatabase():
    def __init__(self):
        self.dbName_="ia_iot.db"
        self.conn_=sqlite3.connect(self.dbName_)
        self.cur_=self.conn_.cursor()
        self.dhtTableName_="DHT_data"
        print("database opened sucessfully.")
    def DHTTableName(self):
        return self.dhtTableName_
    def DoQuery(self, query):
        return self.cur_.execute(query)
        self.conn_.commit();
        
    def DHTTable(self):
        self.cur_.execute("DROP TABLE IF EXISTS %s" % (self.DHTTableName()))
        self.cur_.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
        self.conn_.commit()
        print("DHT_data table created sucessfully.")

    def AddTODHTTable(self, temp, hum):
        self.cur_.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
        self.conn_.commit()
    
    def __del__(self):
        print("database closed sucessfully.")
        self.conn_.close(); 

if __name__=='__main__':
    litedb=SqliteDatabase()
    litedb.DHTTable()
    litedb.AddTODHTTable(20, 45)
    litedb.AddTODHTTable(10, 55)
    #query="select *from %s " % ("DHT_data")
    #print(litedb.DoQuery(query))

    
