"""Creates and returns results graph."""
from sample_data import results_list, test_type
import plotly.graph_objects as go
import pandas as pd

def result_graph(df,result):
    """Create a scatter graph based on filtered data frame."""
    graph = go.Figure()
    count = 0
    for item in results_list:
        count += 1
        if item=="All results":
            temp_df=df
        else:
            temp_df = df.loc[df['result'] == item]
        if not temp_df.empty:
            day_group = temp_df.groupby('day')
            graph_df = pd.DataFrame()
            graph_df['count'] = day_group['result'].count()
            graph_df = graph_df.reset_index()
            if item == result:
                visibility = True
            else:
                visibility = 'legendonly'
            graph.add_trace(go.Scatter(x=graph_df['day'], y= graph_df['count'], mode="markers+lines", name=item, marker_symbol= count, showlegend=True, visible=visibility,fill="tonexty"))
    data = df.loc[df['result'] == result]
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
    return [graph, data]
