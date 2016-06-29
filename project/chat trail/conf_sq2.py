import sqlite3 as sq

class config():
	
	def create_table(self):
		conn = sq.connect('end_user.db')
		try:
			conn.execute("CREATE TABLE TABLE1 \
			(s_no INTEGER PRIMARY KEY AUTOINCREMENT, \
			date TEXT,VALUE INT );")
		except Exception, e:
			print e
		conn.close()

	def insert_values(self,date,value):
		conn = sq.connect('end_user.db')
		try:
			conn.execute("INSERT INTO table1(date,VALUE) VALUES(?,?);",(date,value)	)
			conn.commit()
		except sq.OperationalError as e:
			print e
			db.create_table()
		conn.close()

	def read_one(self):
		conn = sq.connect('end_user.db')
		try:
			cur=conn.execute("SELECT * FROM table1 ORDER BY date DESC LIMIT 1")
			for data in cur:
				date=data[1]
				VALUE= data[2]
		except sq.OperationalError as e:
			print e
			db.create_table()			
		conn.close()
		return date,VALUE
 		

 	def read_all(self):
 		conn = sq.connect('end_user.db')
 		try:
			cur=conn.execute("SELECT * FROM table1 ORDER BY date DESC ")
		except sq.OperationalError as e:
			print e
			db.create_table()	
		data_list=[]
		for data in cur:
			data_list.append(data)

 		conn.close()
 		return data_list 		

db=config() 