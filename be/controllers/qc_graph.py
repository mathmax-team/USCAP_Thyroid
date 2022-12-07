"""Creates and returns qc graph."""
from sample_data import choices
import plotly.graph_objects as go

def qc_graph(df, type, genotype):
    """Create a scatter graph on filtered data frame."""
    graph = go.Figure()
    df = df[df['mvp'] == genotype]
    count = 0
    positive = df[df['cytology'] == 'positive']
    print(positive)
    graph.add_trace(go.Scatter(x=positive['day'], y=positive[type], marker_symbol= count, mode='markers+lines', name='positive_cytology', showlegend=True))
    for qc_result in choices:
        count += 1
        data = df[df['test_quality'] == qc_result]
        graph.add_trace(go.Scatter(x=data['day'], y=data[type], marker_symbol= count, mode='markers+lines', name=qc_result, showlegend=True, fill='tonexty'))
        graph.update_layout(legend_title_text = "Combinations")
        graph.update_yaxes(title_text='number')
    return graph