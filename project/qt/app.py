import sys
import socket
from PyQt4 import QtCore,QtGui
from u1 import Ui_MainWindow


#worker thread====client.py
class WorkThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)
		self.signal("DATA_RECIEVE")
		self.s=0
		self.s= socket.socket()
		self.s.connect(('127.0.0.1',12345))

	def recieve():
	
		try:
			while 1:
				try:
					reply=self.s.recv(1024)
				except Exception, e:
					reply = 0
					print 'send: ', e
				if reply =='q':
					break
				print "server:"+reply
	def run(self): 	
		while 1:
			if self.i:
				
				self.emit(self.signal_DATA_RECIEVE)
				sleep(0.5)



###############################################33
class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.wt_obj=WorkThread(self)
		self.connect(self.wt_obj,self.wt_obj.signal_DATA_RECIEVE,self.data)
		#insert value to text view
			

		#
	def data(self,):
		maxCnt = 3
			self.ui.text.insertPlainText("s_no\tDATE\t       TEMPERAT   URE\n")
		self.ui.text.insertPlainText("120\t28-06-2016 12:33:21\t130")
		for i in range(maxCnt):
			self.ui.table.setRowCount(i+1)			
			self.ui.table.setItem(i, 0, QtGui.QTableWidgetItem(str(i)))
			self.ui.table.setItem(i, 1, QtGui.QTableWidgetItem(str(i*2)))
			self.ui.table.setItem(i, 2, QtGui.QTableWidgetItem(str(i*3)))





if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())