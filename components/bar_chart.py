from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px


# Id's are unique to each component and idealy should be verbose and descriptive
# This is one component that will be used in the Dash app
# Decorator that changes the behavior of some other function (DRY) Do not repeat yourself
def render(app, data):
    # A decorator that wraps a function and changes its behavior need Output() and Input()
    # This is the id of the dropdown component "car-dropdown"
    @app.callback(Output("bar-chart", "children"), Input("car-dropdown", "value"))
    def update_bar_chart(dropdown):
        filtered_data = data[data["Manufacturer"] == dropdown]
        if filtered_data.shape[0] == 0:
            return html.Div("No data available for this selection", id="bar-chart")
        # Create a bar chart using Plotly Express
        fig = px.bar(
            filtered_data,
            x="Model",
            y="Sales_in_thousands",
            title=f"{dropdown} Sales by model",
            color="Model", # Color the bars by the model
            labels={"Sales_in_thousands": "Sales in Thousands", "Model": "Car Model"}, # Change the labels for the x and y axis for better readability and visualization
        )
        # Needs two return statements to return the graph and the id must be the same as it is one component
        # But this return returns the graph and the id of the component
        return html.Div(dcc.Graph(figure=fig), id="bar-chart")
    # This return only needs to return the id of the component that will be used in the layout.py
    return html.Div(id="bar-chart")
