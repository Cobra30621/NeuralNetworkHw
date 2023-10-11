from PyQt5 import QtWidgets, QtGui, QtCore

from DataParser import DataParser
from mainwindow import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
     def __init__(self):
         super(MainWindow, self).__init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
         self.ui.label.setText('Hello World!')


if __name__ == '__main__':
     # app = QtWidgets.QApplication([])
     # window = MainWindow()
     # window.show()
     # sys.exit(app.exec_())

     parser = DataParser("2Ccircle1.txt")
     print("X:", parser.X)
     print("Y:", parser.Y)