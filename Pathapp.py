# 1. Import Dash
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
from sample_data import sensitivity_list,choices,last_week_date, last_year_date, last_month_date,results_list, genotype_list,type_list
from datetime import date
from be.controllers.filtering_tools import filter_dataframe,make_property_df,new_row_by_column
from be.controllers.scatter_plot import scatter_graph
from be.controllers.adequacy_bar_graph import make_adequacy_graph
from be.controllers.sensitivity_graph import sensitivity_scatter_graph
import pandas as pd


###########################################
#  THIS IS A PATHOLOGY MONITOR MOCKUP
##################  DATA #####################
frequency_df=pd.read_csv("Frequency.csv")
frequency_df["day"]=pd.to_datetime(frequency_df["day"])

################## MAKE DROPDOWN FROM LIST
def make_drop(lista:list,id:str):### This generates a dropdown .dbc object from parameters
    color="primary"
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
type_drop=make_drop(type_list+["All test types"],"type")
results_drop=make_drop(results_list+["All results"],"results")###### it starts at 1 to rule out the "All results" option
genotype_drop=make_drop(genotype_list+["All genotypes"],"genotype")
mvp=make_drop(sensitivity_list,"mvp")


###################### THE TABLE THAT DISPLAYS COUNT AND AVERAGE
table_header = [
    html.Thead(html.Tr([html.Th("Number of tests"), html.Th("Daily average")]))
]

row1 = html.Tr([html.Td("Arthur",id="tests"), html.Td("Dent",id="average")])


table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body, bordered=True,style={"width":"300px","height":"20px"})

###################### PAGE HEADER    #######################


page_header=[
    dbc.Row(html.Div(style={"height":"10px"})),
    dbc.Row([
        dbc.Col(
            [dbc.Row(html.Img(src="assets/UHealth_logo.png",style={'height': '60px'})),
            #dbc.Row(html.H3('Cytopathology Monitor'),style={"textAlign":"center"})
            ],
            #width="3",
            align="start"),
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
                            dbc.Row(type_drop["drop"],style={"textAlign":"center"}),
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
                                dbc.Row(results_drop["drop"],style={"textAlign":"center"}),
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
                            dbc.Row(genotype_drop["drop"],style={"textAlign":"center"}),
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
########################### CALL BACK type_drop ###################
@app.callback(
    [
     Output("type", "label")
     ],
    type_drop["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = type_drop["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
################  CALL BACK results_drop #################

@app.callback(
    [
     Output("results", "label")
     ],
    results_drop["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = results_drop["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]

########################## CALL BACK GENOTYPE DROP ###################
@app.callback(
    [
     Output("genotype", "label")
     ],
    genotype_drop["inputs"]
)
def update_default_period(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = genotype_drop["list"][0]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    return [button_id]
################  CALL BACK RESULTS DROP #################

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

################################## CALL BACK UPDATE DATE RANGES
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


######################## CALL BACK UPDATE GRAPHS
@app.callback(

    Output(component_id='types-graph', component_property='figure'),
    Output(component_id='tree-map', component_property='figure'),
    Output(component_id='results-graph', component_property='figure'),
    Output(component_id='mvp-graph', component_property='figure'),
    Output(component_id='qc-graph', component_property='figure'),
    Output(component_id='tests', component_property='children'),
    Output(component_id='average', component_property='children'),
    Input(component_id= 'date-range', component_property='start_date'),
    Input(component_id= 'date-range', component_property='end_date'),
    Input(component_id='type', component_property='label'),
    Input(component_id='results', component_property='label'),
    Input(component_id='genotype', component_property='label'),
    Input(component_id='mvp', component_property='label'),
)
def update_graphs(start_date,end_date,type_label,result_label,genotype_label,sensitivity_label):



############# GRAPH BY TYPE
    if type_label[:3]=="All":
        type_label="All"
    if genotype_label[:3]=="All":
        genotype_label="All"
    if result_label[:3]=="All":
        result_label="All"

    filtered_df=filter_dataframe(frequency_df,pd.to_datetime(start_date),pd.to_datetime(end_date))
    type_graph= scatter_graph(filtered_df,type_label,["All"]+type_list)

    ########## GRAPH BY GENOTYPE

    genotype_graph= scatter_graph(filtered_df,genotype_label,["All"]+genotype_list)

    ########### GRAPH BY RESULTS

    result_graph= scatter_graph(filtered_df,result_label,["All"]+results_list)

    ######################## GRAPH BY SENSITIVITY
    prefix=""
    if sensitivity_label=="Sensitivity Liquid based":
        prefix="Liquid based"
    if sensitivity_label=="Sensitivity Conventional":
        prefix="Conventional"
    sensitivity_graph= sensitivity_scatter_graph(filtered_df,prefix)




    ############## GRAPH BY ADEQUACY
    #########define a prefix
    prefix=type_label
    if prefix=="All":
        prefix=""


    ##############
    adequate=filtered_df[prefix+"Sat"].sum()
    inadequate_processed=filtered_df[prefix+"Insat_NP"].sum()
    inadequate_not_processed=filtered_df[prefix+"Insat_P"].sum()

    adequacy_graph=make_adequacy_graph(adequate,inadequate_processed,inadequate_not_processed)

    ########### UPDATE NUMBER OF TEST
    number_of_tests=filtered_df[type_label].sum()

    ########## UPDATE AVERAGE
    N=filtered_df.shape[0]

    average="No tests"
    if N !=0:
        avg=round(number_of_tests/N,1)
        average=str(avg)



    return  type_graph,adequacy_graph,result_graph,genotype_graph,sensitivity_graph,number_of_tests,average


#######################################################
if __name__ == "__main__":
    app.run_server(debug=True)