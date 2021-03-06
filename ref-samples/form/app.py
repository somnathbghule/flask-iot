#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            print(request.form['username'])
            print(request.form['password'])
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
if __name__ == '__main__':       
    app.run(debug=True, host='0.0.0.0')
