from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

with ui.splitter() as splitter:
    # Two rows containg equation and linmits for X axis
    with splitter.before:
        with ui.column():
            with ui.row():
                ui.input(label="Enter an Equation: y =", placeholder="x**2")
            with ui.row():
                ui.input(label="Lower x limit:", placeholder="-10")
                ui.label("< x <")
                ui.input(label="Upper x limit:", placeholder="  10")

    # Pacehoder column with sample plot
    # Example taken from (https://nicegui.io/documentation/pyplot)
    with splitter.after:
        with ui.column():
            with ui.pyplot(figsize=(8, 5)):
                x = np.linspace(0.0, 5.0)
                y = np.cos(2 * np.pi * x) * np.exp(-x)
                plt.plot(x, y, '-')

# Run the app
ui.run(title="eqnPlot")