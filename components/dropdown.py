from dash import html, dcc


# A function to create a dropdown component for the Dash project
# This function will take in the Dash app and the data as arguments
def render(app, data):
    all_cars = data["Manufacturer"].unique()
    car_makes = [{"label": car, "value": car} for car in all_cars]
    return html.Div(
        [
            dcc.Dropdown(
                options=car_makes, 
                value="Acura",
                multi=False,
                id="car-dropdown",
            )
        ]
    )
