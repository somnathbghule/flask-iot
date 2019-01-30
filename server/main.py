#!/usr/bin/python3
from flask import Flask, render_template, request
import os
false=0
true=1
signed_in=false

ledRed="This is red led"

app = Flask(__name__)
@app.route('/')


@app.route('/login',methods = ['POST', 'GET'])
def login():
    print("login called---------", signed_in)	
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
	print ("plot something")
	return render_template('plots.html')



if __name__ == '__main__':       
    app.run(debug=True, host='0.0.0.0')
