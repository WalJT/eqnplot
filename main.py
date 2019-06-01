# Simple Qt5 App that takes an equation as input and plots it using matplotlib

import sys
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt

class EquationWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.eqn_box = QtWidgets.QLineEdit() # Equation Entry Box
        self.eqn_start = QtWidgets.QLabel("y =")
        self.plot_butt = QtWidgets.QPushButton("Plot Equation") # Button to plot equation

        # Create Layout
        vertical_layout = QtWidgets.QVBoxLayout()
        horizontal_layout = QtWidgets.QHBoxLayout()

        horizontal_layout.addWidget(self.eqn_start)
        horizontal_layout.addWidget(self.eqn_box)

        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.plot_butt)

        self.setLayout(vertical_layout)
        self.setWindowTitle("Equation Window")

        self.plot_butt.clicked.connect(self.plot_equation)

        self.show()

    def plot_equation(self):
        eqn = self.eqn_box.text()
        print(eqn)


app = QtWidgets.QApplication(sys.argv)
starting_window = EquationWindow()
sys.exit(app.exec_())