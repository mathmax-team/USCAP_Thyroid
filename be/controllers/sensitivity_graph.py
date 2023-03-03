import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
#from sample_data import type_list
def sensitivity_scatter_graph(sensitivity_dict):
    """Create a scatter graph based on filtered data frame."""
    my_green="#42D7A7"
    my_orange="#FFC006"
    colors=[my_orange,my_green]
    graph = go.Figure()
    count=0
    for key in list(sensitivity_dict.keys()):
        graph.add_trace(go.Scatter(x=sensitivity_dict[key]['x'], y= sensitivity_dict[key]["y"],
            mode="markers+lines", name=key, showlegend=True,fill=None,marker=dict(color=colors[count%2])))
        count=count + 1

#     graph.add_trace(go.Scatter(x=sensitivity_dict["Positive histology"]['x'], y= sensitivity_dict["Posi"]["y"],
#             mode="markers+lines", name="Real Sensitivity", showlegend=True,fill=None,marker=dict(color=my_green)))
    graph.update_layout(margin=go.layout.Margin(
    l=0, #left margin
    r=0, #right margin
    b=0, #bottom margin
    t=0, #top margin
    ),
    template="plotly_dark",
    plot_bgcolor= 'rgba(0, 0, 0, 0)',
    paper_bgcolor= 'rgba(0, 0, 0, 0)',
    height=250,
    legend=dict(yanchor="top", y=-0.2, xanchor="left", x=0),
    title="Cytohistological correlation",
    title_x=0.2,
    title_y=0.99,
    title_font_size=14,
    )

    #)
    return graph