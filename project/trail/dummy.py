import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
from u1 import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
	
  
	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())