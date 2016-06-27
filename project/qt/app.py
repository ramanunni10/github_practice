import sys
from PyQt4 import QtGui
from u1 import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#insert value to text view
		self.ui.text.insertPlainText("hello")
		self.ui.text.insertPlainText("  hello")
		

		#

		maxCnt = 3
		
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