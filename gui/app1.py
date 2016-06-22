import sys
from PyQt4 import QtCore, QtGui
from time import sleep
from ui1 import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button.clicked.connect(self.toggle)

    def toggle(self):
		self.ui.text.insertPlainText("hello\n")
		sleep(1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())