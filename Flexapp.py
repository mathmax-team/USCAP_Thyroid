# 1. Import Dash
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from sample_data import last_week_date, last_year_date, last_month_date,test_type, results_list, genotype_list
from datetime import date


################## MAKE DROPDOWN FROM LIST
def make_drop(lista,id):
    items=lista
    atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),items))
    inputs=list(map(lambda z: Input(z,"n_clicks"),items))

    menu=dbc.DropdownMenu(atems,
            label=lista[0],
            className="mb-3",
            id= id  #create an id for the dropdown menu to be used in the graph callback to modify the label
        ,color="success",
        size="sm"
        )
    return {"drop":menu,"inputs":inputs,"list":lista}


###################  GENERATE THE DROPDOWN ELEMENTS  #######################


dropletter=make_drop(['Last week', 'Last month', 'Last year'],"dropletter")
type=make_drop(test_type,"type")
weird=make_drop(results_list,"weird")
genotype=make_drop(genotype_list,"genotype")
mvp=make_drop(["A","B"],"mvp")

###################### PAGE HEADER    #######################


page_header=[
    dbc.Row(html.Div(style={"height":"10px"})),
    dbc.Row([
        dbc.Col(
            [dbc.Row(html.Img(src="assets/medicine.svg",style={'height': '60px'})),
            dbc.Row(html.H3('Cytopathology Monitor'),style={"textAlign":"center"})
            ],
            #width="3",
            align="end"),
        dbc.Col(dropletter["drop"]),
        dbc.Col(dcc.DatePickerRange(
                id = 'date-range',
                start_date_placeholder_text = last_month_date,
                end_date = date.today(),
                max_date_allowed = date.today(),
                #day_size=30,
                #style={"width":"10cm","height":"20cm","margin-top":"50px","margin-left":"20px"}
                    ),
                    width=4
                ),
        dbc.Col([
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
                    style={"height":"100px","width":"300px"}
                                ),
                    )
                                ],
                )
            ],
            id="page_header",
            justify="end",
            )
        ]
#############################     Imgrid   ###################################################
Imgrid=html.Div(children=[
                  #First GRAPH
                    html.Div(
                        dbc.Col([
                            dbc.Row(type["drop"],style={"textAlign":"center"}),
                            dbc.Row(
                            dcc.Graph(
                                id='types-graph',
                                figure={},
                                config={
                                    'staticPlot': False,     # True, False
                                    'scrollZoom': True,      # True, False
                                    'doubleClick': 'reset+autosize',  # 'reset', 'autosize' or 'reset+autosize', False
                                    'showTips': False,       # True, False
                                    'displayModeBar': False,  # True, False, 'hover'
                                    'watermark': False,
                                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                    },
                            style={"height":"300px"}
                            ),
                            )
                        ],
                        style={'padding':'5px'}
                        )),
                        #Second GRAPH
                        # html.Div(children=[
                        #     html.H2('Adequacy', style={'textAlign': 'center'}),

                        # ], style={'padding':'10px', 'border':None}),

                        #Third GRAPH
                        html.Div(
                            dbc.Col([
                                dbc.Row(weird["drop"],style={"textAlign":"center"}),
                                dbc.Row(
                                dcc.Graph(id='results-graph', figure={},
                                    config={
                                        'staticPlot': False,     # True, False
                                        'scrollZoom': False,      # True, False
                                        'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                        'showTips': False,       # True, False
                                        'displayModeBar': False,  # True, False, 'hover'
                                        'watermark': False,
                                        # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                            },
                                        style={"height":"300px"}
                                        )
                                )
                        ],
                        ),
                        style={'padding':'5px'}
                        ),
                        html.Div(dbc.Col(
                            [
                            dbc.Row(genotype["drop"],style={"textAlign":"center"}),
                            dbc.Row(
                                dcc.Graph(id='mvp-graph', figure={},
                                    config={
                                        'staticPlot': False,     # True, False
                                        'scrollZoom': False,      # True, False
                                        'doubleClick': 'reset+autosize',  # 'reset', 'autosize' or 'reset+autosize', False
                                        'showTips': False,       # True, False
                                        'displayModeBar': False,  # True, False, 'hover'
                                        'watermark': False,
                                        # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                            },
                                        style={"height":"300px"}
                                        ),
                            )
                            # dcc.Dropdown(genotype_list,
                            # value=genotype_list[0],
                            # id = 'selected-genotype'
                            # ),
                        ],
                        style={'padding':'5px', 'border':None}
                        ),
                        ),

                        #Fifth GRAPH
                        html.Div(dbc.Col([
                            dbc.Row(mvp["drop"],style={"textAlign":"center"}),
                            dbc.Row(
                                dcc.Graph(id='qc-graph', figure={},
                                config={
                                    'staticPlot': False,     # True, False
                                    'scrollZoom': False,      # True, False
                                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                    'showTips': False,       # True, False
                                    'displayModeBar': False,  # True, False, 'hover'
                                    'watermark': False,
                                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                    },
                                    style={"height":"300px"}
                                    ),
                            )
                        ],
                        style={'padding':'5px'}),
                        )
                        ],
                        #html.Div('6', style={'padding':'0px', 'border':None}),
                    id="grid",
                    style={'display': 'grid', 'gridTemplateRows':"repeat(2, 1fr)",'gridTemplateColumns': 'repeat(2, 1fr)', 'gridAutoFlow': 'row',"height":"100px"}
)


######################################

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=dbc.Container([dbc.Row(page_header),dbc.Row(Imgrid)],fluid="True")
############## UPDATE DROPDOWN


########################### CALL BACK letterdrop ###################
@app.callback(
    [
     Output("dropletter", "label")
     ],
    dropletter["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = dropletter["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
########################### CALL BACK type ###################
@app.callback(
    [
     Output("type", "label")
     ],
    type["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = type["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
################  CALL BACK weird #################

@app.callback(
    [
     Output("weird", "label")
     ],
    weird["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = weird["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]

########################## CALL BACK genotype ###################
@app.callback(
    [
     Output("genotype", "label")
     ],
    genotype["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = genotype["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
################  CALL BACK weird #################

@app.callback(
    [
     Output("mvp", "label")
     ],
    mvp["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = mvp["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]




if __name__ == "__main__":
    app.run_server(debug=True)