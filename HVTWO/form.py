# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Wed Dec  9 15:32:07 2015
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
        self.btnSearch.setGeometry(QtCore.QRect(700, 0, 90, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.lstSearch = QtGui.QListView(self.centralwidget)
        self.lstSearch.setGeometry(QtCore.QRect(10, 40, 260, 525))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstSearch.sizePolicy().hasHeightForWidth())
        self.lstSearch.setSizePolicy(sizePolicy)
        self.lstSearch.setObjectName(_fromUtf8("lstSearch"))
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(305, 220, 90, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.lstSimilar = QtGui.QListView(self.centralwidget)
        self.lstSimilar.setGeometry(QtCore.QRect(430, 40, 260, 525))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstSimilar.sizePolicy().hasHeightForWidth())
        self.lstSimilar.setSizePolicy(sizePolicy)
        self.lstSimilar.setObjectName(_fromUtf8("lstSimilar"))
        self.btnRem = QtGui.QPushButton(self.centralwidget)
        self.btnRem.setGeometry(QtCore.QRect(305, 320, 90, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRem.sizePolicy().hasHeightForWidth())
        self.btnRem.setSizePolicy(sizePolicy)
        self.btnRem.setObjectName(_fromUtf8("btnRem"))
        self.btnDone = QtGui.QPushButton(self.centralwidget)
        self.btnDone.setGeometry(QtCore.QRect(700, 535, 90, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDone.sizePolicy().hasHeightForWidth())
        self.btnDone.setSizePolicy(sizePolicy)
        self.btnDone.setObjectName(_fromUtf8("btnDone"))
        self.searchtext = QtGui.QLineEdit(self.centralwidget)
        self.searchtext.setGeometry(QtCore.QRect(10, 0, 681, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchtext.sizePolicy().hasHeightForWidth())
        self.searchtext.setSizePolicy(sizePolicy)
        self.searchtext.setObjectName(_fromUtf8("searchtext"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDatabase = QtGui.QMenu(self.menuBar)
        self.menuDatabase.setObjectName(_fromUtf8("menuDatabase"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionEdit_info = QtGui.QAction(MainWindow)
        self.actionEdit_info.setObjectName(_fromUtf8("actionEdit_info"))
        self.menuDatabase.addAction(self.actionEdit_info)
        self.menuBar.addAction(self.menuDatabase.menuAction())

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
        self.menuDatabase.setTitle(_translate("MainWindow", "Database", None))
        self.actionEdit_info.setText(_translate("MainWindow", "Edit info...", None))
        self.actionEdit_info.setShortcut(_translate("MainWindow", "Ctrl+E", None))

