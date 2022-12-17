import dash
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

data = pd.DataFrame(
    {
        "item": [
            "Red square",
            "Red circle",
            "Blue square",
            "Blue circle",
            "Green square",
            "Green circle",
        ],
        "color": ["red", "red", "blue", "blue", "green", "green"],
        "shape": ["square", "circle", "square", "circle", "square", "circle"],
        "qty": [3, 2, 5, 3, 2, 6],
    }
)
items=[

                dbc.DropdownMenuItem("Red", id="Red"),
                dbc.DropdownMenuItem("Blue", id="Blue"),
                dbc.DropdownMenuItem("Green", id="Green"),
            ]
cosas=["Red is a good color","Pink is good for Flamingos","Green is for hippies"]
atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),cosas))
INP=list(map(lambda z: Input(z,"n_clicks"),cosas))
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.DropdownMenu(atems,
            label="Filter plot",
            className="mb-3",
            id= 'iddropdownmenu'  #create an id for the dropdown menu to be used in the graph callback to modify the label
        ),
         #dcc.Graph(id="graph"),
    ]
)


@app.callback(
    [
     Output("iddropdownmenu", "label")
      #,Output("graph", "figure")
     ],
      # using the id for the dropdown menu as an output to modify its label when callback is triggered
    INP,
)
def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "all"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id in ["red", "blue", "green"]:
        df = data.loc[data["color"] == button_id, :]
    elif button_id in ["square", "circle"]:
        df = data.loc[data["shape"] == button_id, :]
    else:
        df = data

    return [button_id]#go.Figure(data=[go.Pie(labels=df["item"], values=df["qty"])])

# the second output being returned above is the selected button_id (all, red, blue, green, etc...) which will be set as the label for the dropdownmenu


if __name__ == "__main__":
    app.run_server(debug=True)