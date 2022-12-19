"""Creates and returns types graph."""
from sample_data import test_type
import plotly.graph_objects as go
import pandas as pd

def types_graph(df, type):
    """Create a scatter graph on filtered data frame."""
    graph = go.Figure()
    count = 0

    for test in test_type:
        if test == type:
            visibility = True
        else:
            visibility = 'legendonly'

        graph.add_trace(go.Scatter(x=df['day'], y=df[test], mode='lines+markers', name=test, cliponaxis=True,
        line_shape= "spline", showlegend=True, line_smoothing=1, marker_symbol=count, visible=visibility, fill='tonexty'
        ))
        count += 1
    graph.update_layout(legend_title_text = "Type")
    graph.update_yaxes(title_text='Daily tests')
    graph.update_xaxes(title_text='Day')
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
    # graph.update_layout(plot_bgcolor='white')
    # graph.update_layout(colorway=['red'])
    # graph.update_layout(paper_bgcolor='black')
    return graph
