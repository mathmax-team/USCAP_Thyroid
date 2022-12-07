"""Creates and returns mvp graph."""
from sample_data import genotype_list
import plotly.graph_objects as go

def mvp_graph(df, type, result):
    """Create a scatter graph on filtered data frame."""
    data = df.loc[df['type'] == type]
    # data = df[df['result'] == result]
    data = data.loc[data['result'] == result]
    graph = go.Figure()
    for gn in genotype_list:
        data = df[df['mvp'] == gn]
        graph.add_trace(go.Scatter(x=df['day'], y=data['mvp'], mode='markers+lines', name=gn, showlegend=True))
    graph.update_layout(legend_title_text = "Genotype")
    graph.update_yaxes(title_text='number')
    return [graph, df]