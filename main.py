# Simple Qt5 App that takes an equation as input and plots it using matplotlib

import sys
from PyQt5 import QtWidgets

class EquationWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Qquation Window")

        self.show()


app = QtWidgets.QApplication(sys.argv)
starting_window = EquationWindow()