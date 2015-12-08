import sys
import qdarkstyle # For dark style. pip install qdarkstyle. requires PySide
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow
import psycopg2
import getpass
import pprint as pp

class MyDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Initialize window
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize search list (on left)
        self.lstSearch = self.ui.lstSearch
        self.modelSearch = QtGui.QStandardItemModel(self.lstSearch)
        
        # Initialize similar list (on right)
        self.lstSimilar = self.ui.lstSimilar
        self.modelSimilar = QtGui.QStandardItemModel(self.lstSimilar)
    
        # Define functions for buttons
        self.ui.btnDone.clicked.connect(self.close)
        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnRem.clicked.connect(self.rem)
        
        # KeyEvent filter to filter out when you press the return key
        self.ui.searchtext.installEventFilter(self)
                
    # Go into the database and get list
    def getdat(self,inputdata):
        host = 'localhost'
        dbname = 'gavi'

        #username = input('User name for {}.{}: '.format(host,dbname))
        username = 'jonkristinnhelgason'
        #pw = getpass.getpass()
        pw = ''

        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        #print("Connected!\n")

        s = ("""select name
        from drinkers
        where lower(name) like '{}%';""".format(inputdata))


        cursor.execute(s)

        #pp.pprint(cursor.fetchall())

        return cursor.fetchall()


    def search(self):
        #  
        self.modelSearch.clear()

        # Get text from textbox and clear it
        txt = self.ui.searchtext.toPlainText()
        self.ui.searchtext.clear()

        # Get data from sql database
        movielistoftuple = self.getdat(txt)
        
        for i in movielistoftuple:
            # Get each line of text
            txt = i[0]

            # Create item from text and add to list
            item = QtGui.QStandardItem(txt)

            #Add to the list
            self.modelSearch.appendRow(item)

        # Make sure list appears
        self.lstSearch.setModel(self.modelSearch)

    def add(self):
        # Get index for selected item
        index = self.lstSearch.selectedIndexes()[0]

        # Get item associated with selected index
        item = self.modelSearch.itemFromIndex(index)
        newitem = QtGui.QStandardItem(item.text())
        
        # Remove item from search list
        self.modelSearch.removeRow(index.row())
        self.lstSearch.setModel(self.modelSearch)
        
        # Move to similar list
        self.modelSimilar.appendRow(newitem)
        self.lstSimilar.setModel(self.modelSimilar)
        
    def rem(self):
        # Get index for selected item
        index = self.lstSimilar.selectedIndexes()[0]
        
        # Get item associated with selected index
        item = self.modelSimilar.itemFromIndex(index)
        newitem = QtGui.QStandardItem(item.text())
        
        # Remove item from similar list
        self.modelSimilar.removeRow(index.row())
        self.lstSimilar.setModel(self.modelSimilar)
        
        # Move to search list
        self.modelSearch.appendRow(newitem)
        self.lstSearch.setModel(self.modelSearch)
        
    def eventFilter(self, obj, event):
        # Call the search function if you press Return
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Return:
            self.search()
            return True
        # Default case, writes text to the textbox
        QtGui.QWidget.eventFilter(self, obj, event)
        return False

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    app.setStyleSheet(qdarkstyle.load_stylesheet()) # For dark theme
    myapp.show()
    sys.exit(app.exec_())

    # Close the sql connection
    cursor.close()
    conn.close()
