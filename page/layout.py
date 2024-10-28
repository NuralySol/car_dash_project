import dash_bootstrap_components as dbc
# Import the dropdown component from the components folder 
from components import dropdown, bar_chart, scatter, scatter_model

# A function to create the layout for the Dash project
def create_layout(app, data):
    return dbc.Container([
        dropdown.render(app, data),
        bar_chart.render(app, data),
        scatter.render(app, data),
        scatter_model.render(app, data)
    ])