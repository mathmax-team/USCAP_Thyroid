# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

table_header = [
    html.Thead(html.Tr([html.Th("Tests"), html.Th("Daily avg"),html.Th("Positive rate"),html.Th("False negative rate")]))
]

row1 = html.Tr([html.Td("345",id="tests"), html.Td("45.6",id="average"),html.Td("Positivity rate",id="positivity_rate"),html.Td("0.4",id="false_negative_rate")])


table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"20px"})
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
time_period_choice=make_drop(["Historical","Last week","Last Month","Year to date"],"time_period_choice")
sex_choice=make_drop(["All sexes","Female","Male"],"sex_choice")
responsable_choice=make_drop(["Laboratory","Peter","Jane","Alice"],"responsable_choice")
age_choice=make_drop(["All ages","Young","Old"],"age_choice")
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
,style={"height":"35vh"," background-color":"rgb(18, 18, 18)"},
)##8af2a6"})

smallcard = dbc.Card(
    dbc.CardBody(
        [table,
            # html.H4("Title", id="card-title"),
            # html.H2("100", id="card-value"),
            # html.P("Description", id="card-description")
        ]
    )
,style={"height":"20vh","background-color":"#8af2a6","margin-top":"40px"})

layout = html.Div(
     children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="three columns div-user-controls",
                    children=[
                    html.H5([
                        html.P("Bethesda Classification"),
                         ],style={"display":"flex","justify-content":"center"}),
                    html.Div([
                        html.H5("Here I asay something")
                    ],
                    style={"display":"flex","justify-content":"center"}),

                        # className="row",
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            time_period_choice
                        ],
                    ),
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
                            responsable_choice
                        ],
                    ),
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

                html.Div(
                        className="div-for-dropdown",
                        children=[
                            sex_choice
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

                    ])
    #    style={"height":"500px"} )