"""Use to filter datframe based on start_date and end_date."""
import pandas as pd
from sample_data import week_day

def filter_dataframe(df, start_date, end_date):
    """Filter a datframe based on to dates."""
    filtered_df= df[(df['day']>=start_date) & (df['day']<=end_date)]
    return filtered_df

def new_row_by_column(df,fecha,column):
    column_values=list(df[column].unique())
    new_row_in={"day":fecha}
    df_prop=df[df["day"]==fecha]
    new_row_in["All "+column+ "s"]=df_prop.shape[0]
    for tipo in column_values:
        temp_df=df_prop[df_prop[column]==tipo]
        new_row_in[tipo]=temp_df.shape[0]
    # new_row_in["weekday"]=week_day(fecha.weekday())
    return pd.DataFrame([new_row_in])

def make_property_df(df,column):
    fechas=df["day"].unique()
    possibilities=list(df[column].unique())
    df_columns=["day","All "+column+"s"]+possibilities+["weekday"]
    prop_df=pd.DataFrame(columns=df_columns)
    for fecha in fechas:
        prop_df=pd.concat([prop_df,new_row_by_column(df,fecha,column)],axis=0, ignore_index=True)

    return prop_df