from PyQt5 import QtWidgets, QtGui, QtCore

from DataParser import DataParser
from Uicontroller import Uicontroller
from mainwindow import Ui_MainWindow
import sys

if __name__ == '__main__':
    ui = Uicontroller()
    ui.setUI()
