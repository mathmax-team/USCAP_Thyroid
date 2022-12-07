"""Use to filter datframe based on start_date and end_date."""

def filter_dataframe(df, start_date, end_date):
    """Filter a datframe based on to dates."""
    filtered_df= df[(df['day']>=start_date) & (df['day']<=end_date)]
    return filtered_df