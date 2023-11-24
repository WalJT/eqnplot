from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np

def plot_graph() -> None:
    try:
        # https://nicegui.io/documentation/section_page_layout#clear_containers
        # ^^^ Need to implement that here to clear exiting plots
        with ui.pyplot(figsize=(8, 5)):
            x = np.linspace(float(lower_x_input.value), float(upper_x_input.value))
            y = eval(eqn_input.value)
            plt.plot(x, y, 'k-',)
    except:
        ui.notify("Error: Missing or invalid equation or parameters")

# Two rows containg equation and linmits for X axis
with ui.column():
    with ui.row():
        eqn_input = ui.input(label="Enter an Equation: y =",
                             placeholder="<an expression in terms of x>")
    with ui.row():
        lower_x_input = ui.input(label="Lower x limit:", placeholder="<a number>")
        ui.label("< x <")
        upper_x_input = ui.input(label="Upper x limit:", placeholder="<a number>")
    ui.button("Plot", on_click=plot_graph)

# Run the app
ui.run(title="eqnPlot")