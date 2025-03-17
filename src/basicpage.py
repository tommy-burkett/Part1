# Dash: The application class
# html: Various HTML components
# dcc: dash core components (things like buttons, figures, slider bars, etc.)
from dash import Dash, html, dcc

from src.analysis import get_data
from src.plots import plotly_scatter, go

def run_app() -> None:
    # Create the application
    app = Dash(__name__)

    # The title will appear in the browser tab
    app.title = "Hello World"

    # Create a layout
    create_layout(app)

    # This runs the app, only use debug=True when testing, it shows an additional menu on the webpage
    app.run(debug=True)
    return None

def make_figure() -> go.Figure:
    x, y = get_data(n=5000)
    fig = plotly_scatter(x, y)
    return fig

def create_layout(app: Dash) -> None:
    layout = html.Div(id='main-div',
                      children=[html.H1('welcome to my website'),   # This is a large header
                                html.Hr(),                          # This is a horizontal line
                                html.H2('here is a figure')         # This is a smaller header
                                ]
                      )
    app.layout = layout
    return None