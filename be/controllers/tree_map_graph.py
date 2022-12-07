"""Creates and returns adequacy tree_map graph."""
from sample_data import test_type, initial_df, adequacy_list
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# # Second Graph definition
tree_values = [100, 40, 60, 30, 30]
tree_labels = ["Satisfactory","Yes", "No", "Processed", "Not Processed"]
tree_parents = ["", "Satisfactory", "Satisfactory", "No", "No"]

fig = px.treemap()
fig.update_layout(margin = dict(t=100, l=50, r=50, b=100))


def tree_map_graph(df, type, click_data):
    """Create a tree map based on filtered data frame."""
    count_df = pd.DataFrame()
    count_df = df[df['type'] == type]
    # count_df['adequacy'] = df['adequacy']
    count = len(count_df.index)
    print(f'columns: {count_df["adequacy"]}')
    # satisfactory_df = count_df.apply(lambda row: row[count_df['adequacy'].isin([{'satisfactory': 'Yes'}])])
    satisfactory_df = count_df[count_df['adequacy'] == (adequacy_list[0])]
    satisfactory = len(satisfactory_df.index)
    not_processed_df = count_df[count_df['adequacy'] == {'satisfactory':'No', 'processed':'processed'}]
    not_processed = len(not_processed_df.index)
    remainder_df = count_df[count_df['adequacy'] == {'satisfactory':'No', 'processed':'Not processed'}]
    remainder = len(remainder_df.index)
    not_satisfactory = not_processed + remainder
    tree_values = [count,
                    satisfactory,
                    not_satisfactory,
                    not_processed,
                    remainder]

    # treemap figure
    adequacy_graph = px.treemap()
    adequacy_graph.update_layout(margin = dict(t=100, l=50, r=50, b=100))
    adequacy_graph.add_trace(go.Treemap(
        branchvalues = "total",
        labels = tree_labels,
        parents = tree_parents,
        values = tree_values,
        textinfo = "label+value",
        marker_colorscale = 'Blues'
    ),row = 1, col = 1)

    message = ''
    processed = ''
    if click_data:
        clicked_data = click_data.get("points")
        label = clicked_data[0]["label"]
        match label:
            case 'Yes':
                df = df[df['adequacy'].isin([{'satisfactory': 'Yes'}])]
                message = 'Yes'
                processed = 'Yes'
            case 'No':
                df = df[df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'},{'satisfactory': 'No', 'processed': 'processed'}])]
                message = 'No'
                processed = '-'
            case 'Processed':
                df = df[df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'processed'}])]
                message = 'No'
                processed = 'Yes'
            case 'Not Processed':
                message = 'No'
                processed = 'Not processed'
                df = df[df['adequacy'].isin([{'satisfactory': 'No', 'processed': 'Not processed'}])]
            case 'Satisfactory':
                message = 'All'
                processed = '-'

    return [adequacy_graph, message, processed, df]
