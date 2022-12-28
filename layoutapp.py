from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as df
from dash import html, dcc, Output, Input
from sample_data import sensitivity_list,choices,last_week_date, last_year_date, last_month_date,results_list, genotype_list,type_list

def make_drop(lista:list,id:str):### This generates a dropdown .dbc object from parameters
    color="secondary"
    size="lg"
    # if lista[0][:4]=="Last":
    #     color="warning"
    #     size="lg"
    #items=lista
    atems=list(map(lambda z: dbc.DropdownMenuItem(z,id=z),lista))
    inputs=list(map(lambda z: Input(z,"n_clicks"),lista))

    menu=dbc.DropdownMenu(atems,
    label=lista[0],
    className="mb-3",
    id= id,  #create an id for the dropdown menu to be used in the graph callback to modify the label
    color=color,
    size="sm",
    #     toggle_style={
    #     #"textTransform": "lowercase",
    #     #"background": "#67c29c",
    #    # "height":"0px",
    #    #siz
    #    }

        )
    return {"drop":menu,"inputs":inputs,"list":lista}


###################  GENERATE THE DROPDOWN ELEMENTS  #######################


dropletter=make_drop(["Cjlsj",'Last year', 'Last month', 'Last week'],"dropletter")


# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    },
                    style={"height":"230px"}
                )
            ])
        ),
    ])

# # Text field
# def drawText():
#     return html.Div([
#         dbc.Card(
#             dbc.CardBody([
#                 html.Div([
#                     html.H2("These are some words"),
#                 ], style={'textAlign': 'center'})
#             ])
#         ),
#     ])

# Data
df = px.data.iris()

# # Build App
# app = Dash(external_stylesheets=[dbc.themes.SLATE])

# app.layout = html.Div([
#     dbc.Card(
#         dbc.CardBody([
#             dbc.Row([
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#                 dbc.Col([
#                     drawText()
#                 ], width=3),
#             ], align='center'),
#             html.Br(),
#             dbc.Row([
#                 dbc.Col([
#                     drawFigure()
#                 ], width=3),
#                 dbc.Col([
#                     drawFigure()
#                 ], width=3),
#                 dbc.Col([
#                     drawFigure()
#                 ], width=6),
#             ], align='center'),
#             html.Br(),
#             dbc.Row([
#                 dbc.Col([
#                     drawFigure()
#                 ], width=9),
#                 dbc.Col([
#                     drawFigure()
#                 ], width=3),
#             ], align='center'),
#         ]), color = 'dark'
#     )
# ])

# # Run app and display result inline in the notebook
# app.run_server(debug=True)
import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# dbc.Col([
#         dbc.Row(type_drop["drop"],style={"textAlign":"center"}),
#         dbc.Row(
#         dcc.Graph(
#             id='types-graph',
#             figure={},
#             config={
#                 'staticPlot': False,     # True, False
#                 'scrollZoom': True,      # True, False
#                 'doubleClick': 'reset+autosize',  # 'reset', 'autosize' or 'reset+autosize', False
#                 'showTips': False,       # True, False
#                 'displayModeBar': False,  # True, False, 'hover'
#                 'watermark': False,
#                 # 'modeBarButtonsToRemove': ['pan2d','select2d'],
#                 },
#         style={"height":"320px"}
#         ),
#         style={"padding":"0px"},
#         )
#     ],
#     style={'padding':'5px'}
#     )


graph_container =dbc.Row(dbc.Col(
    [
    dbc.Row(dropletter["drop"],align="center",justify="center",style={"textAlign":"center","margin-bottom":"0px"}),
    dbc.Row(drawFigure())],
    className="flex-grow-1"
))

graph_container1 = html.Div(
    [drawFigure()],
    style={"backgroundColor": "blue"}, className="flex-grow-1"
)

content = html.Div(
[
        graph_container,
        graph_container,
        #html.P("This is column for content",style={"height":"50px"}),
        #html.P("Sample text 1"),
        #html.P("Sample text 2"),
        graph_container,
    ],
    className="h-100 d-flex flex-column",
)

page_structure = [
    dbc.Row(
        [
            dbc.Col(
                [
                dbc.Row(html.Img(src="assets/miami_white.png",style={"width":"350px","margin-Top":"30px","align":"center"})),
                dbc.Row(html.P("This is column 1")),
                dbc.Row(html.P("please stop")),
                ],
                style={"background-color": "black"},
                class_name="border",
                xs=12,
                md=3,
            ),
            dbc.Col(
                [content],
                style={"height": "100vh"},
                class_name="border",
                xs=12,
                md=9,
            ),
        ],
        class_name="g-0",
    )
]

app.layout = dbc.Container(
    id="root",
    children=page_structure,
    fluid=True,
    class_name="g-0",
)

if __name__ == "__main__":
    app.run(debug=True)
