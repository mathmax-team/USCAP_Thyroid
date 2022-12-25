"""Creates and returns results graph."""
from sample_data import results_list,type_list,genotype_list
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def scatter_graph(df,choice,possibilities):
    """Create a scatter graph based on filtered data frame."""
    paleta=(["#FFC006","#95BFE1","#E83283","#42D7A7","#38CBFB","#d6e649","#f230a1","#30bff2","#f24730","#8c7649","#498c6f","#74678f"])
    cosas=["All"]+type_list+genotype_list+results_list
    color=dict()
    for i in range(len(cosas)):
        color[cosas[i]]=paleta[i%len(paleta)]
    graph = go.Figure()
    count=0
    for possibility in possibilities:
        if possibility == choice:
            visibility = True
        else:
            visibility = 'legendonly'
        graph.add_trace(go.Scatter(x=df['day'], y= df[possibility], mode="markers+lines", name=possibility, showlegend=True, visible=visibility,fill="tonexty",line=dict(color=color[possibility])))
        count=count+1
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