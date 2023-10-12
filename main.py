from PyQt5 import QtWidgets, QtGui, QtCore

from DataParser import DataParser
from mainwindow import Ui_MainWindow
import sys





if __name__ == '__main__':
     app = QtWidgets.QApplication([])
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())

     parser = DataParser("2Ccircle1.txt")
     print("X:", parser.X)
     print("Y:", parser.Y)