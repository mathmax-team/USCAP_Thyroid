import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def make_gene(data_frame,labels_column,values_column,title):
    fig = px.bar( data_frame,x=labels_column, y=values_column, title="Wide-Form Input",color=labels_column,
     color_discrete_sequence=px.colors.qualitative.Light24
    )
    fig.update_xaxes(visible=False, showticklabels=False)
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
            xaxis_title=None,
            # legend_traceorder="reversed",

        )
    return fig