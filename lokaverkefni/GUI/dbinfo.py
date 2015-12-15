from PyQt4.uic import loadUiType
import sys
from PyQt4 import QtGui
from libs.populate_sql import sql_create_database, sql_populate_database
from sqlalchemy import create_engine
Ui_dbDialog, QWidget = loadUiType('GUI/dbDialog.ui')

class DBInfo(QWidget, Ui_dbDialog):
    def __init__(self, parent):
        super(DBInfo, self).__init__()
        self.setupUi(self)

        self.host = 'localhost'
        self.usr = 'postgres'
        self.db = ''
        self.pw = ''
        self.parent = parent

        self.txtHost.insert(self.host)
        self.txtDb.insert(self.db)
        self.txtUser.insert(self.usr)
        self.txtPwd.insert(self.pw)
        
        self.btnOk.clicked.connect(self.saveinfo)
        self.btnpopulate.clicked.connect(self.createdb)

    def createdb(self):
        try:
            sql_create_database(self.txtUser.text(), self.txtPwd.text(), self.txtDb.text(), self.txtHost.text())
            self.parent.engine = sql_populate_database(self.txtUser.text(), self.txtPwd.text(), self.txtDb.text(), self.txtHost.text())
            info = 'Success! The database has been created'
        except:
            info = 'Something went wrong. Are you sure the information you entered is correct?'
        QtGui.QMessageBox.information(self, 'Database creation information', info)

        ######################### Save info from textboxes to use for connections #########################
    def saveinfo(self):
        self.host = self.txtHost.text()
        self.db = self.txtDb.text()
        self.usr = self.txtUser.text()
        self.pw = self.txtPwd.text()
        self.parent.engine = create_engine('postgresql+psycopg2://{}:{}@{}:5432/{}' .format(self.usr,self.pw,self.host,self.db))
        closer = self.test()
        
        if closer:
            self.close()

    ######################### Code for testing database connetion #########################
    def test(self):
        closer = False
        
        try:
            connection = self.parent.engine.connect()
            connection.close()
            conninfo = 'Success! You are now connected to your database'
            closer = True
        except:
            conninfo = 'Something went wrong. Are you sure the information you entered is correct?'
        
        QtGui.QMessageBox.information(self, 'Connection info', conninfo)
        
        return closer
