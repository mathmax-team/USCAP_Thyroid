import dash
from dash import dcc, callback
from dash import html,no_update
import numpy as np
import plotly.express as px
from dash.dependencies import Input, Output,State
from plotly import graph_objs as go
from plotly.graph_objs import *
import dash_bootstrap_components as dbc
from datetime import date
from sample_data import sensitivity_list,choices,last_week_date, last_year_date, last_month_date,results_list,genotype_list,type_list
from be.controllers.filtering_tools import filter_dataframe,make_plotable,next_monday
from be.controllers.scatter_plot import scatter_graph
from be.controllers.adequacy_bar_graph import make_adequacy_graph
from be.controllers.sensitivity_graph import sensitivity_scatter_graph
from be.controllers.default_times_ranges import Default_time_ranges,first_day,last_day,df
from be.controllers.tab_names import Overall,Movie,ComparingCP
# Connect to your app pages
from pages import Bethesda, Comparison, Molecular
import pandas as pd
# ############################## SOME INFO FROM DATA FRAME

# df=pd.read_csv("data/USCAP_Large.csv")
# for col in ["ACCESS_DATE","SIGN_DATE"]:
#     df[col]=df[col].apply(lambda z:pd.Timestamp(z))
# first_day=min(df["SIGN_DATE"].to_list())
# last_day=max(df["SIGN_DATE"].to_list())
# ############DICTIONARY FOR DEFAULT TIME RANGES
# ##################################################

# Default_time_ranges=dict()
# Default_time_ranges["Historical"]=[first_day,last_day]

# Default_time_ranges["Last year"]=[date.today().replace(day=1,month=1,year=date.today().year-1),date.today().replace(day=31,month=12,year=date.today().year-1)]

# Default_time_ranges["Current month"]=[date.today().replace(day=1),date.today()]
# Default_time_ranges["Current year"]=[date.today().replace(day=1,month=1),date.today()]
#############################################CALL BACK FOR DATES

############################# TABS
header_tabs=dbc.Tabs(id="id_tabs",
                        children=[
                        dbc.Tab(label=Overall,tab_id=Overall),
                        dbc.Tab( label=ComparingCP,tab_id=ComparingCP),
                        # dbc.Tab( label="Mutations by Category",tab_id="Mutations by Category"),
                        # dbc.Tab(label="Mutations by Result",tab_id="Mutations by Result"),
                        dbc.Tab(label=Movie,tab_id=Movie),
                        ],
                         )
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

def image_link(link,path_to_image):
    return html.A(
                    href=link,
                    children=[
                    html.Img(
                    src=path_to_image,height="50px"
                    )
                      ]
                    )
###################  GENERATE THE DROPDOWN ELEMENTS  #######################


# # dropletter=make_drop(['Last year', 'Last month', 'Last week'],"dropletter")
# type_drop=make_drop(type_list+["All test types"],"type")
# results_drop=make_drop(results_list+["All results"],"results")###### it starts at 1 to rule out the "All results" option
# genotype_drop=make_drop(genotype_list+["All genotypes"],"genotype")


# dropletter=dbc.DropdownMenu(
#     children=[
#         dbc.DropdownMenuItem("Math"),
#         dbc.DropdownMenuItem("Physics"),
#         # dbc.DropdownMenuItem(divider=True),
#         dbc.DropdownMenuItem("Computing"),
#     ],
#     nav=True,
#     in_navbar=True,
#     label="Menu",
# )

# def drawFigure(altura,id):
#     return  html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 dcc.Graph(
#                     figure={},
#                     id=id,
#                     config={
#                         'displayModeBar': False
#                     },
#                 )
#             ],
#             )
#         ),
#     ])

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


logo = dbc.Navbar(
dbc.Container(
    [html.A(

            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(image_link("","/assets/UHealth_logo.png"),width=2),
                    # dbc.Col(html.Img(src="/assets/USCAPheaderlogo.png", height="50px"),width=2),
                    dbc.Col(image_link("","/assets/USCAPheaderlogo.png"),width=2),
                    dbc.Col(header_tabs,width=8),
                ],
                align="center",
                className="g-0",
                justify="center",
            ),
    style={"textDecoration": "none","content-align":"left","width":"90%"}),

    ],
),
# color="#0dcdf6",
color="#aab8b1",
dark=True,
className="mb-5",
style={"height":"8vh"},
)

# Comparison.layout
# Layout of Dash App
app.layout = html.Div(
     children=[logo,
        # html.Div(children=["Camilo"],id="id_hidden"),#,style={"display":"None"}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', children=[Bethesda.layout],style={"height":"85vh","backgkround-color":"white","margin-top":"0px"}),
        html.Div([
                        html.P(
                            "POWERED BY ",
                            style={"font-size":"0.5em","align-self":"center"}),
                        # html.Div(image_link("",app.get_asset_url("logo_IC_nobg.png")),className="logo",style={'display': 'inline-block',"height":"7vh"})
                        html.Img(
                            className="logo",
                            src=app.get_asset_url("logo_IC_nobg.png"),
                            style={'display': 'inline-block',"height":"7vh"}),
                    ],style={"display":"flex","height":"10vh","justify-content":"center","color":"white","background-color":"black","margin-bottom":"0px"}
                    ),
                    ],
        )


app.config.suppress_callback_exceptions=True
#######################################################

# @app.callback(
#     Output(component_id='id_hidden', component_property='children'),
#     Input(component_id='id_tabs', component_property='active_tab'),

#     # State(component_id='ROM', component_property='value'),

# )
# def update_page(input_value):
#     ans="Dashboard"
#     if input_value == "ROM":
#         ans="Movie"
#     return ans

# @app.callback(
#     Output(component_id='page-content', component_property='children'),
#     Input(component_id='id_hidden', component_property='children'),
# )
# def update_page(hidden_word):
#     ans=Bethesda_distribution.layout
#     if hidden_word=="Movie":
#         ans=Molecular.layout
#     return ans

if __name__ == "__main__":
    app.run_server(debug=True,port=8051)
