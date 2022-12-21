"""Creates and returns results graph."""
from sample_data import results_list, test_type
import plotly.graph_objects as go
import pandas as pd

def scatter_graph(df,choice):
    """Create a scatter graph based on filtered data frame."""
    graph = go.Figure()
    for possibility in df.columns:
        if possibility not in ["day","weekday"]:
            if possibility == choice:
                visibility = True
            else:
                visibility = 'legendonly'
            graph.add_trace(go.Scatter(x=df['day'], y= df[possibility], mode="markers+lines", name=possibility, showlegend=True, visible=visibility,fill="tonexty"))
    #data = df.loc[df['result'] == result]
    graph.update_layout(margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin

    ),
    paper_bgcolor="#f5f3f4",
    plot_bgcolor="#f5f3f4",
    height=300,
    #width=650
    )
    return graph