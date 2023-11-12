from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

# Two rows containg equation and linmits for X axis
with ui.column():
    with ui.row():
        ui.label("Enter an Equation:")
        ui.input("Equation")
    with ui.row():
        ui.input("lower X")
        ui.label("< x <")
        ui.input("upper x")

ui.run(title="eqnPlot")