from flask import Flask,render_template,redirect,request,flash
from datetime import datetime as dt
import time as t
from conf_sq import config
app=Flask(__name__)
app.secret_key="this is secret key"

@app.route('/',methods=['GET','POST'])
def home():
	if request.method == 'POST':
		name=request.form['username']
		passw=request.form['password']
		if name =='user' and passw =='password':
			return redirect('/table')
		else:
			flash("password wrong")
	return render_template("home.html")

@app.route('/table')
def table():
	
	date,value=read()
	'''read value from data base'''


	return render_template("table.html",date=date,value=v)	


if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)

