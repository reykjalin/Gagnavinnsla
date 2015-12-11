import sys
import qdarkstyle # For dark style. pip install qdarkstyle. requires PySide
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow
from dbDialog import Ui_dbDialog
import psycopg2
import getpass
import pprint as pp

NROFMOVIES = 10

######################################## Dialog for database info code ########################################
class DBInfo(QtGui.QWidget):
    ######################### Initialize window #########################
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
        
    ######################### Save info from textboxes to use for connections #########################
    def saveinfo(self):
        self.parent.host = self.ui.txtHost.text()
        self.parent.db = self.ui.txtDb.text()
        self.parent.usr = self.ui.txtUser.text()
        self.parent.pw = self.ui.txtPwd.text()
        closer = self.test()
        if closer:
            self.close()

    ######################### Code for testing database connetion #########################
    def test(self):
        closer = False
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
            conninfo = 'Success! You are now connected to your database'
            closer = True
        except:
            conninfo = 'Something went wrong. Are you sure the information you entered is correct?'
        
        QtGui.QMessageBox.information(self, 'Connection info', conninfo)
        
        return closer


######################################## Main window code ########################################
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
        
        # Lists used to store ratings and years
        self.moviesselected = []
        self.movieyears = []
        self.movieratings = []
        self.tmpmovieyears = []
        self.tmpmovieratings = []

    ######################### Open dialog for editing database info #########################
    def edit(self):
        self.wedit = DBInfo(self)
        self.wedit.setStyleSheet(qdarkstyle.load_stylesheet()) # For dark theme
        self.wedit.show()
        
    ######################### Go into the database and get searched movies #########################
    def getdat(self,inputdata):
        ######################### Connect to database #########################
        try:
            conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.db, self.usr, self.pw)
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
        except:
            errorstr = 'You are not connected to a database, \n\n press CTRL + E to access database settings'
            QtGui.QMessageBox.information(self, 'Error', errorstr)

        ######################### Create sql command #########################
        s = """select title, year, rating
        from movies
        where lower(title) like %s or year like %s
        order by title;"""
        values = ('%' + inputdata.replace("'", "''").lower() + '%', '%' + inputdata.replace("'","''") + '%')

        ######################### Get movies from search #########################
        cursor.execute(s, values)
        retval = cursor.fetchall()
        cursor.close()
        conn.close()
        return retval
        

    def search(self):
        ######################### Clear listbox and tmpmovieyears #########################
        self.modelSearch.clear()
        self.tmpmovieyears.clear()
        self.tmpmovieratings.clear()

        ######################### Get text from textbox and clear it #########################
        txt = self.ui.searchtext.text()
        self.ui.searchtext.clear()

        ######################### Get data from sql database #########################
        movielistoftuple = self.getdat(txt)
        
        ######################### Add items to list #########################
        for i in movielistoftuple:
            # Get each line of text
            self.tmpmovieyears.append(i[1])
            self.tmpmovieratings.append(i[2])
            txt = i[0]

            # Create item from text and add to list
            item = QtGui.QStandardItem(txt)
            item.setEditable(False)

            #Add to the list
            self.modelSearch.appendRow(item)

        ######################### Make sure list appears #########################
        self.lstSearch.setModel(self.modelSearch)

    def add(self):
        ######################### Get index for selected item #########################
        index = self.lstSearch.selectedIndexes()[0]
 
        ######################### Get item associated with selected index #########################
        item = self.modelSearch.itemFromIndex(index)
        newitem = QtGui.QStandardItem(item.text())
        newitem.setEditable(False)

        ######################### Add item to list #########################
        if newitem.text() not in self.moviesselected or self.tmpmovieyears[index.row()] not in self.movieyears:
            # Add to the list of values selected
            test = self.moviesselected.append(newitem.text())
            self.movieyears.append(self.tmpmovieyears[index.row()])
            self.movieratings.append(self.tmpmovieratings[index.row()])
            self.tmpmovieyears.pop(index.row())
            self.tmpmovieratings.pop(index.row())
            
            # Move to similar list
            self.modelSimilar.appendRow(newitem)
            self.lstSimilar.setModel(self.modelSimilar)

        ######################### Remove item from search list #########################
        self.modelSearch.removeRow(index.row())
        self.lstSearch.setModel(self.modelSearch)
        
    def rem(self):
        ######################### Get index for selected item #########################
        index = self.lstSimilar.selectedIndexes()[0]
        
        ######################### Get item associated with selected index #########################
        item = self.modelSimilar.itemFromIndex(index)
        newitem = QtGui.QStandardItem(item.text())
        newitem.setEditable(False)
        
        ######################### Remove from the list of values selected #########################
        test = self.moviesselected.remove(item.text())

        ######################### Remove item from similar list #########################
        self.modelSimilar.removeRow(index.row())
        self.lstSimilar.setModel(self.modelSimilar)
        self.tmpmovieyears.append(self.movieyears[index.row()])
        self.tmpmovieratings.append(self.movieratings[index.row()])
        self.movieyears.pop(index.row())
        self.movieratings.pop(index.row())

        ######################### Move to search list #########################
        self.modelSearch.appendRow(newitem)
        self.lstSearch.setModel(self.modelSearch)
        
    def popupwindow(self):
        ######################### Connect to db #########################
        
        conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.db, self.usr, self.pw)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        ######################### Create sql command to get genres #########################
        sqlcmd = """select distinct lower(g.genre)
        from genres g, movies m
        where m.id = g.movieid
        and ("""
        for i in range(len(self.moviesselected) - 1):
            sqlcmd += "lower(m.title) = '" + self.moviesselected[i].replace("'","''").lower() + "' and m.year = '" + self.movieyears[i] + "' or "
        sqlcmd += "lower(m.title) = '" + self.moviesselected[len(self.moviesselected) - 1].replace("'","''").lower() + "' and m.year = '" + self.movieyears[len(self.moviesselected) - 1] + "') order by lower(g.genre);"

        ######################### Get genres #########################
        cursor.execute(sqlcmd)
        genres = cursor.fetchall()        

        ######################### Create sql command to get tags #########################
        sqlcmd = """select distinct lower(mt.tag)
        from genres g, movies m, mtags mt
        where m.id = g.movieid and m.id = mt.movieid
        and ("""
        for i in range(len(self.moviesselected) - 1):
            sqlcmd += "lower(m.title) = '" + self.moviesselected[i].replace("'","''").lower() + "' and m.year = '" + self.movieyears[i] + "' or "
        sqlcmd += "lower(m.title) = '" + self.moviesselected[len(self.moviesselected) - 1].replace("'","''").lower() + "' and m.year = '" + self.movieyears[len(self.moviesselected) - 1] + "') order by lower(mt.tag);"
        
        ######################### Get tags #########################
        cursor.execute(sqlcmd)
        tags = cursor.fetchall()

        ######################### Get lowest rating from chosen movies #########################
        avgminfive = sum(self.movieratings) / len(self.movieratings) - 0.5

        ######################### Create sql command to get similar movies #########################
        sqlcmd = """select m.title, m.year
        from genres g, movies m, mtags mt
        where m.id = g.movieid and m.id = mt.movieid
        and m.rating >= """  + str(avgminfive) + """
        and ("""
        if len(genres) > 0:
            for i in range(len(genres) - 1):
                sqlcmd += "lower(g.genre) = '" + genres[i][0].replace("'","''") + "' or "
            sqlcmd += "lower(g.genre) = '" + genres[len(genres) - 1][0].replace("'","''") + "')\nand ("

        if len(tags) > 0:
            for i in range(len(tags) - 1):
                sqlcmd += "lower(mt.tag) = '" + tags[i][0].replace("'","''") + "' or "
            sqlcmd += "lower(mt.tag) = '" + tags[len(tags) - 1][0].replace("'","''") + "')\nand ("

        if len(self.moviesselected) > 0:
            for i in range(len(self.moviesselected) - 1):
                sqlcmd += "lower(m.title) != '" + self.moviesselected[i].replace("'","''").lower() + "' and m.year != '" + self.movieyears[i] + "' and "
            sqlcmd += "lower(m.title) != '" + self.moviesselected[len(self.moviesselected) - 1].replace("'","''").lower() + "' and m.year != '" + self.movieyears[len(self.moviesselected) - 1] + "') group by m.title, m.year order by count(m.title) desc limit {}".format(NROFMOVIES)

        ######################### Sort similar movies according to rating #########################
        sqlcmd = """select m.title, m.year, m.rating
        from movies m
        where (m.title, m.year) in (""" + sqlcmd + """) order by m.rating desc;"""


        ######################### Get similar movies #########################
        cursor.execute(sqlcmd)
        similar = cursor.fetchall()

        
        ######################### Show movies in messagebox #########################
        moviestr = 'Movies you might like:\n\n'
        for i in range(len(similar)):
            moviestr += similar[i][0] + '  (' + similar[i][1] + ')\n'
        moviestr += '\nWould you like to try again?'


        # The QWidget widget is the base class of all user interface objects in PyQt4.
        w = QtGui.QWidget()

        ######################### Show a message box #########################
        result = QtGui.QMessageBox.question(w, "Movies you might like", moviestr, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        # Close application if user chooses no
        if result != QtGui.QMessageBox.Yes:
            self.close()

        cursor.close()
        conn.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    app.setStyleSheet(qdarkstyle.load_stylesheet()) # For dark theme
    myapp.show()
    sys.exit(app.exec_())
