from PyQt4.uic import loadUiType
import sys
from PyQt4 import QtGui
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import  matplotlib.pyplot as plt
import GUI.dbinfo as db
from libs.get_data import get_conflicts, get_minyear, get_maxyear
from libs.get_coords import get_eclipse_coords
from SpinTest import plotmap
Ui_MainWindow, QMainWindow = loadUiType('GUI/mainframe.ui')



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        ######################### Get database info #########################
        self.engine = '' # engine variable stores database information
        self.wedit = db.DBInfo(self)
        self.wedit.exec_()
        
        super(Main, self).__init__()
        self.setupUi(self)
        
        # TODO: make queries for max year and min year
        self.slyear.setMaximum(get_maxyear(self.engine))
        self.slyear.setMinimum(get_minyear(self.engine))

        ######################### Initialize text for selected year #########################
        self.txtyear.setText(str(self.slyear.value()))

        ######################### Program events #########################
        self.slyear.valueChanged.connect(self.updTxt)
        self.slyear.sliderReleased.connect(self.updFig)
        self.txtyear.returnPressed.connect(self.updSl)
        self.actionDatabase_info.triggered.connect(self.edit)

        fig = plotmap()
        self.addmpl(fig)

    ######################### Edit textbox and slider #########################
    def updTxt(self):
        self.txtyear.setText(str(self.slyear.value()))
    def updSl(self):
        self.slyear.setValue(int(self.txtyear.text()))
        self.updFig()

    ######################### Update figure #########################
    def updFig(self):
        try:
            self.rmmpl()
        except:
            pass
        
        failed = False
        fig1 = get_conflicts(self.engine, int(self.txtyear.text()))
        self.addmpl(fig1)
        try:
            #fig1 = get_conflicts(self.engine, int(self.txtyear.text()))
            #self.addmpl(fig1)
            print('try')
        except:
            info = "Could not connect to database. Are you sure you're connected to one?"
            failed = True
            pass

        if failed:
            QtGui.QMessageBox.information(self, 'Error', info)
 
    def onpick(self, event):
        ind = event.ind
        artist = event.artist
        xdata = artist.get_xdata()
        ydata = artist.get_ydata()

        if ind[0] in range(len(xdata)):
            print('The coordinates are {}, {}'.format(xdata[ind[0]],ydata[ind[0]]))
        return ind[0]


        
    ######################### Create Database #########################
    def edit(self):
        self.wedit = db.DBInfo(self)
        self.wedit.show()

    ######################### Create figure #########################
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.canvas.mpl_connect('pick_event', self.onpick)
        self.mplvlayout.addWidget(self.canvas)
        self.canvas.draw()

    ######################### Remove figure #########################
    def rmmpl(self,):
        self.mplvlayout.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvlayout.removeWidget(self.toolbar)
        self.toolbar.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    
    main.show()
    sys.exit(app.exec_())

