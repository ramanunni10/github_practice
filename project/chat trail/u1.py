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
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(120, 150, 281, 192))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 50, 85, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, -10, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.table_2 = QtGui.QTableWidget(self.centralwidget)
        self.table_2.setGeometry(QtCore.QRect(120, 40, 281, 81))
        self.table_2.setObjectName(_fromUtf8("table_2"))
        self.table_2.setColumnCount(2)
        self.table_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.table_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(1, item)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "PLC VIEWER", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TEMPERATURE", None))
        self.pushButton.setText(_translate("MainWindow", "FAN ON", None))
        self.label.setText(_translate("MainWindow", "HOME PAGE", None))
        item = self.table_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE", None))
        item = self.table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TEMPERATURE", None))

