from PyQt4.uic import loadUiType
import sys
from PyQt4 import QtGui
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
Ui_MainWindow, QMainWindow = loadUiType('GUI/mainframe.ui')

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)

        self.slyear.setMaximum(2014)
        self.slyear.setMinimum(1950)

        self.txtyear.setText(str(self.slyear.value()))

        self.slyear.valueChanged.connect(self.ud)
        self.txtyear.editingFinished.connect(self.ud2)

    def ud(self):
        self.txtyear.setText(str(self.slyear.value()))
    def ud2(self):
        self.slyear.setValue(int(self.txtyear.text()))

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
