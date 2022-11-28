from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from datetime import date, timedelta
import pandas as pd
import numpy as np
import random
import math
import datetime
import plotly.graph_objects as go

days = 365
amplitude = 60
displacement = 0
noise = 0.4
day = date.today().day
month = date.today().month
year = date.today().year

if month == 1:
    year = year - 1
    month = 12

last_month_date = date(year, month -1, day) 
last_week_date = date.today() - timedelta(days = 7)
last_year_date = date.today() - timedelta(days = 365)

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def sin_data_generate(N,A,S,R):
    x = np.arange(0,N,1)
    noise = []
    for j in range(N):
        noise.append(R*random.choice(range(-3,3)))
    noise = np.array(noise)
    y = A*np.sin(30*x/(2*math.pi))+S
    y = y + noise
    return [x,y]

test_df = pd.DataFrame()
test_type = ['liquid based', 'conventional','another type']
adequacy_list = [{'satisfactory': 'Yes'},{'satisfactory': 'No', 'processed': 'Not processed'},{'satisfactory': 'No', 'processed': 'processed'}]
results_list = ['negative', 'ASC-US', 'ASC-H', 'LSIL', 'MSIL', 'SCC', 'AC']
for type in test_type:
    test_data = sin_data_generate(days, random.randint(1, 5), random.randint(0,20), noise)
    final = datetime.datetime.now()
    initial = final - datetime.timedelta(days=days-1)
    # print(initial, final)
    
    daterange = pd.date_range(initial, final, freq='D')

    test_df['day'] = daterange
    test_df[type] = test_data[1]
    test_df['adequacy'] = random.choices(adequacy_list, k=len(test_df))
    test_df['result'] = random.choices(results_list, k=len(test_df))

# print(test_df['result'].head(4))
# First Graph definition
# fig1 = px.line(test_df, x="day", y="number", color=test_type, symbol=test_type, title='Types', markers=True)
fig1 = go.Figure()
# Add traces
for test in test_type:
    fig1.add_trace(go.Scatter(x=test_df['day'], y=test_df[test],
                        mode='lines+markers',
                        name=test))
   

# Second Graph definition
tree_values = [100, 40, 60, 30, 30]
tree_labels = ["Satisfactory","Yes", "No", "Processed", "Not Processed"]
tree_parents = ["", "Satisfactory", "Satisfactory", "No", "No"]

fig2 = px.treemap()
fig2.update_layout(margin = dict(t=100, l=50, r=50, b=100))

# fig1.update_layout(
#     plot_bgcolor = colors["background"],
#     paper_bgcolor = colors["background"],
#     font_color = colors["text"]
# )


app.layout = html.Div(children=[
    html.Nav(children=[
        html.H2('Cytopathology')], style={'fontWeight': 'bold', 'textAlign': 'center', 'marginBottom': '20px', 'borderBottom': 'solid 1px black', 'backgroundColor': 'Black', 'color': 'white', 'height': '80px'}
        ),
    html.Div(children=[
        # Default time Ranges
        html.Label('Range: '),
        dcc.Dropdown(['last week', 'last month', 'last year'], 'last month', style={'width': '60%'}, id='default-time-ranges'),

        dcc.DatePickerRange(
            id = 'date-range',
            start_date_placeholder_text = last_month_date,
            end_date = date.today(),
            max_date_allowed = date.today()
        )

    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'width': '100%'}),
    html.Hr(),

    html.Div(children=[
        #First GRAPH
        html.Div(children=[
            html.H2('Types', style={'textAlign': 'center'}),
            dcc.Graph(
                id='types-graph',
                figure=fig1,
                config={
                    'staticPlot': False,     # True, False
                    'scrollZoom': False,      # True, False
                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                    'showTips': True,       # True, False
                    'displayModeBar': 'hover',  # True, False, 'hover'
                    'watermark': False,
                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                    },
            ),
            dcc.RadioItems(test_type, 
            value='liquid based',
            id = 'type-radio'
            ),
            html.Div(id='type-selected-graph'),
        ], style={'padding':'10px', 'border':'solid 1px black'}),

        #Second GRAPH
        html.Div(children=[
            html.H2('Adequacy', style={'textAlign': 'center'}),
            html.Label('Type: '),
            html.Div(id='type-selected'),
            dcc.Graph(
                id='tree-map',
                figure={},
                clickData={},
                config={
                    'staticPlot': False,     # True, False
                    'scrollZoom': True,      # True, False
                    'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                    'showTips': True,       # True, False
                    'displayModeBar': 'hover',  # True, False, 'hover'
                    'watermark': False,
                    # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                    },
            ),
        ], style={'padding':'10px', 'border':'solid 1px black'}),

        #Third GRAPH
        html.Div(children=[
            html.H2('Results', style={'textAlign': 'center'}),
            html.Div(id='adequacy-selected'),
            dcc.Graph(id='results-graph', figure={}, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': True,       # True, False
                      'displayModeBar': 'hover',  # True, False, 'hover'
                      'watermark': False,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },),
            dcc.Dropdown(results_list, 
            value='negative',
            id = 'selected-result'
            ),

        ], style={'padding':'10px', 'border':'solid 1px black'}),

        #Fourth GRAPH
        html.Div(children=[
            html.H2('MPV', style={'textAlign': 'center'}),
            html.Div(id='result-selected'),
            dcc.Graph(id='mpv-graph', figure={}, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': True,       # True, False
                      'displayModeBar': 'hover',  # True, False, 'hover'
                      'watermark': False,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },),
        ], style={'padding':'10px', 'border':'solid 1px black'}),
        
        #Fifth GRAPH
        html.Div(children=[
            html.H2('QC', style={'textAlign': 'center'}),
                dcc.Graph(id='qc-graph', figure={}, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': True,       # True, False
                      'displayModeBar': 'hover',  # True, False, 'hover'
                      'watermark': False,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },),
        ], style={'padding':'10px', 'border':'solid 1px black'}),
        
        html.Div('6', style={'padding':'10px', 'border':'solid 1px black'}),
    ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gridTemplateRows':'repeat(2, 1fr)','gridAutoFlow': 'column'}),

], style={'display': 'grid', 'margin': '20px'})

@app.callback(
    Output(component_id='types-graph', component_property='figure'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def filter_df_by_dates(start_date, end_date):
    filter_df = test_df[(test_df['day']>start_date) & (test_df['day']<end_date)]
    # print(start_date, end_date)
    fig = go.Figure()
    # Add traces
    for test in test_type:
        fig.add_trace(go.Scatter(x=filter_df['day'], y=filter_df[test],
                            mode='lines+markers',
                            name=test))
    return fig

@app.callback(
    Output(component_id= 'date-range', component_property='start_date'),
    Output(component_id= 'date-range', component_property='end_date'),
    Input(component_id='default-time-ranges', component_property='value')
)
def update_time_range(input_range):
    if input_range == 'last week':
        start_date = last_week_date
    elif input_range == 'last month':
        start_date =last_month_date
    elif input_range == 'last year':
        start_date = last_year_date
    end_date = date.today()
    return start_date, end_date


@app.callback(
    Output(component_id='type-selected', component_property='children'),
    Output('tree-map', 'figure'),
    Input(component_id='type-radio', component_property='value'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def update_tree_map(selected_type, start_date, end_date):
    filtered_df = test_df[(test_df['day']>start_date) & (test_df['day']<end_date)]
    count_df = pd.DataFrame()
    count_df['value'] = filtered_df[str(selected_type)]
    count_df['adequacy'] = filtered_df['adequacy']
    count = filtered_df[str(selected_type)].count()
    satisfactory_df = count_df[count_df['adequacy'] == {'satisfactory': 'Yes'}]
    satisfactory = satisfactory_df['value'].count()
    not_processed_df = count_df[count_df['adequacy'] == {'satisfactory': 'No', 'processed': 'Not processed'} ]
    not_processed = not_processed_df['value'].count()
    remainder_df = count_df[count_df['adequacy'] == {'satisfactory': 'No', 'processed': 'processed'} ]
    remainder = remainder_df['value'].count()
    not_satisfactory = not_processed + remainder
    tree_values = [count, 
                    satisfactory, 
                    not_satisfactory, 
                    not_processed, 
                    remainder]
    fig = px.treemap()
    fig.update_layout(margin = dict(t=100, l=50, r=50, b=100))
    fig.add_trace(go.Treemap(
        branchvalues = "total",
        labels = tree_labels,
        parents = tree_parents,
        values = tree_values,
        textinfo = "label+value",
        marker_colorscale = 'Blues'
    ),row = 1, col = 1)
    return f'{selected_type}', fig


@app.callback(
    Output(component_id='adequacy-selected', component_property='children'),
    Output(component_id='results-graph', component_property='figure'),
    Input(component_id='tree-map', component_property='clickData'),
    Input(component_id='type-radio', component_property='value'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def update_result_graph(click_data, type, start_date, end_date):
    filtered_result_df = test_df[(test_df['day']>start_date) & (test_df['day']<end_date)]
    message = ''
    processed = ''
    if click_data:
        clicked_data = click_data.get("points")
        label = clicked_data[0]["label"]
        print(f'label: {label}')
        print(f'type: {type}')
        match label:
            case 'Yes':
                filtered_result_df = filtered_result_df[filtered_result_df['adequacy'].isin([{'satisfactory': 'Yes'}])]
                message = 'Yes'
                processed = 'Yes'
            case 'No':
                filtered_result_df = filtered_result_df[filtered_result_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'},{'satisfactory': 'No', 'processed': 'processed'}])]
                message = 'No'
                processed = 'No'
            case 'Processed':
                filtered_result_df = filtered_result_df[filtered_result_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'processed'}])]
                message = 'No'
                processed = 'Yes'
            case 'Not Processed':
                message = 'No'
                processed = 'No'
                filtered_result_df = filtered_result_df[filtered_result_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'}])]
            case 'Satisfactory':
                message = 'All'
                processed = ''

    fig3 = go.Figure()
    # print(filtered_result_df.head())    
    for result in results_list:
        data = filtered_result_df[filtered_result_df['result'] == result]
        fig3.add_trace(go.Scatter(x=filtered_result_df["day"], y= data[type], mode="markers+lines", name=result,  ))
    # fig3 = px.line(filtered_result_df, x=filtered_result_df["day"], y=filtered_result_df[type], color=filtered_result_df["result"], symbol=filtered_result_df["result"])
    return f'Type: {type}, Adequacy: {message}, Processed: {processed}', fig3

@app.callback(
    Output(component_id='result-selected', component_property='children'),
    Output(component_id='mpv-graph', component_property='figure'),
    Input(component_id='tree-map', component_property='clickData'),
    Input(component_id='selected-result', component_property='value'),
    Input(component_id='type-radio', component_property='value'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def update_mpv_graph(click_data, result, type, start_date, end_date):
    filtered_df = test_df[(test_df['day']>start_date) & (test_df['day']<end_date)]
    if click_data:
        clicked_data = click_data.get("points")
        label = clicked_data[0]["label"]
        print(f'label: {label}')
        print(f'type: {type}')
        match label:
            case 'Yes':
                filtered_df = filtered_df[filtered_df['adequacy'].isin([{'satisfactory': 'Yes'}])]
            case 'No':
                filtered_df = filtered_df[filtered_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'},{'satisfactory': 'No', 'processed': 'processed'}])]
            case 'Processed':
                filtered_df = filtered_df[filtered_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'processed'}])]
            case 'Not Processed':
                filtered_df = filtered_df[filtered_df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'}])]

    filtered_df = filtered_df[filtered_df['result'] == result]
    print(filtered_df)
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=filtered_df['day'], y=filtered_df[type], mode='markers+lines', name=type))
    return f'{result}', fig4



if __name__ == '__main__':
    app.run_server(debug=True)