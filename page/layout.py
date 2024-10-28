from dash import html, Dash
import dash_bootstrap_components as dbc

# Import the dropdown component from the components folder
from components import dropdown, bar_chart, scatter, scatter_model

# A function to create the layout for the Dash project
def create_layout(app, data):
    return dbc.Container(
        [
            # Background Image (semi-transparent)
            html.Div(
                html.Img(
                    src=app.get_asset_url("circuit-board.jpg"),
                    style={
                        "width": "100%",
                        "height": "100%",
                        "position": "absolute",
                        "top": "0",
                        "left": "0",
                        "opacity": "0.55",  # Semi-transparent
                        "z-index": "-1",  # Places the image behind the content
                    },
                )
            ),
            # Content Overlay
            dbc.Container(
                [
                    # Header Section
                    html.H1(
                        "Car Data Visualization Dashboard",
                        className="text-center mb-5",
                        style={
                            "color": "#007bff",  # Primary blue color
                            "font-size": "3rem",  # Increase font size
                            "font-weight": "bold",  # Bold font for emphasis
                            "text-shadow": "2px 2px 4px rgba(0, 0, 0, 0.2)",  # Adds a soft shadow for depth
                            "margin-top": "20px",  # Adds top margin for spacing
                            "padding": "10px",  # Adds padding for better readability
                            "background-color": "rgba(255, 255, 255, 0.8)",  # Semi-transparent background
                            "border-radius": "8px",  # Rounds the corners for a softer look
                        },
                    ),
                    
                    # Dropdown Section
                    html.Div(
                        [
                            html.H4(
                                "Select Car Model", 
                                className="text-center mb-3",
                                style={
                                    'color': '#343a40',  # Dark grey color
                                    'font-weight': 'bold',
                                    'text-decoration': 'underline'
                                }
                            ),
                            dropdown.render(app, data)
                        ],
                        className="mb-5 p-4 rounded",
                        style={
                            'background-color': 'rgba(240, 240, 240, 0.9)',  # Light grey background
                            'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.1)',  # Subtle shadow
                            'border': '1px solid #ddd'  # Light border
                        }
                    ),

                    # Visualization Section
                    dbc.Row(
                        [
                            # Bar Chart
                            dbc.Col(
                                [
                                    html.H5(
                                        "Bar Chart Analysis",
                                        className="text-center mb-3",
                                        style={
                                            'color': '#007bff',  # Primary color for emphasis
                                            'font-weight': 'bold'
                                        }
                                    ),
                                    bar_chart.render(app, data)
                                ],
                                lg=6,
                                className="p-3",
                                style={
                                    'background-color': 'rgba(255, 255, 255, 0.95)',  # White background
                                    'border-radius': '8px',  # Rounded corners
                                    'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.1)',  # Subtle shadow
                                    'border': '1px solid #ddd'
                                }
                            ),

                            # Scatter Plot
                            dbc.Col(
                                [
                                    html.H5(
                                        "Scatter Plot",
                                        className="text-center mb-3",
                                        style={
                                            'color': '#007bff',  # Primary color for consistency
                                            'font-weight': 'bold'
                                        }
                                    ),
                                    scatter.render(app, data)
                                ],
                                lg=6,
                                className="p-3",
                                style={
                                    'background-color': 'rgba(255, 255, 255, 0.95)',  # White background
                                    'border-radius': '8px',
                                    'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.1)',
                                    'border': '1px solid #ddd'
                                }
                            )
                        ],
                        className="mb-4"
                    ),

                    # Additional Scatter Plot for Model Comparison
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H5(
                                        "Model Comparison Scatter Plot",
                                        className="text-center mb-3",
                                        style={
                                            'color': '#007bff',
                                            'font-weight': 'bold'
                                        }
                                    ),
                                    scatter_model.render(app, data)
                                ],
                                lg=12,
                                className="p-3",
                                style={
                                    'background-color': 'rgba(255, 255, 255, 0.95)',
                                    'border-radius': '8px',
                                    'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.1)',
                                    'border': '1px solid #ddd'
                                }
                            )
                        ]
                    ),
                ],
                style={"position": "relative", "z-index": "1"}  # Ensures content overlays the background
            ),
        ],
        fluid=True,
        style={"max-width": "1200px", "margin": "auto", "position": "relative"}
    )