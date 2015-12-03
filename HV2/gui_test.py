import sys
from PyQt4 import QtCore, QtGui
from form import Ui_MainWindow

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
                

    def search(self):
        # Get text from textbox and clear it
        txt = self.ui.searchtext.toPlainText()
        self.ui.searchtext.clear()
        
        # Create item from text and add to list
        item = QtGui.QStandardItem(txt)
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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
