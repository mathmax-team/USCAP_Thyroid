"""Creates and returns results graph."""
from sample_data import results_list, test_type
import plotly.graph_objects as go
import pandas as pd

def result_graph(df, type, result):
    """Create a scatter graph based on filtered data frame."""
    graph = go.Figure()
    count = 0
    data = df.loc[df['type'] == type]
    for item in results_list:
        count += 1
        temp_df = data.loc[data['result'] == item]
        day_group = temp_df.groupby('day')
        graph_df = pd.DataFrame()
        graph_df['count'] = day_group['result'].count()
        graph_df = graph_df.reset_index()

        if item == result:
            visibility = True
        else:
            visibility = 'legendonly'


        graph.add_trace(go.Scatter(x=graph_df['day'], y= graph_df['count'], mode="markers+lines", name=item, marker_symbol= count, showlegend=True, visible=visibility))
    return [graph, data]
