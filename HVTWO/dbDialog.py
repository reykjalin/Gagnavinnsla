# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbDialog.ui'
#
# Created: Wed Dec  9 15:39:06 2015
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

class Ui_dbDialog(object):
    def setupUi(self, dbDialog):
        dbDialog.setObjectName(_fromUtf8("dbDialog"))
        dbDialog.resize(400, 260)
        self.txtHost = QtGui.QLineEdit(dbDialog)
        self.txtHost.setGeometry(QtCore.QRect(80, 20, 310, 27))
        self.txtHost.setObjectName(_fromUtf8("txtHost"))
        self.label = QtGui.QLabel(dbDialog)
        self.label.setGeometry(QtCore.QRect(42, 24, 31, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtDb = QtGui.QLineEdit(dbDialog)
        self.txtDb.setGeometry(QtCore.QRect(80, 70, 310, 27))
        self.txtDb.setObjectName(_fromUtf8("txtDb"))
        self.txtUser = QtGui.QLineEdit(dbDialog)
        self.txtUser.setGeometry(QtCore.QRect(80, 120, 310, 27))
        self.txtUser.setEchoMode(QtGui.QLineEdit.Normal)
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.label_2 = QtGui.QLabel(dbDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 124, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dbDialog)
        self.label_3.setGeometry(QtCore.QRect(14, 174, 61, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtPwd = QtGui.QLineEdit(dbDialog)
        self.txtPwd.setGeometry(QtCore.QRect(80, 170, 310, 27))
        self.txtPwd.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPwd.setObjectName(_fromUtf8("txtPwd"))
        self.label_4 = QtGui.QLabel(dbDialog)
        self.label_4.setGeometry(QtCore.QRect(16, 74, 56, 17))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnOk = QtGui.QPushButton(dbDialog)
        self.btnOk.setGeometry(QtCore.QRect(305, 220, 85, 27))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))

        self.retranslateUi(dbDialog)
        QtCore.QMetaObject.connectSlotsByName(dbDialog)

    def retranslateUi(self, dbDialog):
        dbDialog.setWindowTitle(_translate("dbDialog", "Database information", None))
        self.label.setText(_translate("dbDialog", "Host:", None))
        self.label_2.setText(_translate("dbDialog", "Username:", None))
        self.label_3.setText(_translate("dbDialog", "Password:", None))
        self.label_4.setText(_translate("dbDialog", "DB name:", None))
        self.btnOk.setText(_translate("dbDialog", "PushButton", None))
        self.btnOk.setShortcut(_translate("dbDialog", "Return", None))

