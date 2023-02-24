from plotly import graph_objs as go
import pandas as pd

def make_table_graph_from_df(dataframe,title):
    fig = go.Figure(data=[go.Table(columnwidth = [10+len(column_name) for column_name in dataframe.columns],
        header=dict(values=list(dataframe.columns),
            fill_color="#121212",
            line_color="white",
            font = dict(color = 'white', size = 13),
            height=18,
                    align='left'),
        cells=dict(values=[list(dataframe[item]) for item in dataframe.columns],
            fill_color="#121212",
            line_color="white",
            font = dict(color = 'white', size = 13),
            height=18,
            align='left'))
    ])
    fig.update_layout(
        autosize=True,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=40,
            pad=0
        ),
        template="plotly_dark",
        title={
        "text":title,
        'y':0.98,
        'x':0.46,
        'xanchor': 'center',
        'yanchor': 'top'
        },
        legend_title="",
        # xaxis_title=None,
        # legend_traceorder="reversed",

    )



    return fig