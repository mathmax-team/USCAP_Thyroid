# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def make_drop(lista:list,id:str):
    menu=dcc.Dropdown(id=id,
    options=[ {"label": html.Span([i],style={"color":"yellow"}), "value": i} for i in lista],
    value=lista[-1],
    clearable=False,
    style={"color":"red",}

        )
    return {"drop":menu}


###################  GENERATE THE DROPDOWN ELEMENTS  #######################

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



df_test_graph = px.data.tips()
fig = px.pie(df_test_graph, values='tip', names='day')

fig.update_layout(
    autosize=False,
    width=470,
    height=200,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    template="plotly_dark"
    # paper_bgcolor="gray",
    # plot_bgcolor="gray"
)

dfa=pd.read_excel("pages/data/USCAP.xlsx")

card = dbc.Card(
    dbc.CardBody(
        [dcc.Graph(
    figure=fig,
style={"height":"30vh"},
config={
                        'displayModeBar': False
                    })
            # html.H4("Title", id="card-title"),
            # html.H2("100", id="card-value"),
            # html.P("Description", id="card-description")
        ]
    )
,style={"height":"35vh","background-color":" rgb(18, 18, 18)"})##8af2a6"})

smallcard = dbc.Card(
    dbc.CardBody(
        [
            html.H4(str(len(dfa["SEX"])), id="card-title"),
            # html.P("Description", id="card-description")
        ]
    )
,style={"height":"15vh","background-color":"#8af2a6","margin-top":"10px"})

layout = html.Div(
     children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="three columns div-user-controls",
                    children=[
                    html.Div([
                        html.H1("Comparison"),
                         ],style={"display":"flex","justify-content":"center"}),
                    html.Div([
                        html.H5("Here I asay something")
                    ],
                    style={"display":"flex","justify-content":"center"}),

                        # className="row",
                    html.Div(
                    className="div-for-dropdown",
                    children=[
                        dcc.DatePickerRange(
                            id = 'date_range',
                            # style={"width":"100%"}
                                )
                    ],
                ),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            simpledrop
                        ],
                    ),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            simpledrop
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

                html.Div(
                        className="div-for-dropdown",
                        children=[
                            simpledrop
                        ],
                    ),
                html.Div(
                        className="div-for-dropdown",
                        children=[
                            simpledrop
                        ],
                    ),
                smallcard,
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="nine columns div-for-charts bg-grey",
                    children=[
                    html.Div([
                    dbc.Row([
                        dbc.Col([card]), dbc.Col([card]),
                    ]),
                    dbc.Row([
                        dbc.Col([card]), dbc.Col([card]),
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

                    ],)
    #    style={"height":"500px"} )