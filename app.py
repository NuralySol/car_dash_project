# import the the necessary libraries for the Dash Project
from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

# Imports using the relative path and the necessary functions for the Dash app
from page.layout import create_layout
from utils.util import get_data


# Load the data from a data directory
PATH = "./data/Car_sales.csv"
data = get_data(PATH)

# Print the head to verify the data was loaded correctly loads 5 rows of the data
print(data.head())

# Initialize the main Dash app and apply Bootstrap theme (default theme)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = create_layout(app, data)

# Run the Dash app using __name__ as the main function, __name__ is a special variable in Python that is used to determine if the script is being run on its own or being imported
if __name__ == "__main__":
    app.run_server(debug=True)
