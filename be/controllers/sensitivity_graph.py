import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from sample_data import type_list
def sensitivity_scatter_graph(df,prefix):
    """Create a scatter graph based on filtered data frame."""
    graph = go.Figure()
    for possibility in [""]+type_list:
        if possibility == prefix:
            visibility_hyst = True
            visibility_cyt=True
        # else:
        #     visibility_hyst = 'legendonly'
        #     visibility_cyt= False
            # cit=make_property_df(df,"cytology")
            # hist=make_property_df(df,"hystology")
            graph.add_trace(go.Scatter(x=df['day'], y= 0.8*df[prefix+"Positivecytology"], mode="markers+lines", name="Theoretical", showlegend=True, visible=visibility_cyt,fill="tonexty"))
            graph.add_trace(go.Scatter(x=df['day'], y= df[prefix+"Positivehystology"], mode="markers+lines", name="Real", showlegend=True, visible=visibility_hyst,fill="tonexty"))
    #data = df.loc[df['result'] == result]
    graph.update_layout(margin=go.layout.Margin(
    l=0, #left margin
    r=0, #right margin
    b=0, #bottom margin
    t=0, #top margin

    ),
    paper_bgcolor="#f5f3f4",
    plot_bgcolor="#f5f3f4",
    height=250,
    # title={
    #     'text': title,
    #     'y':0.99,
    #     'x':0.5,
    #     'xanchor': 'center',
    #     'yanchor': 'top',
    #     },
    font={
        #family="Courier New, monospace",
        'size':12,
        'color':"#343a40"
    }
    #title_text="Title"
    )
    return graph