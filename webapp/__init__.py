from flask import Flask,render_template,redirect,request,flash
from datetime import datetime as dt
import time as t
from conf_sq import db
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
	try:
		date,value=db.read()
	except Exception,e:
		date="table empty"
		value=-1
		print e
	return render_template("table.html",date=date,value=value)	


if __name__ == '__main__':
	db.create_table()
	
	app.run('0.0.0.0',debug=True)
	
