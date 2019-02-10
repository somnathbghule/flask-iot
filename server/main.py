#!/usr/bin/python3
from flask import Flask, render_template, request, g, current_app
import os
import sys
sys.path.append(os.path.abspath('support_files'))
import sqlite3
from support_files.Sqlite import SqliteDatabase
from support_files.IoTSupport import Warn, LogDebug

false=0
true=1
signed_in=false

ledRed="This is red led"

app = Flask(__name__)
@app.route('/')


@app.route('/login',methods = ['POST', 'GET'])
def login():
    LogDebug("login called"); 
    if signed_in==false:
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    print ("sign up called")
    return render_template('signup.html')

@app.route('/authenticate', methods = ['POST'])
def authenticate():
   print("authenticat called")    
   if request.method == 'POST':
       if request.form['signin'] == 'submit':
           if request.form['userId'] == 'admin' and request.form['userPassword'] == 'admin':
               return render_template('index.html')
           else:
    	       return render_template('login.html')

@app.route('/index')
def index():        
    sql=SqliteDatabase(get_db, close_db)
    return render_template('index.html')
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
	if deviceName == 'ledRed':
		actuator=ledRed
	if action == 'on':
		print("on the led red.")
	if action == 'off':
		print("off the led red.")
	templateData={
		'ledRed': 'On'
	}
	return render_template('index.html', **templateData )

@app.route('/plots')
def plots():
	LogDebug ("plot something")
	sql=SqliteDatabase(get_db, close_db)
	sql.GetAllFromEmployeeTable()	
	return render_template('plots.html')

def get_db(db_name):
	with app.app_context():
		db = getattr(g, '_database', None)
		if db is None:
			db = g._database = sqlite3.connect(db_name)
			LogDebug("data base opened: "+db_name)
		return db

def close_db():
	db = getattr(g, '_database', None)
	LogDebug("close_db called.")
	if db is not None:
		LogDebug("connection closed.")
		db.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
