from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# A function to create a scatter plot component for the Dash project
# This function will take in the Dash app and the data as arguments
# This is a nested function that will be used in the layout.py
def render(app, data):
    @app.callback(Output("scatter-plot", "children"), Input("car-dropdown", "value"))
    # Nested function that will be used to update the scatter plot
    def update_scatter_plot(dropdown):
        filtered_data = data[data["Manufacturer"] == dropdown]
        # If the data is empty return a message to the user
        if filtered_data.shape[0] == 0:
            return html.Div("No data available for this selection", id="scatter-plot")
        # price is multiplied by 10 to make the size of the bubbles more visible
        # use the for loop to iterate over the price and multiply each value by 10
        price = filtered_data["Price_in_thousands"].tolist()
        s = [i *10 for i in price]
        fig = px.scatter(
            filtered_data,
            x = "Price_in_thousands",
            y = "Sales_in_thousands",
            title = f"{dropdown} Price vs Sales in Thousands",
            color = "Model", # Dynamic symbols and colors for each model
            size = s, # Dynamic size for each model
            labels = {"Price_in_thousands": "Price in Thousands", "Sales_in_thousands": "Sales in Thousands"},
        )
        # As alwats the return statement needs to return the graph and the id of the component
        return html.Div(dcc.Graph(figure=fig), id="scatter-plot")
    # This return only needs to return the id of the component that will be used in the layout.py
    return html.Div(id="scatter-plot")