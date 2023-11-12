from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

# Two rows containg equation and linmits for X axis
with ui.splitter() as splitter:
    with splitter.before:
        with ui.column():
            with ui.row():
                ui.label("Enter an Equation:")
                ui.input("Equation")
            with ui.row():
                ui.input("lower X")
                ui.label("< x <")
                ui.input("upper x")

        # Pacehoder column with sample plot
        # Example taken from (https://nicegui.io/documentation/pyplot)
    with splitter.after:
        with ui.column():
            with ui.pyplot(figsize=(3, 2)):
                x = np.linspace(0.0, 5.0)
                y = np.cos(2 * np.pi * x) * np.exp(-x)
                plt.plot(x, y, '-')
    

ui.run(title="eqnPlot")