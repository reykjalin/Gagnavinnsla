from PyQt4.uic import loadUiType
import sys
from PyQt4 import QtGui
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import GUI.dbinfo as db
Ui_MainWindow, QMainWindow = loadUiType('GUI/mainframe.ui')

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)

        self.slyear.setMaximum(2014)
        self.slyear.setMinimum(1950)

        self.txtyear.setText(str(self.slyear.value()))

        self.slyear.valueChanged.connect(self.updTxt)
        self.txtyear.editingFinished.connect(self.updSl)
        self.actionDatabase_info.triggered.connect(self.edit)

        self.engine = ''

    ######################### Edit textbox and slider #########################
    def updTxt(self):
        self.txtyear.setText(str(self.slyear.value()))
    def updSl(self):
        self.slyear.setValue(int(self.txtyear.text()))

    ######################### Create Database #########################
    def edit(self):
        self.wedit = db.DBInfo(self)
        self.wedit.show()

    ######################### Create figure #########################
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvlayout.addWidget(self.canvas)
        self.canvas.draw()

    ######################### Remove figure #########################
    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()

if __name__ == '__main__':
    import mapplot
    fig1 = mapplot.plottest()
 
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())
