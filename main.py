# Simple Qt5 App that takes an equation as input and plots it using matplotlib

import sys
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from numpy import *

class EquationWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.eqn_box = QtWidgets.QLineEdit() # Equation Entry Box
        self.min_x_box = QtWidgets.QLineEdit()
        self.max_x_box = QtWidgets.QLineEdit()
        self.eqn_start = QtWidgets.QLabel("y =")
        self.plot_butt = QtWidgets.QPushButton("Plot Equation") # Button to plot equation
        self.x_range = QtWidgets.QLabel("< x <")

        # Create Layout
        vertical_layout = QtWidgets.QVBoxLayout()
        eqbox_layout = QtWidgets.QHBoxLayout()
        x_range_layout = QtWidgets.QHBoxLayout()


        eqbox_layout.addWidget(self.eqn_start)
        eqbox_layout.addWidget(self.eqn_box)

        x_range_layout.addWidget(self.min_x_box)
        x_range_layout.addWidget(self.x_range)
        x_range_layout.addWidget(self.max_x_box)

        vertical_layout.addLayout(eqbox_layout)
        vertical_layout.addLayout(x_range_layout)
        vertical_layout.addWidget(self.plot_butt)

        self.setLayout(vertical_layout)
        self.setWindowTitle("Equation Window")

        self.plot_butt.clicked.connect(self.plot_equation)

        self.show()

    def plot_equation(self):
        x = linspace(float(self.min_x_box.text()), float(self.max_x_box.text()), 300)
        eqn = self.eqn_box.text()
        y = eval(eqn)

        plt.plot(x, y)
        plt.title("y = " + eqn)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


app = QtWidgets.QApplication(sys.argv)
starting_window = EquationWindow()
sys.exit(app.exec_())