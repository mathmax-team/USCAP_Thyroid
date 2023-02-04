import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objs as go
from plotly.graph_objs import *
import dash_bootstrap_components as dbc
from datetime import date
from sample_data import sensitivity_list,choices,last_week_date, last_year_date, last_month_date,results_list,genotype_list,type_list
from be.controllers.filtering_tools import filter_dataframe,make_plotable,next_monday
from be.controllers.scatter_plot import scatter_graph
from be.controllers.adequacy_bar_graph import make_adequacy_graph
from be.controllers.sensitivity_graph import sensitivity_scatter_graph



Records_df=pd.read_csv("Records.csv")
Records_df["day"]=pd.to_datetime(Records_df["day"])

############# GRAPH BY TYPE


# filtered_df=filter_dataframe(frequency_df,pd.to_datetime(last_month_date),pd.to_datetime(last_week_date))
# type_graph= scatter_graph(filtered_df,"Liquid based",["All"]+type_list)

table_header = [
    html.Thead(html.Tr([html.Th("Tests"), html.Th("Daily avg"),html.Th("Positive rate"),html.Th("False negative rate")]))
]

row1 = html.Tr([html.Td("345",id="tests"), html.Td("45.6",id="average"),html.Td("Positivity rate",id="positivity_rate"),html.Td("0.4",id="false_negative_rate")])


table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"20px"})
###############
def make_drop(lista:list,id:str):
    menu=dcc.Dropdown(id=id,
    options=[ {"label": i, "value": i} for i in lista],
    value=lista[-1],
    clearable=False,


        )
    return {"drop":menu}


###################  GENERATE THE DROPDOWN ELEMENTS  #######################


dropletter=make_drop(['Last year', 'Last month', 'Last week'],"dropletter")
type_drop=make_drop(type_list+["All test types"],"type")
results_drop=make_drop(results_list+["All results"],"results")###### it starts at 1 to rule out the "All results" option
genotype_drop=make_drop(genotype_list+["All genotypes"],"genotype")




def drawFigure(altura,id):
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure={},
                    id=id,
                    config={
                        'displayModeBar': False
                    },
                )
            ])
        ),
    ])

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

navbar = dbc.NavbarSimple(
        children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
            ],
            brand=["camilo","matilde",""
                    ],
            brand_href="#",
            color="green",
            dark=True,
            style={"font-color":"red"}
        )
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Math"),
        dbc.DropdownMenuItem("Physics"),
        # dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Computing"),
    ],
    nav=True,
    in_navbar=True,
    label="Options",
)
logo = dbc.Navbar(
dbc.Container(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src="/assets/UHealth_logo.png", height="50px")),
                    # dbc.Col(html.Img(src="/assets/USCAPheaderlogo.png", height="50px")),
                    # dbc.Col(html.P(""),width=2),
                    # dbc.Col(html.P("POWER BY",style={"color":"white","font-size":"12px"}),width=2),
                    dbc.Col(html.Img(src="/assets/logo_IC_nobg.png", height="80px")),
                ],
                align="center",
                # className="g-0",
                justify="center"
            ),
            href="https://plotly.com",
            style={"textDecoration": "none","content-align":"left"},
        ),
        dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
        dbc.Collapse(
            dbc.Nav(
                [dropdown],
                className="ms-auto",
                navbar=True,
            ),
            id="navbar-collapse2",
            navbar=True,
        ),
    ],
),
color="#69ad7a",
dark=True,
className="mb-5",
# style={"color":"blue","height":"70px"}
)


# Layout of Dash App
app.layout = html.Div(
    children=[logo,
        # html.Div(html.P("camilo"),style={"display":"flex","justify-content":"center"}),
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                    #     html.Div(
                    # [
                    # #     html.A(
                    # # html.Img(
                    # #     className="logo",
                    # #     src=app.get_asset_url("UHealth_logo.png"),
                    # #     style={"justify-self":"center","height":"100px"}
                    # # ),
                    # # href="https://umiamihealth.org/en/",
                    # # # style={'display': 'inline-block'}),
                    # # ),
                    # ],
                    # style={"display":"flex","justify-content":"center"}
                    # ),
                    # html.Div([
                    # html.P(
                    #     "POWERED BY",
                    #     style={"font-size":"0.4em","align-self":"center"}),
                    # html.Img(
                    #     className="logo",
                    #     src=app.get_asset_url("logo_IC_nobg.png"),
                    #     style={'display': 'inline-block',"height":"50px"}),
                    # ],style={"display":"flex","height":"50px","justify-content":"center","margin-top":"0px"}
                    # ),
                    html.Div([
                        html.H1("Cytopathology - Monitor"),
                         ],style={"display":"flex","justify-content":"center"}),
                    html.Div([
                        html.P("Here I asay something")
                    ],
                    style={"display":"flex","justify-content":"center"}),
                    html.Div(
                        className="row",
                        children=[
                            html.Div(
                                className="div-for-dropdown",
                                children=[
                                    dropletter["drop"]
                                ],
                            ),
                        ],
                        ),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            dcc.DatePickerSingle(
                                id = 'date_start',
                                style={"width":"100%"}
                                    )
                        ],
                    ),
                    # Change to side-by-side for mobile layout
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            dcc.DatePickerSingle(
                                id = 'date_end',
                                style={"width":"100%"}
                                    )
                        ],
                    ),
                    table,
                    drawFigure("200px","sensitivity-graph"),
                    html.Div(drawFigure("250px","adequacy-graph"),style={"margin-top":"15px"}),
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="eight columns div-for-charts bg-grey",
                    children=[
                        html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        type_drop["drop"]
                                    ],
                                    style={"height":"50px"}
                                ),
                        drawFigure("200px","types-graph"),
                        #dcc.Graph(id="map-graph"),
                        html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown to select times
                                        results_drop["drop"]
                                    ],
                                ),
                        #dcc.Graph(id="histogram"),
                        drawFigure("200px","result-graph"),
                        html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        genotype_drop["drop"]
                                    ],
                                ),
                        drawFigure("200px","genotype-graph"),
                    ],
                ),
            ],
            style={"margin-top":"0px","padding":"0px"}
        )
        ]
        )


@app.callback(
    Output(component_id= 'date_start', component_property='date'),
    Output(component_id= 'date_end', component_property='date'),
    Input(component_id='dropletter', component_property='value')
)
def update_time_range(input_range):
    """Control time range selection."""
    start_date=last_year_date
    end_date=date.today()
    if input_range == 'Last week':
        start_date = last_week_date
    elif input_range == 'Last month':
        start_date =last_month_date
    elif input_range == 'Last year':
        start_date = last_year_date
    end_date = date.today()
    return start_date, end_date

####################### CALL BACK UPDATE GRAPHS
# @app.callback(

#     Output(component_id='types-graph', component_property='figure'),
#     Output(component_id='result-graph', component_property='figure'),
#     Output(component_id='genotype-graph', component_property='figure'),
#     Output(component_id='adequacy-graph', component_property='figure'),
#     Output(component_id='sensitivity-graph', component_property='figure'),
#     Output(component_id='tests', component_property='children'),
#     Output(component_id='average', component_property='children'),
#     Output(component_id='positivity_rate', component_property='children'),
#     Output(component_id='false_negative_rate', component_property='children'),

#     Input(component_id= 'date_start', component_property='date'),
#     Input(component_id= 'date_end', component_property='date'),
#     Input(component_id='type', component_property='value'),
#     Input(component_id='results', component_property='value'),
#     Input(component_id='genotype', component_property='value'),

# )
def update_graphs(start_date,end_date,type_label,result_label,genotype_label):
    if type_label==None:
        type_label="Liquid based"
    if result_label==None:
        type_label="Negative"
    if genotype_label==None:
        genotype_label="HPV 16"

    type_label=str(type_label)
    result_label=str(result_label)
    genotype_label=str(genotype_label)

    #################### FILTER BY DATE

    filtered_Rec_df=filter_dataframe(Records_df,pd.to_datetime(start_date),pd.to_datetime(end_date))

########### UPDATE NUMBER OF TEST
    number_of_tests=filtered_Rec_df.shape[0]

 ########## UPDATE AVERAGE
    number_of_days=filtered_Rec_df["day"].nunique()

    average="No tests"
    if number_of_days !=0:
        average=round(number_of_tests/number_of_days,1)

########## UPDATE POSITIVE RATE
    number_of_negatives=filtered_Rec_df[filtered_Rec_df["result"]=="Negative"].shape[0]
    number_of_positives=number_of_tests-number_of_negatives
    positive_rate = "No tests"
    if number_of_tests !=0:
        positive_rate=round(number_of_positives/number_of_tests,4)
##################################################### UPDATE FALSE NEGATIVE RATE
    number_of_negative_cytologies=filtered_Rec_df[filtered_Rec_df["cytology"]=="Negativecytology"].shape[0]
    number_of_false_negatives=filtered_Rec_df["need_surgery"].sum()
    false_negative_rate = "No tests"
    if number_of_negative_cytologies !=0:
        false_negative_rate=round(0.1*number_of_false_negatives/number_of_negative_cytologies,4)

################### GROUP BY WEEK WHEN NEEDED

    if pd.Timedelta(pd.to_datetime(end_date)-pd.to_datetime(start_date)).days>100:
        filtered_Rec_df["day"]=filtered_Rec_df["day"].apply(lambda z:next_monday(z))




############# GRAPH BY TYPE
    if type_label[:3]=="All":
        type_label="All"
    if genotype_label[:3]=="All":
        genotype_label="All"
    if result_label[:3]=="All":
        result_label="All"

    types_dict=dict()
    for possibility in ["All"]+type_list:
        types_dict[possibility]=make_plotable(filtered_Rec_df,{"type":possibility})

    type_graph=scatter_graph(type_label,types_dict)

#################################### GRAPH BY RESULT ############

    results_dict=dict()
    for possibility in ["All"]+results_list:
        results_dict[possibility]=make_plotable(filtered_Rec_df,{"result":possibility,"type":type_label})

    results_graph=scatter_graph(result_label,results_dict)

#################################### GRAPH BY RESULT ############

    genotype_dict=dict()
    for possibility in ["All"]+genotype_list:
        genotype_dict[possibility]=make_plotable(filtered_Rec_df,{"genotype":possibility,"type":type_label,"result":result_label})

    genotype_graph=scatter_graph(genotype_label,genotype_dict)


############################################### SENSITIVITY GRAPH

    sensitivity_dict=dict()

    sensitivity_dict["Positive cytology"]=make_plotable(filtered_Rec_df,{"cytology":"Positivecytology"})
    sensitivity_dict["Positive histology"]=make_plotable(filtered_Rec_df,{"cytology":"Positivecytology","hystology":"Positivehystology"})
    sensitivity_graph=sensitivity_scatter_graph(sensitivity_dict)


    ############## GRAPH ADEQUAC

    adequate=filtered_Rec_df[filtered_Rec_df["adequacy"]=="Sat"].shape[0]
    inadequate_processed=filtered_Rec_df[filtered_Rec_df["adequacy"]=="Insat_P"].shape[0]
    inadequate_not_processed=filtered_Rec_df[filtered_Rec_df["adequacy"]=="Insat_NP"].shape[0]
    adequacy_graph=make_adequacy_graph(adequate,inadequate_processed,inadequate_not_processed)

    return  type_graph,results_graph,genotype_graph,sensitivity_graph,adequacy_graph,number_of_tests,average,positive_rate,false_negative_rate


#######################################################


if __name__ == "__main__":
    app.run_server(debug=True)
