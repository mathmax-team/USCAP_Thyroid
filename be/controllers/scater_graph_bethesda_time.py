

import plotly.express as px
import pandas as pd
# import numpy as np
import plotly.graph_objects as go


def make_scatter_graph_time_bethesda(
        possibilities:dict):
    """Create a plot given dictionary  whose keys are the six Bethesda Categories and values are dataframes of count by year."""
    paleta=px.colors.qualitative.T10
    N=len(paleta)
    graph = go.Figure()
    count=0
    for possibility in list(possibilities.keys()):

        graph.add_trace(go.Scatter(x=possibilities[possibility]["x"], y= possibilities[possibility]["y"],mode="markers+lines", name=possibility, showlegend=True, visible=True,fill=None,line=dict(color=paleta[count%N])))
        count=count+1
    graph.update_layout(
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
                "text":"Bethesda Category Count Over Time",
                'y':0.98,
                'x':0.46,
                'xanchor': 'center',
                'yanchor': 'top'
                },
                # legend_title="Category",
                xaxis_title="Year",
                yaxis_title="Count",

            )
    return graph