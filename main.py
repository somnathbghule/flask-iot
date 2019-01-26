#!/usr/bin/python3
from flask import Flask, render_template
ledRed="This is red led"
app = Flask(__name__)
@app.route('/')
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
	return render_template('plots.html')


if __name__ == '__main__':       
    app.run(debug=True, host='0.0.0.0')
