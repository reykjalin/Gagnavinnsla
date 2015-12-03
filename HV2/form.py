# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Thu Dec  3 21:05:58 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(697, 10, 91, 29))
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.lstSearch = QtGui.QListView(self.centralwidget)
        self.lstSearch.setGeometry(QtCore.QRect(10, 50, 261, 531))
        self.lstSearch.setObjectName(_fromUtf8("lstSearch"))
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(310, 230, 88, 29))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.lstSimilar = QtGui.QListView(self.centralwidget)
        self.lstSimilar.setGeometry(QtCore.QRect(450, 50, 241, 521))
        self.lstSimilar.setObjectName(_fromUtf8("lstSimilar"))
        self.searchtext = QtGui.QPlainTextEdit(self.centralwidget)
        self.searchtext.setGeometry(QtCore.QRect(10, 10, 681, 31))
        self.searchtext.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.searchtext.setObjectName(_fromUtf8("searchtext"))
        self.btnRem = QtGui.QPushButton(self.centralwidget)
        self.btnRem.setGeometry(QtCore.QRect(310, 330, 88, 29))
        self.btnRem.setObjectName(_fromUtf8("btnRem"))
        self.btnDone = QtGui.QPushButton(self.centralwidget)
        self.btnDone.setGeometry(QtCore.QRect(700, 540, 91, 29))
        self.btnDone.setObjectName(_fromUtf8("btnDone"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "What should you watch?", None))
        self.btnSearch.setText(_translate("MainWindow", "Search", None))
        self.btnSearch.setShortcut(_translate("MainWindow", "Return", None))
        self.btnAdd.setText(_translate("MainWindow", "Add -->", None))
        self.btnAdd.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.btnRem.setText(_translate("MainWindow", "<-- Remove", None))
        self.btnRem.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.btnDone.setText(_translate("MainWindow", "Done", None))
        self.btnDone.setShortcut(_translate("MainWindow", "Ctrl+D", None))

