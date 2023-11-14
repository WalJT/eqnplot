from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

def plot_graph() -> None:
    with ui.column():
        with ui.pyplot(figsize=(8, 5)):
            x = np.linspace(0.0, 5.0)
            y = eval("x**2")
            plt.plot(x, y, 'k-',)

# Two rows containg equation and linmits for X axis
with ui.column():
    with ui.row():
        ui.input(label="Enter an Equation: y =", placeholder="x**2")
    with ui.row():
        ui.input(label="Lower x limit:", placeholder="-10")
        ui.label("< x <")
        ui.input(label="Upper x limit:", placeholder="  10")
    ui.button("Plot", on_click=plot_graph())


# Run the app
ui.run(title="eqnPlot")