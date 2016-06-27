# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd1.ui'
#
# Created by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(613, 438)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(150, 50, 291, 41))
        self.text.setObjectName(_fromUtf8("text"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(150, 120, 301, 192))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 50, 85, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DATE", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TEMP", None))
        self.pushButton.setText(_translate("MainWindow", "FAN ON", None))
        self.label.setText(_translate("MainWindow", "HOME PAGE", None))

