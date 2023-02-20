import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def make_pie(names,values,title):
    # fig = px.pie( names=names,values=values, sort=False)
    fig = go.Figure(
    data=[go.Pie(
        labels=names,
        values=values,
        # Second, make sure that Plotly won't reorder your data while plotting
        sort=False)
    ])
    fig.update_layout(
        autosize=False,
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
        # legend_traceorder="reversed",

    )

    return fig