import sqlite3 as sq

class config():
	
	def create_table(self):
		conn = sq.connect('database1.db')
		try:
			conn.execute("CREATE TABLE TABLE1 \
			(s_no INTEGER PRIMARY KEY AUTOINCREMENT, \
			date TEXT,VALUE INT );")
		except Exception, e:
			print e
		conn.close()

	def insert_values(self,date,value):
		conn = sq.connect('database1.db')
		try:
			conn.execute("INSERT INTO table1(date,VALUE) VALUES(?,?);",(date,value)	)
			conn.commit()
		except sq.OperationalError as e:
			print e
			db.create_table()
		conn.close()

	def read(self):
		conn = sq.connect('database1.db')
		cur=conn.execute("SELECT * FROM table1 ORDER BY date LIMIT 1")
		for data in cur:
			date=data[1]
			VALUE= data[2]
		print date,VALUE
		return date,VALUE
 		conn.close()

db=config() 