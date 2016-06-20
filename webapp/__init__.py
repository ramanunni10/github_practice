from flask import Flask,render_template,redirect,request,flash
from datetime import datetime as dt
import time as t
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
	time1=t.strftime('%l:%M %S%p %b %d, %Y')
	return render_template("table.html",var=time1)	


if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)

