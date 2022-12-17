"""Creates and returns adequacy tree_map graph."""
from sample_data import adequacy_list,tree_labels, tree_parents
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

paleta=["#FFC006","#95BFE1","#E83283","#42D7A7","#38CBFB"]
fig = px.treemap( width=400, height=200)
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))


def tree_map_graph(df, type, click_data):
    """Create a tree map based on filtered data frame."""
    count_df = pd.DataFrame()
    count_df = df[df['type'] == type]
    # count_df['adequacy'] = df['adequacy']
    count = len(count_df.index)
    print(f'columns: {count_df["adequacy"]}')
    # satisfactory_df = count_df.apply(lambda row: row[count_df['adequacy'].isin([{'satisfactory': 'Yes'}])])
    satisfactory_df = count_df[count_df['adequacy'] == str(adequacy_list[0])]
    satisfactory = len(satisfactory_df.index)
    not_processed_df = count_df[count_df['adequacy'] == str(adequacy_list[2])]
    not_processed = len(not_processed_df.index)
    remainder_df = count_df[count_df['adequacy'] == str(adequacy_list[1])]
    remainder = len(remainder_df.index)
    not_satisfactory = not_processed + remainder
    tree_values = [count,
                    satisfactory,
                    not_satisfactory,
                    not_processed,
                    remainder]

    # treemap figure
    adequacy_graph = px.treemap(width=250,height=150)
    adequacy_graph.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    adequacy_graph.add_trace(go.Treemap(
        branchvalues = "total",
        labels = tree_labels,
        parents = tree_parents,
        values = tree_values,
        textinfo = "label+value",
        marker_colorscale = paleta
    ),row = 1, col = 1)

    message = ''
    processed = ''
    if click_data:
        clicked_data = click_data.get("points")
        label = clicked_data[0]["label"]
        match label:
            case 'Yes':
                count_df = count_df[count_df['adequacy'] == str(adequacy_list[0])]
                message = 'Yes'
                processed = 'Yes'
            case 'No':
                count_df = count_df[(count_df['adequacy'] == str(adequacy_list[2])) | (count_df['adequacy'] == str(adequacy_list[1]))]
                message = 'No'
                processed = '-'
            case 'Processed':
                count_df = count_df[count_df['adequacy'] == str(adequacy_list[2])]
                message = 'No'
                processed = 'Yes'
            case 'Not Processed':
                message = 'No'
                processed = 'Not processed'
                count_df = count_df[count_df['adequacy'] == str(adequacy_list[1])]
            case 'Satisfactory':
                message = 'All'
                processed = '-'
                count_df = df[df['type'] == type]

    return [adequacy_graph, message, processed, count_df]
