from PyQt4.uic import loadUiType
import sys
from PyQt4 import QtGui
Ui_dbDialog, QWidget = loadUiType('GUI/dbDialog.ui')

class DBInfo(QWidget, Ui_dbDialog):
    def __init__(self):
        super(DBInfo, self).__init__()
        self.setupUi(self)

        self.host = 'localhost'
        self.usr = 'postgres'
        self.db = ''
        self.pw = ''
        
        self.txtHost.insert(self.host)
        self.txtDb.insert(self.db)
        self.txtUser.insert(self.usr)
        self.txtPwd.insert(self.pw)
        
        self.btnOk.clicked.connect(self.saveinfo)

        ######################### Save info from textboxes to use for connections #########################
    def saveinfo(self):
        self.host = self.txtHost.text()
        self.db = self.txtDb.text()
        self.usr = self.txtUser.text()
        self.pw = self.txtPwd.text()
        closer = self.test()
        if closer:
            self.close()

    ######################### Code for testing database connetion #########################
    def test(self):
        closer = False
        self.host = self.txtHost.text()
        self.db = self.txtDb.text()
        self.usr = self.txtUser.text()
        self.pw = self.txtPwd.text()
        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.db, self.usr, self.pw)
        conninfo = str()
        
        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.close()
            conn.close()
            conninfo = 'Success! You are now connected to your database'
            closer = True
        except:
            conninfo = 'Something went wrong. Are you sure the information you entered is correct?'
        
        QtGui.QMessageBox.information(self, 'Connection info', conninfo)
        
        return closer
