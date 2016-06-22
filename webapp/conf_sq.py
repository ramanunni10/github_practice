import sqlite3 as sq

class config():
	conn = sq.connect('database.db')
	def create_table():
		conn.execute("CREATE TABLE TABLE1 \
			(s_no INTEGER PRIMARY KEY AUTOINCREMENT, \
			date TEXT,VALUE INT );")
	def insert_values(date,value):
		conn.execute("INSERT INTO table1(date,VALUE) VALUES(?,?);",(date,value))
		conn.commit()

	def read():
		cur=conn.execute("SELECT * FROM table1 ORDER BY date DESC LIMIT 1")
		for data in cur:
			date=data[1]
			VALUE= data[2]
		print date,VALUE
		return date,VALUE
