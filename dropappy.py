# import dash
# import dash_bootstrap_components as dbc
# from dash import dcc
# import pandas as pd
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output

# data = pd.DataFrame(
#     {
#         "item": [
#             "Red square",
#             "Red circle",
#             "Blue square",
#             "Blue circle",
#             "Green square",
#             "Green circle",
#         ],
#         "color": ["red", "red", "blue", "blue", "green", "green"],
#         "shape": ["square", "circle", "square", "circle", "square", "circle"],
#         "qty": [3, 2, 5, 3, 2, 6],
#     }
# )
# items=[

#                 dbc.DropdownMenuItem("Red", id="Red"),
#                 dbc.DropdownMenuItem("Blue", id="Blue"),
#                 dbc.DropdownMenuItem("Green", id="Green"),
#             ]
# cosas=["Red is a good color","Pink is good for Flamingos","Green is for hippies"]
# atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),cosas))
# INP=list(map(lambda z: Input(z,"n_clicks"),cosas))
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = dbc.Container(
#     [
#         dbc.DropdownMenu(atems,
#             label="Filter plot",
#             className="mb-3",
#             id= 'iddropdownmenu'  #create an id for the dropdown menu to be used in the graph callback to modify the label
#         ),
#          #dcc.Graph(id="graph"),
#     ]
# )


# @app.callback(
#     [
#      Output("iddropdownmenu", "label")
#       #,Output("graph", "figure")
#      ],
#       # using the id for the dropdown menu as an output to modify its label when callback is triggered
#     INP,
# )
# def make_graph(*args):
#     ctx = dash.callback_context

#     if not ctx.triggered:
#         button_id = "all"
#     else:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

#     if button_id in ["red", "blue", "green"]:
#         df = data.loc[data["color"] == button_id, :]
#     elif button_id in ["square", "circle"]:
#         df = data.loc[data["shape"] == button_id, :]
#     else:
#         df = data

#     return [button_id]#go.Figure(data=[go.Pie(labels=df["item"], values=df["qty"])])

# # the second output being returned above is the selected button_id (all, red, blue, green, etc...) which will be set as the label for the dropdownmenu


# if __name__ == "__main__":
#     app.run_server(debug=True)
from datetime import date
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range')
])


@app.callback(
    Output('output-container-date-picker-range', 'children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    string_prefix = 'Camilo, You have selected: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


if __name__ == '__main__':
    app.run_server(debug=True)