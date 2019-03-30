#!/usr/bin/python3

from flask import g
import sqlite3
import os
from IoTSupport import LogDebug

class Job():
    def __init__(self, jobid, id):
        self.__jobid=jobid
        self.__id=id
    def jobid(self):
        return self.__jobid
    def id(self):
        return self.__id

class Employee():
	def __init__(self,eid, ename):
		self.eid_=eid
		self.ename_=ename
	def eid(self):
		return self.eid_
	def ename(self):
		return self.ename_
		

class SqliteDatabase():
    def __init__(self, get_db, close_db):
        self.dbName_= os.path.dirname(os.path.abspath(__file__)) +"/ia_iot.db"
        self.conn_=get_db(self.dbName_)
        self.cur_=self.conn_.cursor()
        self.dhtTableName_="DHT_data"
        self.close_db=close_db
    def DHTTableName(self):
        return self.dhtTableName_
    def EmployeeTableName(self):
        return "Employee_data"
    def JobTableName(self):
        return "Job_data"
    def DoQuery(self, query):
        return self.cur_.execute(query)
        self.conn_.commit();
        
    def CreateDHTTable(self):
        self.cur_.execute("DROP TABLE IF EXISTS %s" % (self.DHTTableName()))
        self.cur_.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
        self.conn_.commit()
        LogDebug("DHT_data table created sucessfully.")
    
    def AddTODHTTable(self, temp, hum):
        self.cur_.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
        self.conn_.commit()
   
    def CreateEmployeeTable(self):
        self.cur_.execute("DROP TABLE IF EXISTS %s" % (self.EmployeeTableName()))
        self.cur_.execute("CREATE TABLE %s(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL)"%(self.EmployeeTableName()))
        self.conn_.commit()
    
    def AddTOEmployeeTable(self, id, name):
        self.cur_.execute("INSERT INTO Employee_data values((?), (?))", (id, name))
        self.conn_.commit()

    def GetAllFromEmployeeTable(self):
        self.cur_.execute("select * from %s" % (self.EmployeeTableName()))
        rows=self.cur_.fetchall()
        employees=[]
        for row in rows:
            #print(row[0])
            employees.append(Employee(row[0], row[1]))
        return employees
			
    def CreateJobTable(self):
        self.cur_.execute("DROP TABLE IF EXISTS %s" % (self.JobTableName()))
        self.cur_.execute("CREATE TABLE %s(JOBID INT PRIMARY KEY NOT NULL, ID INT NOT NULL)"%(self.JobTableName()))
    
    def AddToJobTable(self, jobid, id):
        self.cur_.execute("INSERT INTO Job_data values((?), (?))", (jobid, id))
        self.conn_.commit()
  
    def AddToJobTableByList(self, jobList):
        for job in jobList:
            self.cur_.execute("INSERT INTO Job_data values((?), (?))", (job.jobid(), job.id()))
            self.conn_.commit()
    
    def __del__(self):
        self.close_db() 

if __name__=='__main__':
    litedb=SqliteDatabase()
    litedb.CreateJobTable()
    litedb.AddToJobTableByList([Job(1,1001), Job(2, 1001), Job(3, 1002)])

    #litedb.CreateEmployeeTable()
    #litedb.AddTOEmployeeTable(1001, "Somnath")
    #litedb.AddTOEmployeeTable(1002, "Pranav")
    #litedb.AddTOEmployeeTable(1003, "Swapnil")
    #litedb.AddTOEmployeeTable(1004, "Rakesh")
    #litedb.CreateDHTTable()
    #litedb.AddTODHTTable(20, 45)
    #litedb.AddTODHTTable(10, 55)
    #query="select *from %s " % ("DHT_data")
    #print(litedb.DoQuery(query))

    
