# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
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
        MainWindow.resize(428, 328)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Button = QtGui.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(60, 220, 85, 27))
        self.Button.setObjectName(_fromUtf8("Button"))
        self.text = QtGui.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(40, 80, 161, 101))
        self.text.setObjectName(_fromUtf8("text"))
        self.Button_2 = QtGui.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(280, 160, 85, 27))
        self.Button_2.setObjectName(_fromUtf8("Button_2"))
        self.line2 = QtGui.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(270, 80, 111, 41))
        self.line2.setText(_fromUtf8(""))
        self.line2.setObjectName(_fromUtf8("line2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "display", None))
        self.Button.setText(_translate("MainWindow", "STOP", None))
        self.Button_2.setText(_translate("MainWindow", "OK", None))
        self.line2.setPlaceholderText(_translate("MainWindow", "update test", None))

