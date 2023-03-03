

import plotly.express as px
import pandas as pd
# import numpy as np
import plotly.graph_objects as go


def make_CatIII_Call_Rate_time(
        dataframe):
    """Create a plot given dictionary  whose keys are the six Bethesda Categories and values are dataframes of count by year."""


        # graph.add_trace(go.Scatter(x=possibilities[possibility]["x"], y= possibilities[possibility]["y"],mode="markers+lines", name=possibility, showlegend=True, visible=True,fill=None,line=dict(color=paleta[count%N])))
    graph=px.line(dataframe,x="Year", y="Cat III Call Rate",color="Pathologist",markers=True, color_discrete_sequence=px.colors.qualitative.T10)
    # graph=px.line(x=[2,4],y=[3,4])

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
                "text":"Category III Call Rate Over Time",
                'y':0.98,
                'x':0.46,
                'xanchor': 'center',
                'yanchor': 'top'
                },
                # legend_title="Category",
                xaxis_title="Year",
                yaxis_title="Cat III Call Rate",

            )
    return graph