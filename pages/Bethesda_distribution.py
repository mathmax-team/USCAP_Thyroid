# Import necessary libraries
import dash
from dash import html, dcc, callback,no_update
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output,State
from datetime import date,timedelta
import pandas as pd
from be.controllers.pie_chart import make_pie
from be.controllers.roman import make_roman
from be.controllers.bar_chart import make_bar
from be.controllers.ROM_chart import make_rom
from be.controllers.Gene_mutated import make_gene
import numpy as np
##################################################


############################## SOME INFO FROM DATA FRAME

df=pd.read_excel("data/USCAP.xlsx")
first_day=min(df["SIGN_DATE"].to_list())
last_day=max(df["SIGN_DATE"].to_list())
############DICTIONARY FOR DEFAULT TIME RANGES
##################################################

Default_time_ranges=dict()
Default_time_ranges["Historical"]=[first_day,last_day]

Default_time_ranges["Last year"]=[date.today().replace(day=1,month=1,year=date.today().year-1),date.today().replace(day=31,month=12,year=date.today().year-1)]

Default_time_ranges["Current month"]=[date.today().replace(day=1),date.today()]
Default_time_ranges["Current year"]=[date.today().replace(day=1,month=1),date.today()]



################################################RENAME PATHOLOGISTS
df["CYTOPATHOLOGIST"]=df["CYTOPATHOLOGIST"].apply(lambda z: "Pathologist " + str(int(z)) if(str(z) != 'nan') else z)
###################################### LIST OF PATHOLOGISTS

pathologists=df["CYTOPATHOLOGIST"].tolist()
pathologists=[x for x in pathologists if str(x) !="nan"]
# pathologists=list(map(lambda z:int(z),pathologists))
pathologists=list(set(pathologists))
pathologists=["All pathologists"]+pathologists

##########################
#########   TABLE I
##########################

table_headerI = [
    html.Thead(html.Tr([html.Th("Number of tests"),html.Th("Positive test"),html.Th("Positivity overall")]))
]

row1I = html.Tr([html.Td("345",id="id_tests"), html.Td("45.6",id="id_positive_tests"),html.Td("someother",id="id_positivity_overall")])


table_bodyI = [html.Tbody([row1I])]

tableI = dbc.Table(table_headerI + table_bodyI, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"0px"})

################# TABLE II

table_headerII = [
    html.Thead(html.Tr([html.Th("Molecular tests"),html.Th("Positivity molecular")]))
]

row1II = html.Tr([html.Td("345",id="id_molecular_tests"), html.Td("45.6",id="id_positivity_molecular")])


table_bodyII = [html.Tbody([row1II])]

tableII = dbc.Table(table_headerII + table_bodyII, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"0px"})


def oldmake_drop(lista:list,id:str):
    menu=dcc.Dropdown(id=id,
    options=[ {"label": html.Span([i],style={"color":"yellow"}), "value": i} for i in lista],
    value=lista[-1],
    clearable=False,
    style={"color":"red",}

        )
    return {"drop":menu}

############################################################
def make_drop(lista:list,id:str):
    menu=dcc.Dropdown(
    lista,
    lista[0],
    id=id,
    maxHeight=300,
    clearable=False,
        )
    return menu


###################  GENERATE THE DROPDOWN ELEMENTS  #######################

time_period_choice=make_drop(["Historical","Current year","Current month","Last year"],"id_time_period_choice")
sex_choice=make_drop(["All sexes","Female","Male"],"id_sex_choice")
responsable_choice=make_drop(pathologists,"id_responsable_choice")
ages=["All ages","Less than 40","40 to 49","50 to 59","60 to 69","70 or older"]
age_choice=make_drop(ages,"id_age_choice")
simpledrop=dcc.Dropdown(
    ['New York City', 'Montreal', 'Paris', 'London', 'Amsterdam', 'Berlin', 'Rome'],
    'Paris', id='height-example-dropdown', maxHeight=300,clearable=False
)
newdrop=dcc.Dropdown(
    [
        {
            "label": html.Span(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "MTL",
            "search": "Montreal"
        },
        {
            "label": html.Span(['New York City'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
            "search": "New York City"
        },
        {
            "label": html.Span(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "LON",
            "search": "London"
        },
    ], value='Montreal',
)

dropletter=make_drop(['Last year','Last month','Last week','All time'],"dropletter")


choices=dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Math"),
        dbc.DropdownMenuItem("Physics"),
        # dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Computing"),
    ],
    # nav=True,
    # in_navbar=True,
    label="Menu",
)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 4, 6, 7, 5, 9, 7, 8]
))

fig.update_layout(
    autosize=False,
    width=470,
    height=300,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    template="plotly_dark",
    paper_bgcolor=" rgb(18, 18, 18)",
    plot_bgcolor=" rgb(18, 18, 18)"
)
def make_card(id):
    card = dbc.Card(
        dbc.CardBody(
            [dcc.Graph(id=id,
        figure=fig,
    style={"height":"100%"},
    config={
                            'displayModeBar': False
                        })
                # html.H4("Title", id="card-title"),
                # html.H2("100", id="card-value"),
                # html.P("Description", id="card-description")
            ]
        )
    ,style={"height":"35vh"," background-color":"rgb(18, 18, 18)"},
    )
    return card

# smallcard = dbc.Card(
#     dbc.CardBody(
#         [table,
#             # html.H4("Title", id="card-title"),
#             # html.H2("100", id="card-value"),
#             # html.P("Description", id="card-description")
#         ]
#     )
# ,style={"height":"20vh","background-color":"#8af2a6","margin-top":"40px"})

layout = html.Div(
     children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="three columns div-user-controls",
                    children=[

                    html.Div(className="div_for_text",
                    children=[html.H5("Bethesda Category")
                    ]),
                    html.Div(className="div_for_text",
                        children=[html.P("Default time periods")],style={"height":"25px"}),

                        # className="row",
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            time_period_choice
                        ],
                    ),
                    html.Div(className="div_for_text",
                        children=[html.P("Custom time period")],style={"height":"25px"}),
                    html.Div(
                    className="div-for-dropdown",
                    children=[
                        dcc.DatePickerRange(
                            id = 'id_date_range',
                            # style={"width":"100%"}
                                )
                    ],
                ),
                html.Div(className="div_for_text",
                        children=[html.P("Filter by pathologist")],style={"height":"25px"}),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            responsable_choice
                        ],
                    ),
                html.Div(className="div_for_text",
                        children=[html.P("Filter by age")],style={"height":"25px"}),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                           age_choice
                        ],
                    ),


                #     html.Div(
                #     className="div-for-dropdown",
                #     children=[
                #         dcc.DatePickerSingle(
                #             id = 'date_start',
                #             style={"width":"100%"}
                #                 )
                #     ],
                # ),
                # # Change to side-by-side for mobile layout
                # html.Div(
                #     className="div-for-dropdown",
                #     children=[
                #         dcc.DatePickerSingle(
                #             id = 'date_end',
                #             style={"width":"100%"}
                #                 )
                #     ],
                # ),
                html.Div(className="div_for_text",
                        children=[html.P("Filter by sex")],style={"height":"25px"}),
                html.Div(
                        className="div-for-dropdown",
                        children=[
                            sex_choice
                        ],
                    ),
                tableI,
                tableII,
                # smallcard,
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="nine columns div-for-charts bg-grey",
                    children=[
                    html.Div([
                    dbc.Row([
                        dbc.Col([make_card("id_first_graph")]), dbc.Col([make_card("id_second_graph")])
                    ]),
                    dbc.Row([
                        dbc.Col([make_card("id_third_graph")]), dbc.Col([make_card("id_fourth_graph")]),
                    ]),
                    # dbc.Row([
                    #     dbc.Col([card]), dbc.Col([card]),dbc.Col([card])
                    # ])
                ])
                    ],
                ),


        ],
        style={"margin-top":"0px","padding":"0px","height":"40vh","background-color":"1f1f1f"}
    )

                    ])

############################################CALL BACK FOR SET CUSTOM
#@callback(
#     Output(component_id='id_time_period_choice', component_property='value'),
#     Input(component_id= 'id_date_range', component_property='start_date'),
#     Input(component_id= 'id_date_range', component_property='end_date'),

#         )
# def update_time_range(start,end):
#     """Control time range selection."""
#     ans=0
#     for item in ["Historical","Last year"]:
#         if [pd.to_datetime(start),pd.to_datetime(end)]==list(map(lambda z:pd.to_datetime(z),Default_time_ranges[item])):
#             ans=item

#     return no_update if ans!=0 else None

#############################################CALL BACK FOR DATES
@callback(
    Output(component_id= 'id_date_range', component_property='start_date'),
    Output(component_id= 'id_date_range', component_property='end_date'),
    Input(component_id='id_time_period_choice', component_property='value'),
    # State(component_id= 'id_date_range', component_property='start_date'),
    # State(component_id= 'id_date_range', component_property='end_date'),
)
def update_time_range(input_range):
    """Control time range selection."""

    start_date=first_day
    end_date=last_day
    if input_range != None:
        [start_date,end_date]=Default_time_ranges[input_range]



    return no_update if input_range==None else start_date,end_date

#############################################CALL BACK FOR SET CUSTOM
# @callback(
#     Output(component_id='id_time_period_choice', component_property='value'),
#     Input(component_id= 'id_date_range', component_property='start_date'),
#     Input(component_id= 'id_date_range', component_property='end_date'),

#         )
# def update_time_range(start,end):
#     """Control time range selection."""
#     ans=0
#     for item in ["Historical","Last year"]:
#         if [pd.to_datetime(start),pd.to_datetime(end)]==list(map(lambda z:pd.to_datetime(z),Default_time_ranges[item])):
#             ans=item

#     return no_update if ans!=0 else None


#############################################CALL BACK FOR GRAPHS
@callback(
    Output(component_id= 'id_first_graph', component_property='figure'),
    Output(component_id= 'id_second_graph', component_property='figure'),
    Output(component_id= 'id_third_graph', component_property='figure'),
    Output(component_id= 'id_fourth_graph', component_property='figure'),
    Output(component_id= 'id_tests', component_property='children'),
    Output(component_id= 'id_positive_tests', component_property='children'),
    Output(component_id= 'id_positivity_overall', component_property='children'),
    Output(component_id= 'id_molecular_tests', component_property='children'),
    Output(component_id= 'id_positivity_molecular', component_property='children'),
    Input(component_id= 'id_date_range', component_property='start_date'),
    Input(component_id= 'id_date_range', component_property='end_date'),
    Input(component_id='id_responsable_choice', component_property='value'),
    Input(component_id='id_age_choice', component_property='value'),
    Input(component_id='id_sex_choice', component_property='value'),
)

def update_time_range(start_date,end_date,responsable,age,sex):
    data=df

    """Apply Date filter"""

    data=data[(data["SIGN_DATE"]>=pd.to_datetime(start_date))&(data["SIGN_DATE"]<=pd.to_datetime(end_date))]

    """Apply Pathologist filter"""
    if responsable !="All pathologists":
        data=data[data["CYTOPATHOLOGIST"]==responsable]

    """Apply Sex filter"""
    if sex !="All sexes":
        data=data[data["SEX"]==sex]

    """Apply Age filter"""


    if age =="Less than 40":
        data=data[data["AGE"]<40]
    if age =="40 to 49":
        data=data[(data["AGE"]>=40)&(data["AGE"]<50)]
    if age =="50 to 59":
        data=data[(data["AGE"]>=50)&(data["AGE"]<60)]
    if age =="60 to 69":
        data=data[(data["AGE"]>=60)&(data["AGE"]<70)]
    if age =="70 or older":
        data=data[data["AGE"]>=70]
################################### TABLE DATA
    tests=data.shape[0]
    positivity_overall="No data"
    positives_overall=data[data["RESULT"]=="POSITIVE"].shape[0]


    if tests>0:
        positivity_overall=round(positives_overall/tests,2)
    molecular_tests=data[data["MOLECULAR "]=="THYROSEQ"].shape[0]
    positivity_molecular="No data"
    positives_molecular=data[data["RESULT"]=="POSITIVE"].shape[0]


    if molecular_tests>0:
        positivity_molecular=round(positives_molecular/molecular_tests,2)

   ######## FIRST GRAPH
    title="Bethesda Category Distribution"
    Beth_info=data["Bethesda Cathegory"].value_counts().to_dict()
    numeric_names=sorted(list(Beth_info.keys()))
    values=[Beth_info[x] for x in numeric_names]
    names=[make_roman(x) for x in numeric_names]
    first_graph=make_pie(names,values,title)

    ######################  SECOND GRAPH
    labels_bar=sorted(list(data["Bethesda Cathegory"].unique()))
    values_bar=[len(data[data["Bethesda Cathegory"]==label])for label in labels_bar]
    bar_data=pd.DataFrame()
    bar_data["Count"]=values_bar
    bar_data["Category"]=[make_roman(x) for x in labels_bar]
    # bar_data["labels"]=bar_data["labels"].astype(str)
    second_graph=make_bar(bar_data,"Category","Count","Bethesda Category Counts")

    ######################  ROM GRAPH
    labels_bar=list(data["ROM"].unique())
    labels_bar=sorted([x for x in labels_bar if str(x) not in ["?","nan"]])
    values_bar=[len(data[data["ROM"]==label])for label in labels_bar]
    labels_bar=[str(x)+ "%" for x in labels_bar]
    bar_data=pd.DataFrame()
    bar_data["Count"]=values_bar
    bar_data["ROM"]=labels_bar
    bar_data["ROM"]=bar_data["ROM"].astype(str)
    rom_graph=make_rom(bar_data,"ROM","Count","Risk of Malignancy")

    ######################  GENE GRAPH
    labels_bar=list(data["GENE MUTATED"].unique())
    labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
    values_bar=[len(data[data["GENE MUTATED"]==label])for label in labels_bar]
    bar_data=pd.DataFrame()
    bar_data["Count"]=values_bar
    bar_data["GENE MUTATED"]=labels_bar
    bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)
    gene_graph=make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated")
    ##################
    # tests=data.shape[0]
    # positivity="No data"
    # positives=data[data["RESULT"]=="POSITIVE"].shape[0]


    # if tests>0:
    #     positivity=round(positives/tests,2)


    return first_graph,second_graph,rom_graph,gene_graph,tests,positives_overall,positivity_overall,molecular_tests,positivity_molecular
