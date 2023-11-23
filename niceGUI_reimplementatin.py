from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

def plot_graph() -> None:
    with ui.column():
        with ui.pyplot(figsize=(8, 5)):
            x = np.linspace(float(lower_x_input.value), float(upper_x_input.value))
            y = eval(eqn_input.value)
            plt.plot(x, y, 'k-',)

# Two rows containg equation and linmits for X axis
with ui.column():
    with ui.row():
        eqn_input = ui.input(label="Enter an Equation: y =", placeholder="x**2")
    with ui.row():
        lower_x_input = ui.input(label="Lower x limit:", placeholder="-10")
        ui.label("< x <")
        upper_x_input = ui.input(label="Upper x limit:", placeholder="  10")
    ui.button("Plot", on_click=plot_graph)

# Run the app
ui.run(title="eqnPlot")