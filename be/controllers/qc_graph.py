"""Creates and returns qc graph."""
from sample_data import choices
import plotly.graph_objects as go
import pandas as pd

def qc_graph(df, type, result, genotype):
    """Create a scatter graph on filtered data frame."""
    count = 0
    graph = go.Figure()
    # df = df[df['mvp'] == genotype]
    data = df.loc[df['type'] == type]
    data = data.loc[data['result'] == result]
    data = data.loc[data['mvp'] == int(genotype)]

    positive = data[data['cytology'] == 'positive']

    positive_day_group = positive.groupby('day')
    graph_df = pd.DataFrame()
    graph_df['count'] = positive_day_group['cytology'].count()
    graph_df = graph_df.reset_index()



    #print(positive)
    graph.add_trace(go.Scatter(x=graph_df['day'], y=graph_df['count'], marker_symbol= count, mode='markers+lines', name='positive_cytology', showlegend=True))

    for qc_result in choices:
        count += 1
        test_data = data[data['test_quality'] == qc_result]
        if not test_data.empty:
            day_group = test_data.groupby('day')
            dataframe = pd.DataFrame()
            dataframe['count'] = day_group['cytology'].count()
            dataframe = dataframe.reset_index()


            graph.add_trace(go.Scatter(x=dataframe['day'], y=dataframe['count'], marker_symbol= count, mode='markers+lines', name=qc_result, showlegend=True, fill=None))
            graph.update_layout(legend_title_text = "Combinations")
            graph.update_yaxes(title_text='number')
            graph.update_layout(margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin

    ),
    #paper_bgcolor="#293241",
    paper_bgcolor="#f5f3f4",
    plot_bgcolor="#f5f3f4",
    height=300,
    width=650

    )


    return graph