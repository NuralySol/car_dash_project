# import the the necessary libraries for the Dash Project

from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd
# from page.layout import create_layout
from utils.util import get_data 


# Load the data from a data directory
PATH = "./data/Car_sales.csv"
data = get_data(PATH)

# Print the head to verify the data was loaded correctly
print(data.head())

# Initialize the main Dash app and apply Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.layout = create_layout(app, data)
app.layout = html.Div("Hello World")

if __name__ == "__main__":
    app.run_server(debug=True)
