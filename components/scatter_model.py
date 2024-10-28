from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# This function will create a scatter plot for the selected model and compare it to other models
# The function will take in the Dash app and the data as arguments
# This is a nested function that will be used in the layout.py
def render(app, data):
    @app.callback(Output("scatter-plot-model", "children"), Input("car-dropdown", "value"))
    def update_scatter_plot(dropdown):
        # Highlight the selected model and include all other models for comparison in the scatter plot
        data['Selected'] = data['Manufacturer'] == dropdown
        fig = px.scatter(
            data,
            x="Sales_in_thousands",
            y="Model",
            title=f"{dropdown} Sales in Thousands vs Other Models",
            color="Selected",  # Highlights the selected model
            size="Sales_in_thousands",
            labels={"Model": "Model", "Sales_in_thousands": "Sales in Thousands"},
        )
        return html.Div(dcc.Graph(figure=fig), id="scatter-plot-model")
    
    return html.Div(id="scatter-plot-model")
