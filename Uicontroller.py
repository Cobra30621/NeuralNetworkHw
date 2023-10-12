import sys

from pyqt5_plugins.examplebutton import QtWidgets

from DataParser import DataParser
from Perceptron import Perceptron
from mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Uicontroller:
    def __int__(self):
        print("Uicontroller:")
        self.setUI()

    def setUI(self):
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        self.ui = window.ui
        self.ui.trainButton.clicked.connect(self.train)
        options = ['perceptron1.txt', 'perceptron2.txt', '2Ccircle1.txt', '2Circle1.txt', '2 Circle2.txt', '2CloseS.txt', '2CloseS2.txt', '2CloseS3.txt', '2cring.txt', '2CS.txt', '2Hcircle1.txt', '2ring.txt']
        self.ui.datasetComboBox.addItems(options )
        print("SetUI")
        sys.exit(app.exec_())

    def train(self):
        epoch = self.ui.epoch_spinBox.value()
        learning_rate = self.ui.learningRate_doubleSpinBox.value()
        dataSet = self.ui.datasetComboBox.currentText()

        self.parser = DataParser(dataSet)
        # print("X_train:", self.parser.X_train)
        # print("X_test:", self.parser.X_test)
        # print("Y_train:", self.parser.Y_train)
        # print("Y_test:", self.parser.Y_test)
        # print("Y_Set:", self.parser.Y_set)

        self.perceptron = Perceptron(learning_rate=learning_rate , epochs=epoch, y_set=self.parser.Y_set)
        self. perceptron.fit(self.parser.X_train, self.parser.Y_train)
        self.perceptron.evaluate_accuracy(self.parser.X_test, self.parser.Y_test)
        # Plot decision boundary
        self.showOutcome()


    def showOutcome(self):

        print("train_accuracy", self.perceptron.train_accuracy)
        print("test_accuracy", self.perceptron.test_accuracy)
        print("weights", self.perceptron.weights)

        self.ui.weight_label.setText(str(self.perceptron.weights))
        self.ui.trainAccuracy_label.setText(str(self.perceptron.train_accuracy))
        self.ui.testAccuracy_label.setText(str(self.perceptron.test_accuracy))

        self.perceptron.plot_accuracy()
        plot = self.ui.MplWidget.canvas.axes.plot
        print("plot", plot)
        self.perceptron.plot_decision_boundary(self.ui.MplWidget.canvas.axes, self.parser.X, self.parser.Y)


