import sys
from PyQt4 import QtCore, QtGui
from time import sleep
from ui1 import Ui_MainWindow

class disp(QtCore.QThread):
	def __init__(self,obj, parent=None):
		QtCore.QThread.__init__(self, parent)
		self.obj=obj
		self.i=False
		self.signal_disp = QtCore.SIGNAL("hello") 
		

	def run(self): 	
		while 1:
			if self.i:
				self.emit(self.signal_disp)
				sleep(0.5)



class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		print "1"
		QtGui.QWidget.__init__(self, parent)
		
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.Button.clicked.connect(self.but_clicked)
		self.disp_obj=disp(self)
		self.connect(self.disp_obj,self.disp_obj.signal_disp,self.toggle)
		self.disp_obj.start()
		print "2"
	def but_clicked(self):
		self.ui.text.clear()
		self.disp_obj.i = not self.disp_obj.i
	def toggle(self):
		self.ui.text.insertPlainText("hello\n")


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	print "3"
	sys.exit(app.exec_())