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
from libs.get_data import get_conflicts, get_minyear, get_maxyear, get_conflist, get_exportlist, get_confinfo, get_eclipseinfo, makethevideo, plot_all
from libs.SpinTest import plotmap
from libs.get_coords import get_locs_db
Ui_MainWindow, QMainWindow = loadUiType('GUI/mainframe.ui')



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        ######################### Get database info #########################
        self.engine = '' # engine variable stores database information
        self.wedit = db.DBInfo(self)
        self.wedit.exec_()
        self.plot2D = True
        self.Echeck = True
        self.Eplot = True
        self.Ccheck = True
        self.Cplot = True
        self.plotall = False
        
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
        self.btnglobe.clicked.connect(self.globebutton)
        self.chkconflicts.stateChanged.connect(self.conflictCheck)
        self.chkeclipses.stateChanged.connect(self.eclipseCheck)
        self.actionGenerate_Globe.triggered.connect(self.globemovie)
        self.actionPlot_all.triggered.connect(self.plot_all_datapoints)

        fig = plotmap()
        self.addmpl(fig)

        self.chkconflicts.toggle()
        self.chkeclipses.toggle()

    def plot_all_datapoints(self):
        self.plotall = True
        self.updFig()

    def globebutton(self):
        if self.plot2D:
            self.plot2D = False
            self.btnglobe.setText('Map view')
            self.updFig()

        else:
            self.plot2D = True
            self.btnglobe.setText('Globe view')
            self.updFig()


    def conflictCheck(self):
        if self.Ccheck:
            self.Cplot = True
            self.Ccheck = False
            self.updFig()
        else:
            self.Cplot = False
            self.Ccheck = True
            self.updFig()

    def eclipseCheck(self):
        if self.Echeck:
            self.Eplot = True
            self.Echeck = False
            self.updFig()
        else:
            self.Eplot = False
            self.Echeck = True
            self.updFig()

    ######################### Edit textbox and slider #########################
    def updTxt(self):
        self.plotall = False
        self.txtyear.setText(str(self.slyear.value()))
    def updSl(self):
        self.plotall = False
        self.slyear.setValue(int(self.txtyear.text()))
        self.updFig()

    ######################### Update figure #########################
    def updFig(self):
        try:
            self.rmmpl()
        except:
            pass
        
        failed = False
        try:
            fig1 = get_conflicts(self.engine, int(self.txtyear.text()),self.Eplot ,self.Cplot ,self.plot2D,self.plotall)
            self.addmpl(fig1)
        except Exception as e:
            print(e)
            info = "Could not connect to database. Are you sure you're connected to one?"
            failed = True
            pass

        if failed:
            QtGui.QMessageBox.information(self, 'Error', info)
        else:
            self.updConflist()
            self.updExplist()

    def onpick(self, event):
        ind = event.ind
        artist = event.artist
        xdata = artist.get_xdata()
        ydata = artist.get_ydata()

        if ind[0] in range(len(xdata)):
            self.updTxtinfo(ind, artist)
        return ind[0]

    def updTxtinfo(self, ind, artist):
        lat = artist.get_ydata()[ind[0]]
        lon = artist.get_xdata()[ind[0]]
        year = int(self.txtyear.text())
        conflict = True
        try:
            self.txtconfinfo.setText(get_confinfo(self.engine, lat, lon, year))
        except:
            conflict = False
        if not conflict:
            try:
                self.txteclipse.setText(get_eclipseinfo(self.engine, lat, lon, year))
            except:
                pass

    def globemovie(self):
        makethevideo(self.engine,int(self.txtyear.text()), self.Eplot,self.Cplot,self.plotall)

    def updConflist(self):
        self.txtconflist.setText(get_conflist(self.engine, int(self.txtyear.text())))
    def updExplist(self):
        self.txtexport.setText(get_exportlist(self.engine, int(self.txtyear.text())))
        
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

