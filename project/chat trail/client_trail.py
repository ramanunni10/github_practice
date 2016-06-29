import sys
import socket
from conf_sq2 import db
from PyQt4 import QtCore,QtGui
from u1 import Ui_MainWindow



class WorkThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)
		self.signal_DATA_RECIEVE = QtCore.SIGNAL("DATA_RECIEVE")
		self.s=0
		self.s= socket.socket()
		self.s.connect(('127.0.0.1',1234))

	def run(self):

		try:
			while 1:
				try:
					
					reply=self.s.recv(1024)
		
					dc,tc=reply.split(',')
					db.insert_values(dc,tc)
					self.emit(self.signal_DATA_RECIEVE)
				
				except Exception, e:
					print 'send: ', e
				if reply =='q':
					break
				print "server:"+str(reply)
		finally:
			self.s.close()





###############################################
class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
		print("one")
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.ui.table_2.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.wt_obj=WorkThread()
		self.connect(self.wt_obj,self.wt_obj.signal_DATA_RECIEVE,self.data)
		self.wt_obj.start()
		#insert value to text view

	def data(self,):
			self.ui.table_2.setRowCount(1)
			datec,timec=db.read_one()
			self.ui.table_2.setItem(0, 0, QtGui.QTableWidgetItem(datec))
			self.ui.table_2.setItem(0, 1, QtGui.QTableWidgetItem(str(timec)))
			count =0
			cursor=db.read_all()
			for data in cursor:
				datec=data[1]
				VALUEc= data[2]
				self.ui.table.setRowCount(count+1)
				self.ui.table.setItem(count, 0, QtGui.QTableWidgetItem(datec))
				self.ui.table.setItem(count, 1, QtGui.QTableWidgetItem(str(VALUEc)))
				count=count+1	
			
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())