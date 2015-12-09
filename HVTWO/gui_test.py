import sys
import qdarkstyle # For dark style. pip install qdarkstyle. requires PySide
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow
from dbDialog import Ui_dbDialog
import psycopg2
import getpass
import pprint as pp


class DBInfo(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_dbDialog()
        self.ui.setupUi(self)

        self.parent = parent
        self.ui.txtHost.insert(parent.host)
        self.ui.txtDb.insert(parent.db)
        self.ui.txtUser.insert(parent.usr)
        self.ui.txtPwd.insert(parent.pw)
        
        self.ui.btnOk.clicked.connect(self.saveinfo)
        self.ui.btnTest.clicked.connect(self.test)

    def saveinfo(self):
        self.parent.host = self.ui.txtHost.text()
        self.parent.db = self.ui.txtDb.text()
        self.parent.usr = self.ui.txtUser.text()
        self.parent.pw = self.ui.txtPwd.text()
        self.close()
    def test(self):
        self.parent.host = self.ui.txtHost.text()
        self.parent.db = self.ui.txtDb.text()
        self.parent.usr = self.ui.txtUser.text()
        self.parent.pw = self.ui.txtPwd.text()
        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.parent.host, self.parent.db, self.parent.usr, self.parent.pw)
        conninfo = str()
        
        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.close()
            conn.close()
            conninfo = 'Success! You can now connect to your database'
        except:
            conninfo = 'Something went wrong. Are you sure the information you entered is correct?'
        
        QtGui.QMessageBox.information(self, 'Connection info', conninfo)
        

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
        self.ui.btnDone.clicked.connect(self.popupwindow)
        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnRem.clicked.connect(self.rem)
        self.ui.actionEdit_info.triggered.connect(self.edit)
        
        # Defualt db info
        self.host = 'localhost'
        self.db = ''
        self.usr = 'postgres'
        self.pw = ''
        
        self.moviesselected = list()


    def edit(self):
        self.wedit = DBInfo(self)
        self.wedit.setStyleSheet(qdarkstyle.load_stylesheet()) # For dark theme
        self.wedit.show()
        
    # Go into the database and get list
    def getdat(self,inputdata):
        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.db, self.usr, self.pw)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        #print("Connected!\n")

        s = ("""select title, year
        from movies
        where lower(title) like '%{}%' or year like'%{}%'
        order by title;""".format(inputdata.lower(),inputdata))


        cursor.execute(s)

        #pp.pprint(cursor.fetchall())

        return cursor.fetchall()


    def search(self):
        # Clear listbox
        self.modelSearch.clear()

        # Get text from textbox and clear it
        txt = self.ui.searchtext.text()
        self.ui.searchtext.clear()

        # Get data from sql database
        movielistoftuple = self.getdat(txt)
        
        for i in movielistoftuple:
            # Get each line of text
            txt = i[0]# + ' ({})'.format(i[1])

            # Create item from text and add to list
            item = QtGui.QStandardItem(txt)
            item.setEditable(False)

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
        newitem.setEditable(False)

        if newitem.text() not in self.moviesselected:
            # Add to the list of values selected
            test = self.moviesselected.append(newitem.text())
            #print(test)
            
            # Move to similar list
            self.modelSimilar.appendRow(newitem)
            self.lstSimilar.setModel(self.modelSimilar)

        # Remove item from search list
        self.modelSearch.removeRow(index.row())
        self.lstSearch.setModel(self.modelSearch)
        
    def rem(self):
        # Get index for selected item
        index = self.lstSimilar.selectedIndexes()[0]
        
        # Get item associated with selected index
        item = self.modelSimilar.itemFromIndex(index)
        newitem = QtGui.QStandardItem(item.text())
        newitem.setEditable(False)
        
        # Remove from the list of values selected
        test = self.moviesselected.remove(item.text())

        # Remove item from similar list
        self.modelSimilar.removeRow(index.row())
        self.lstSimilar.setModel(self.modelSimilar)
        
        # Move to search list
        self.modelSearch.appendRow(newitem)
        self.lstSearch.setModel(self.modelSearch)
        
    def popupwindow(self):
        # Connect to db
        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.db, self.usr, self.pw)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        # Create sql command to get genres
        sqlcmd = """select distinct lower(g.genre)
        from genres g, movies m
        where m.id = g.movieid
        and ("""
        for i in range(len(self.moviesselected) - 2):
            sqlcmd += "lower(m.title) = '" + self.moviesselected[i].replace("'","''").lower() + "' or "
        sqlcmd += "lower(m.title) = '" + self.moviesselected[len(self.moviesselected) - 1].replace("'","''").lower() + "') order by lower(g.genre);"

        # Get genres
        cursor.execute(sqlcmd)
        genres = cursor.fetchall()        

        # Create sql command to get tags
        sqlcmd = """select distinct lower(mt.tag)
        from genres g, movies m, mtags mt
        where m.id = g.movieid and m.id = mt.movieid
        and ("""
        for i in range(len(self.moviesselected) - 2):
            sqlcmd += "lower(m.title) = '" + self.moviesselected[i].replace("'","''").lower() + "' or "
        sqlcmd += "lower(m.title) = '" + self.moviesselected[len(self.moviesselected) - 1].replace("'","''").lower() + "') order by lower(mt.tag);"
        
        # Get tags
        cursor.execute(sqlcmd)
        tags = cursor.fetchall()


        # Get similar movies
        sqlcmd = """select m.title, count(m.title)
        from genres g, movies m, mtags mt
        where m.id = g.movieid and m.id = mt.movieid
        and ("""
        for i in range(len(genres) - 2):
            sqlcmd += "lower(g.genre) = '" + genres[i][0].replace("'","''") + "' or "
        sqlcmd += "lower(g.genre) = '" + genres[len(genres) - 1][0].replace("'","''") + "')\nand ("

        for i in range(len(tags) - 2):
            sqlcmd += "lower(mt.tag) = '" + tags[i][0].replace("'","''") + "' or "
        sqlcmd += "lower(mt.tag) = '" + tags[i][0].replace("'","''") + "') group by m.title order by count(m.title) desc limit {};".format(5)

        # Get similar movies
        cursor.execute(sqlcmd)
        similar = cursor.fetchall()
        
        # Show movies in messagebox
        moviestr = 'Movies you might like:\n\n'
        for i in range(len(similar)):
            moviestr += similar[i][0] + '\n'
        moviestr += '\nWould you like to try again?'

        # The QWidget widget is the base class of all user interface objects in PyQt4.
        w = QtGui.QWidget()

        # Show a message box
        result = QtGui.QMessageBox.question(w, "Movies you might like", moviestr, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if result != QtGui.QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    app.setStyleSheet(qdarkstyle.load_stylesheet()) # For dark theme
    myapp.show()
    sys.exit(app.exec_())

    # Close the sql connection
    cursor.close()
    conn.close()
