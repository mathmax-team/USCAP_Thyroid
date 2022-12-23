# 1. Import Dash
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from sample_data import sensitivity_list,choices,last_week_date, last_year_date, last_month_date,test_type, results_list, genotype_list
from datetime import date
from be.controllers.types_graph import types_graph
from be.controllers.filtering_tools import filter_dataframe,make_property_df,new_row_by_column
from be.controllers.tree_map_graph import tree_map_graph
from be.controllers.results_graph import result_graph
from be.controllers.mvp_graph import mvp_graph
from be.controllers.qc_graph import qc_graph
from be.controllers.scatter_plot import scatter_graph
from be.controllers.adequacy_bar_graph import make_adequacy_graph
from be.controllers.sensitivity_graph import sensitivity_scatter_graph
#from be.controllers.
import pandas as pd
##################  DATA #####################
frequency_df=pd.read_csv("frequency.csv")
frequency_df["day"]=pd.to_datetime(frequency_df["day"])

data_df=pd.read_csv("lab_data.csv")
data_df["day"]=pd.to_datetime(data_df["day"])

# Data={"All types":data_df}
# for tipo in ["Conventional","Liquid based"]:
#     Data[tipo]=data_df[data_df["type"]==tipo]

# test_df = pd.read_csv('test_dataframe_T.csv')
# test_df["day"]=pd.to_datetime(test_df["day"])
# initial_df = pd.read_csv('test_type_count_T.csv')
# initial_df["day"]=pd.to_datetime(initial_df["day"])

################## MAKE DROPDOWN FROM LIST
def make_drop(lista,id):
    color="success"
    size="sm"
    if lista[0][:4]=="Last":
        color="warning"
        size="lg"
    #items=lista
    atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),lista))
    inputs=list(map(lambda z: Input(z,"n_clicks"),lista))

    menu=dbc.DropdownMenu(atems,
            #label="Camilo",
            className="mb-3",
            id= id  #create an id for the dropdown menu to be used in the graph callback to modify the label
        ,color=color,
        size=size
        )
    return {"drop":menu,"inputs":inputs,"list":lista}


###################  GENERATE THE DROPDOWN ELEMENTS  #######################


dropletter=make_drop(['Last year', 'Last month', 'Last week'],"dropletter")
type=make_drop(test_type+["All test types"],"type")
weird=make_drop(results_list+["All results"],"weird")###### it starts at 1 to rule out the "All results" option
genotype=make_drop(genotype_list+["All genotypes"],"genotype")
mvp=make_drop(sensitivity_list,"mvp")
###################### table
table_header = [
    html.Thead(html.Tr([html.Th("Number of tests"), html.Th("Daily average")]))
]

row1 = html.Tr([html.Td("Arthur",id="tests"), html.Td("Dent",id="average")])


table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body, bordered=True,style={"width":"300px","height":"30px"})
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
                    width=3
                ),
                dbc.Col(table),
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
                    #style={"height":"150px","width":"300px"}
                                ),
                    ),

                    # dbc.Row([html.Div(html.H4(children="count_tests",id="count_tests"),style={"margin-top":"5px"})]),
                    # dbc.Row([html.Div(html.H4(children="Average:45",id="avg",style={"margin-top":"-12px"}))],
                    # style={"margin-top":"0px"},
                    # ),


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
                            style={"padding":"0px"},
                            )
                        ],
                        style={'padding':'5px'}
                        )
                        ),
                        #Second GRAPH
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
                                        ),
                                style={"padding":"0px"}
                                )
                        ],
                        ),
                        style={'padding':'5px'}
                        ),
                        #THIRD GRAPH
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
                            style={"padding":"0px"}
                            )
                        ],
                        style={'padding':'5px'}
                        ),
                        ),
                        #FOURTH GRAPH
                        html.Div(dbc.Col([
                            dbc.Row(mvp["drop"],style={"textAlign":"center"},),#
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
                                    style={"height":"300px"},
                                    ),
                                    style={"padding":"0px"}
                            )
                        ],
                        style={'padding':'5px'},
                        ),
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

##################################
@app.callback(
    Output(component_id= 'date-range', component_property='start_date'),
    Output(component_id= 'date-range', component_property='end_date'),
    Input(component_id='dropletter', component_property='label')
)
def update_time_range(input_range):
    """Control time range selection."""
    if input_range == 'Last week':
        start_date = last_week_date
    elif input_range == 'Last month':
        start_date =last_month_date
    elif input_range == 'Last year':
        start_date = last_year_date
    end_date = date.today()
    return start_date, end_date

#####################################################
# @app.callback(
#     #Output(component_id='type-selected', component_property='children'),
#     #Output(component_id='adequacy-selected', component_property='children'),
#     # Output(component_id='result-selected', component_property='children'),
#     # Output(component_id='genotype-selected', component_property='children'),

#     Output(component_id='types-graph', component_property='figure'),
#     Output(component_id='tree-map', component_property='figure'),
#     Output(component_id='results-graph', component_property='figure'),
#     Output(component_id='mvp-graph', component_property='figure'),
#     Output(component_id='qc-graph', component_property='figure'),
#     Input(component_id = 'type-dropdown', component_property='value'),
#     Input(component_id='tree-map', component_property='clickData'),
#     Input(component_id='selected-result', component_property='value'),
#     Input(component_id='genotype-radio', component_property='value'),

#     # Input(component_id='default-time-range', component_property='start_date'),

#     Input(component_id='default-time-ranges', component_property='value')
# )
#####################################################
@app.callback(
    #Output(component_id='type-selected', component_property='children'),
    #Output(component_id='adequacy-selected', component_property='children'),
    # Output(component_id='result-selected', component_property='children'),
    # Output(component_id='genotype-selected', component_property='children'),

    Output(component_id='types-graph', component_property='figure'),
    Output(component_id='tree-map', component_property='figure'),
    Output(component_id='results-graph', component_property='figure'),
    Output(component_id='mvp-graph', component_property='figure'),
    Output(component_id='qc-graph', component_property='figure'),
    Output(component_id='tests', component_property='children'),
    Output(component_id='average', component_property='children'),

    Input(component_id= 'date-range', component_property='start_date'),
    Input(component_id= 'date-range', component_property='end_date'),
    #Input(component_id = 'dropletter', component_property='label'),
    Input(component_id='type', component_property='label'),
    Input(component_id='weird', component_property='label'),
    Input(component_id='genotype', component_property='label'),
    Input(component_id='mvp', component_property='label'),

    #Input(component_id='default-time-range', component_property='start_date'),

   # Input(component_id='default-time-ranges', component_property='value')
)
def update_graphs(start_date,end_date,tipo,result_label,genotype_label,sensitivity_label):

    # """Return all graphs based on interactive filters."""
    # if input_range == 'Last week':
    #     start_date = last_year_date
    # elif input_range == 'Last month':
    #     start_date =last_month_date
    # elif input_range == 'Last year':
    #     start_date = last_year_date
    # end_date = date.today()
    ####Filter by dates
    #temp_df=Data[tipo]


    if tipo[:3]=="All":
        tipo="All"
    if genotype_label[:3]=="All":
        genotype_label="All"
    if result_label[:3]=="All":
        result_label="All"

    filtered_df=filter_dataframe(frequency_df,pd.to_datetime(start_date),pd.to_datetime(end_date))
    type_graph= scatter_graph(filtered_df,tipo,["All"]+test_type)
    genotype_graph= scatter_graph(filtered_df,genotype_label,["All"]+genotype_list)

    result_graph= scatter_graph(filtered_df,result_label,["All"]+results_list)

    ########################
    prefix=""
    if sensitivity_label=="Sensitivity Liquid based":
        prefix="Liquid based"
    if sensitivity_label=="Sensitivity Conventional":
        prefix="Conventional"
    sensitivity_graph= sensitivity_scatter_graph(filtered_df,prefix)




    ############## Create graph by adequacy (to do)
    #########define a prefix
    prefix=tipo
    if prefix=="All":
        prefix=""


    ##############
    adequate=filtered_df[prefix+"Sat"].sum()
    inadequate_processed=filtered_df[prefix+"Insat_NP"].sum()
    inadequate_not_processed=filtered_df[prefix+"Insat_P"].sum()

    adequacy_graph=make_adequacy_graph(adequate,inadequate_processed,inadequate_not_processed)
    ########### NUMBER OF TESTS
    number_of_tests=filtered_df[tipo].sum()
    ########## AVERAGE
    N=filtered_df.shape[0]

    average="No tests"
    if N !=0:
        avg=round(number_of_tests/N,1)
        average=str(avg)



    return  type_graph,adequacy_graph,result_graph,genotype_graph,sensitivity_graph,number_of_tests,average


#######################################################
if __name__ == "__main__":
    app.run_server(debug=True)