import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from sample_data import type_list
def sensitivity_scatter_graph(sensitivity_dict):
    """Create a scatter graph based on filtered data frame."""
    my_green="#42D7A7"
    my_orange="#FFC006"
    graph = go.Figure()
    graph.add_trace(go.Scatter(x=sensitivity_dict["Theoretical"]['x'], y= 0.8*sensitivity_dict["Theoretical"]["y"],
            mode="markers+lines", name="Theoretical", showlegend=True,fill="tonexty",marker=dict(color=my_orange)))
    graph.add_trace(go.Scatter(x=sensitivity_dict["Real Sensitivity"]['x'], y= sensitivity_dict["Real Sensitivity"]["y"],
            mode="markers+lines", name="Real Sensitivity", showlegend=True,fill="tonexty",marker=dict(color=my_green)))
    graph.update_layout(margin=go.layout.Margin(
    l=0, #left margin
    r=0, #right margin
    b=0, #bottom margin
    t=0, #top margin

    ),
    template="plotly_dark",
    plot_bgcolor= 'rgba(0, 0, 0, 0)',
    paper_bgcolor= 'rgba(0, 0, 0, 0)',
    height=200,
    )
    return graph