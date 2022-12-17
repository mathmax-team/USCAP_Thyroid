# 1. Import Dash
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# 2. Create a Dash app instance
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
dropdown = dbc.DropdownMenu(color="warning",
    label="Pick a date",
    children=[
        dbc.DropdownMenuItem("Ayer"),
        dbc.DropdownMenuItem("Hoy"),
        dbc.DropdownMenuItem("Mañana"),
    ],
)
# 3. Add the example to the app's layout
# First we copy the snippet from the docs
badge = dbc.Button(
    [
        "Notifications",
        dbc.Badge("4", color="light", text_color="primary", className="ms-3"),
    ],
    color="success",

)
row_content = [
    dbc.Col(dcc.DatePickerRange(
                            id = 'date-range',
                            #start_date_placeholder_text = last_month_date,
                            #end_date = date.today(),
                            #max_date_allowed = date.today(),
                            #day_size=30,
                        style={"width":"8cm"}),width=4),
    dbc.Col(html.Div("Cytopathology Monitor",style={"font-size":"30px","color":"yellow"}), width=2),
    dbc.Col(
        [dbc.Row(html.Img(src="assets/medicine.svg",style={'height': '100px', "margin-top":"10px","margin-left":"30px"}),)],
        align="center"),
    dbc.Col(html.Div("Two of two columns",style={"margin-left":"50px"}),width=3),
    dbc.Col(dropdown,width=2)

]

row = html.Div(
    [
        dbc.Row(
            row_content,
            justify="start",
        ),

    ]
)


rownew = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
        dbc.Row(dbc.Col(html.Div("An automatically sized column"), width="auto")
        ),
        dbc.Row(
            [
                dbc.Col(dropdown, width=3),
                dbc.Col(html.Div("One of three columns"),width={"size": 2, "offset": 1}),
                dbc.Col(html.Div("One of three columns"), width=2),
            ]
        ),
    ]
)
breadcrumb = dbc.Breadcrumb(
    items=[
        {"label": "Docs", "href": "/docs", "external_link": True},
        {
            "label": "Components",
            "href": "/docs/components",
            "external_link": True,
        },
        {"label": "Breadcrumb", "active": True},
    ],
)
camilo=dbc.Col(html.Div("Camilo"))
# Then we incorporate the snippet into our layout.
# This example keeps it simple and just wraps it in a Container

app.layout = dbc.Container(row)
    #html.Div(
        #dbc.Row([dbc.Row(html.Div("camilo")),dbc.Row(html.Div("camilo",style={"color":"pink","font-size":"25px"}))]))#dbc.Container(dbc.Col(children=[dbc.Row(children=[camilo,badge,badge,badge]),badge,breadcrumb,dropdown,row,rownew]), fluid=True)
#)
# 5. Start the Dash server
if __name__ == "__main__":
    app.run_server(debug=True)





