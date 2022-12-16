"""Dash App for visualization of tables and graphics."""
from dash import Dash, html, dcc, Output, Input
import flask
import plotly.express as px
import pandas as pd
from sample_data import last_week_date, last_year_date, last_month_date,test_type, results_list, genotype_list
from datetime import date
from be.controllers.types_graph import types_graph
from be.controllers.filter_dataframe import filter_dataframe
from be.controllers.tree_map_graph import tree_map_graph
from be.controllers.results_graph import result_graph
from be.controllers.mvp_graph import mvp_graph
from be.controllers.qc_graph import qc_graph
import datetime
#from fe.assets.colors import color as mycol

external_stylesheets = ['/assets/styles.css']
f_app = flask.Flask(__name__)
app = Dash(__name__, server=f_app, external_stylesheets=external_stylesheets)

test_df = pd.read_csv('test_dataframe.csv')
test_df["day"]=pd.to_datetime(test_df["day"])
initial_df = pd.read_csv('test_type_count.csv')
initial_df["day"]=pd.to_datetime(initial_df["day"])

# html.Img(src="fe/assets/micro.png" alt="logo")
#,'backgroundColor':"black"
app.layout = html.Div(children=[
                html.Div(children=[
                    ###Name and Logo
                    html.Div(children=[
                        html.Img(src="assets/medicine.svg",style={'height': '60px','margin-bottom': '10px'}),
                        html.H1('CYTOPATHOLOGY MONITOR',style={"margin-top":"10px","textAlign":"center"})
                        ],
                        style={"margin-left":"20px","align-items":"center"},
                        className="horizontal"
                    ),
                    ##Time and default ranges
                    html.Div(children=[
                        html.Label('Time period:',style={'font-size':"20px",'font-weight':"bold","display":"flex"}),
                        dcc.Dropdown(['last week', 'last month', 'last year'], 'last month',
                            style={'width': '200px','color':'black',"font-size":"20px","display":"flex","align-items": "center","justifyContent":"right","height":"1.2cm"} ,id="default-time-ranges"),


                            ], style={"margin-left":"20mm","display":'table','justify-items': 'center', 'align-items': 'right','width': '100px'}
                    ),
                    ###DatePicker
                    dcc.DatePickerRange(
                            id = 'date-range',
                            start_date_placeholder_text = last_month_date,
                            end_date = date.today(),
                            max_date_allowed = date.today(),
                            day_size=30,
                        style={"width":"10cm","height":"20cm","margin-top":"50px","margin-left":"20px"}),
                    ##Title and Treegraph
                    html.Div(children=[
                        html.H3('Type : ', style={'fontWeigth': 'bold','textAlign':'center','font-size':"20px"},id='type-selected'),
                        dcc.Graph(
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
                                style={"height":"100px","width":"100px"}
                                    )
                                    ],
                                    style={},
                                    className="vertical")

                    ],
                    style={"display":"flex","height":"30mm"},
                    id="grad"
                    ),
                html.Hr(),
                html.Div(children=[

                    #


                        #First GRAPH
                    html.Div(children=[
                            html.Div(children=[
                            #html.H2('Test', style={'textAlign': 'center'}),
                            html.H3('Test selected: '),
                            dcc.Dropdown(test_type,value=test_type[0],
                                id = 'type-dropdown',
                                style={"color":"white","width":"200px"}
                            )],style={"display":'flex','justifyContent': 'center', 'alignItems': 'center','width': '100%',"height":"40px"}
                        ),
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
                            ),

                            # dcc.RadioItems(test_type,
                            # value='liquid based',
                            # id = 'type-radio'
                            # ),
                        ],
                        style={'padding':'10px', 'border':None}),
                        #Second GRAPH
                        # html.Div(children=[
                        #     html.H2('Adequacy', style={'textAlign': 'center'}),

                        # ], style={'padding':'10px', 'border':None}),

                        #Third GRAPH
                        html.Div(children=[
                            html.Div(children=[
                                #html.H2('Results', style={'textAlign': 'center'}),
                                html.H3('Select Adequacy: ', style={'fontWeigth': 'bold'}),
                                #html.Div(id='adequacy-selected'),
                                dcc.Dropdown(results_list,
                                value=results_list[0],
                                id = 'selected-result'
                                ,style={'color':'white',"font-size":"20px","width":"200px"})],style={"display":'flex','justifyContent': 'center', 'alignItems': 'center','width': '100%',"height":"40px"}
                            ),
                            dcc.Graph(id='results-graph', figure={},
                                config={
                                    'staticPlot': False,     # True, False
                                    'scrollZoom': False,      # True, False
                                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                    'showTips': False,       # True, False
                                    'displayModeBar': False,  # True, False, 'hover'
                                    'watermark': False,
                                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                        },),


                        ], style={'padding':'10px'}),


                        #Fourth GRAPH
                        html.Div(children=[
                            #html.H2('MVP', style={'textAlign': 'center'}),
                            html.H3('Result selected: ', style={'fontWeigth': 'bold'}),
                             dcc.RadioItems(genotype_list,
                            value=genotype_list[0],
                            id = 'genotype-radio'
                            ),
                            html.Div(id='result-selected'),
                            dcc.Graph(id='mvp-graph', figure={},
                                config={
                                    'staticPlot': False,     # True, False
                                    'scrollZoom': False,      # True, False
                                    'doubleClick': 'reset+autosize',  # 'reset', 'autosize' or 'reset+autosize', False
                                    'showTips': False,       # True, False
                                    'displayModeBar': False,  # True, False, 'hover'
                                    'watermark': False,
                                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                        }),
                            # dcc.Dropdown(genotype_list,
                            # value=genotype_list[0],
                            # id = 'selected-genotype'
                            # ),

                        ], style={'padding':'10px', 'border':None}),

                        #Fifth GRAPH
                        html.Div(children=[
                            #html.H2('QC', style={'textAlign': 'center'}),
                            html.H3('MVP selected:', style={'fontWeigth': 'bold'}),
                            html.Div(id='genotype-selected'),
                            dcc.Graph(id='qc-graph', figure={},
                                config={
                                    'staticPlot': False,     # True, False
                                    'scrollZoom': False,      # True, False
                                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                    'showTips': False,       # True, False
                                    'displayModeBar': False,  # True, False, 'hover'
                                    'watermark': False,
                                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                                    },),
                        ], style={'padding':'10px'}),
                        ],
                        #html.Div('6', style={'padding':'0px', 'border':None}),
                    id="grid",
                    style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gridTemplateRows':'repeat(3, 1fr)','gridAutoFlow': 'row'})
                    ])




@app.callback(
    Output(component_id= 'date-range', component_property='start_date'),
    Output(component_id= 'date-range', component_property='end_date'),
    Input(component_id='default-time-ranges', component_property='value')
)
def update_time_range(input_range):
    """Control time range selection."""
    if input_range == 'last week':
        start_date = last_week_date
    elif input_range == 'last month':
        start_date =last_month_date
    elif input_range == 'last year':
        start_date = last_year_date
    end_date = date.today()
    return start_date, end_date



@app.callback(
    #Output(component_id='type-selected', component_property='children'),
    #Output(component_id='adequacy-selected', component_property='children'),
    Output(component_id='result-selected', component_property='children'),
    Output(component_id='genotype-selected', component_property='children'),
    Output(component_id='types-graph', component_property='figure'),
    Output(component_id='tree-map', component_property='figure'),
    Output(component_id='results-graph', component_property='figure'),
    Output(component_id='mvp-graph', component_property='figure'),
    Output(component_id='qc-graph', component_property='figure'),

    Input(component_id = 'type-dropdown', component_property='value'),
    Input(component_id='tree-map', component_property='clickData'),
    Input(component_id='selected-result', component_property='value'),
    Input(component_id='genotype-radio', component_property='value'),
    # Input(component_id='default-time-range', component_property='start_date'),
    Input(component_id='default-time-ranges', component_property='value')
)
def update_graphs(type, click_data, result, genotype, input_range):

    """Return all graphs based on interactive filters."""
    if input_range == 'last week':
        start_date = last_week_date
    elif input_range == 'last month':
        start_date =last_month_date
    elif input_range == 'last year':
        start_date = last_year_date

    end_date = date.today()

    filtered_df = filter_dataframe(initial_df,pd.to_datetime(start_date),pd.to_datetime(end_date))
    types = types_graph(filtered_df, type)
    test_dataframe = filter_dataframe(test_df,pd.to_datetime(start_date), pd.to_datetime(end_date))
    tree_data = tree_map_graph(test_dataframe, type, click_data)
    tree_graph = tree_data[0]
    # message =  tree_data[1]
    # processed = tree_data[2]
    result_df = tree_data[3]
    results_data = result_graph(result_df, type, result)
    results_graph = results_data[0]
    mvp_data = mvp_graph(results_data[1], type, result, genotype)
    mvps_graph = mvp_data[0]
    qc = qc_graph(result_df, type, result, genotype)
#f'{type}'
    return f'{result}', f'{genotype}', types, tree_graph, results_graph, mvps_graph, qc
# #initial_df["day"][5]>last_month_date
# print("this is type" ,type(initial_df["day"][0]))
# print(initial_df.dtypes)
if __name__ == '__main__':
    app.run_server(debug=True)