import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



def make_pie(dataframe,names,values,title):
    fig=px.pie(dataframe, values=values, names=names,
             color_discrete_sequence=px.colors.qualitative.T10


    )

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
        'x':0.50,
        'xanchor': 'center',
        'yanchor': 'top'
        },

    )
    fig.update_traces(sort=False)

    return fig