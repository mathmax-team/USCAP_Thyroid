import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def make_stacked_bar(data_frame,labels_column,values_column,title,yaxislabel):
    feg = px.bar( data_frame,x=labels_column, y=values_column, title="Wide-Form Input",
    color_discrete_sequence=px.colors.qualitative.T10
    # color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta","orange"]
    )
    feg.update_layout(
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
            xaxis_title=None,
            yaxis_title=yaxislabel
            # legend_traceorder="reversed",

        )
    return feg