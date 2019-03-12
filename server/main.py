#!/usr/bin/python3
from flask import Flask, render_template, request, g, current_app
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/support_files'))
import sqlite3
from support_files.Sqlite import SqliteDatabase
from support_files.IoTSupport import Warn, LogDebug
import logging
from logging.handlers import RotatingFileHandler

false=0
true=1
signed_in=false

ledRed="This is red led"

app = Flask(__name__)
def myfun():
    LogDebug("action called")

@app.route('/')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    LogDebug("login called"); 
    if signed_in==false:
        return render_template('login.html', **templateData)
    else:
        return render_template('index.html', **templateData)


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    print ("sign up called")
    return render_template('signup.html')

@app.route('/authenticat', methods = ['POST'])
def authenticate():
   LogDebug("authenticat called")    
   if request.method == 'POST':
       if request.form['signin'] == 'submit':
           if request.form['userId'] == 'admin' and request.form['userPassword'] == 'admin':
               return render_template('index.html', **templateData)
           else:
    	       return render_template('login.html', **templateData)

@app.route('/index')
def index():        
    sql=SqliteDatabase(get_db, close_db)
    return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
	LogDebug(glob_var)
	if deviceName == 'ledRed':
		actuator=ledRed
	if action == 'on':
		LogDebug("on the led red.")
	if action == 'off':
		LogDebug("off the led red.")
	templateData={
		'ledRed': action,
        'fun':myfun
	}
	return render_template('index.html', **templateData )

@app.route('/plots')
def plots():
    LogDebug ("plot something")
    sql=SqliteDatabase(get_db, close_db)
    sql.GetAllFromEmployeeTable()
    return render_template('plots.html')

@app.route('/chart')
def chart():
    labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ];
    values = ['Day off', 'Day off', 'Work day', 'Day off', 'Work day', 'Day off', 'Work day']
    return render_template('chart.html', values=values, labels=labels)

@app.route('/bar')
def bar():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('bar.html', values=values, labels=labels)

@app.route('/linebar')
def linebar():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('linebar.html', values=values, labels=labels)

@app.route('/piechart')
def piechart():
    #labels = ["January","February","March","April","May","June","July","August"]
    #values = [10,9,8,7,6,4,7,8]
    #colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    labels = [ "Mark","John","Max","Tom" ]
    values = [ 50, 100,150, 180 ]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C" ]
    return render_template('piechart.html', set=zip(values, labels, colors))

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

#for defining global variables
with app.app_context():
    LogDebug (app.name + " Application Started.")
    glob_var=100
    templateData={
        'fun':myfun
    }

@app.teardown_appcontext
def teardown_app(exception):
    LogDebug (app.name + " url: ")
    #LogDebug (request.url)


if __name__ == '__main__':
    #handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    #handler.setLevel(logging.INFO)
    #app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0')
