# 1. Import Dash
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input

items=['Last week', 'Last month', 'Last year']
atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),items))

INP=list(map(lambda z: Input(z,"n_clicks"),items))

dropletter=dbc.DropdownMenu(atems,
            label="Time period",
            className="mb-3",
            id= 'iddropdownmenu'  #create an id for the dropdown menu to be used in the graph callback to modify the label
        ,color="warning"
        )


page_header=[dbc.Row(html.Div(style={"height":"10px"})),dbc.Row([
                    dbc.Col(
                    [dbc.Row(html.Img(src="assets/medicine.svg",style={'height': '60px'})),
                        dbc.Row(html.H4('CYTOPATHOLOGY MONITOR'),style={"textAlign":"center"})
                        ],
                    width="3",
                    align="end"),

                    ##Time and default ranges
                    dbc.Col(
                        #html.Label('Time period:',style={'font-size':"20px",'font-weight':"bold","display":"flex"}),
                        dropletter),
                    ###DatePicker
                    dbc.Col(
                    dcc.DatePickerRange(
                            id = 'date-range',
                            #start_date_placeholder_text = last_month_date,
                            #end_date = date.today(),
                            #max_date_allowed = date.today(),
                            #day_size=30,
                        #style={"width":"10cm","height":"20cm","margin-top":"50px","margin-left":"20px"}
                    ),width=4),
                    ##Title and Treegraph
                    dbc.Col([
                        #dbc.Row(html.H3('Type : ', style={'fontWeigth': 'bold','textAlign':'center','font-size':"20px"},id='type-selected')),
                        dbc.Row(dcc.Graph(
                                id='tree-map',
                                figure={},
                                clickData={},
                                config={
                                'staticPlot': False,     # True, False
                                'scrollZoom': True,      # True, False
                                'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                'showTips': True,       # True, False
                                'displayModeBar': None,  # True, False, 'hover'
                                'watermark': False,
                                # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                },
                                style={"height":"50px","width":"300px"}
                                    ),
                                    )
                                    ]
                                    )

                    ],
                    #style={"display":"flex","height":"30mm"},
                    id="grad",
                    #align="center",
                    justify="end",
                    className="pad-row"
                    )
                    ]

# 2. Create a Dash app instance
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=dbc.Container(page_header,fluid="True")

@app.callback(
    [
     Output("iddropdownmenu", "label")
     ],
    INP
)
def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "Time period"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
if __name__ == "__main__":
    app.run_server(debug=True)