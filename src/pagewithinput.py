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

# @callback(
#         Output(component_id='my-figure',
#                component_property='figure',
#         Input(component_id='my-input',
#               component_property='value'
#               )
# )
# )

def make_figure(freq: float=1) -> go.Figure:
    x, y = get_data(n=5000, freq=float(freq))
    fig = plotly_scatter(x, y)
    return fig

def create_layout(app: Dash) -> None:
    layout = html.Div(id='main-div',
                      children=[html.H1('welcome to my website'),   # This is a large header
                                html.Hr(),                          # This is a horizontal line
                                html.H2('here is a figure'),        # This is a smaller header
                                dcc.Input(id='my-input',
                                          type='test',
                                          value=1
                                ),
                                dcc.Graph(id='my-figure',
                                          figure=make_figure())                         
                                ]
                      )
    app.layout = layout
    return None