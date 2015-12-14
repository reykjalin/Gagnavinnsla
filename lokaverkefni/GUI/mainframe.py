# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe.ui'
#
# Created: Mon Dec 14 14:37:30 2015
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
        MainWindow.resize(1169, 782)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplframe = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplframe.sizePolicy().hasHeightForWidth())
        self.mplframe.setSizePolicy(sizePolicy)
        self.mplframe.setObjectName(_fromUtf8("mplframe"))
        self.verticalLayout.addWidget(self.mplframe)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.slyear = QtGui.QSlider(self.centralwidget)
        self.slyear.setOrientation(QtCore.Qt.Horizontal)
        self.slyear.setObjectName(_fromUtf8("slyear"))
        self.horizontalLayout.addWidget(self.slyear)
        self.txtyear = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtyear.sizePolicy().hasHeightForWidth())
        self.txtyear.setSizePolicy(sizePolicy)
        self.txtyear.setMinimumSize(QtCore.QSize(0, 0))
        self.txtyear.setMaximumSize(QtCore.QSize(70, 16777215))
        self.txtyear.setMaxLength(4)
        self.txtyear.setAlignment(QtCore.Qt.AlignCenter)
        self.txtyear.setObjectName(_fromUtf8("txtyear"))
        self.horizontalLayout.addWidget(self.txtyear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Conflict map", None))

