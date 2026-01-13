import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(
    [
        html.P("Enter your name:"),
        dcc.Input(id="name-input", value="", type="text"),
        html.Div(id="output"),
    ]
)


# Define the callback function
@app.callback(Output("output", "children"), [Input("name-input", "value")])
def update_output(name):
    return f"Hello, {name}!"


# Run the app
if __name__ == "__main__":
    app.run_server()
