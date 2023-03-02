import pandas as pd
from be.controllers.default_times_ranges import years,pathologists


def make_gap_minder_data(dataframe):
    gap_minder_data=pd.DataFrame()
    for year in years:
        for pathologist in pathologists:
            new_row=dict()
            size=dataframe[(dataframe["CYTOPATHOLOGIST"]==pathologist)&(dataframe["YEAR"]==year)].shape[0]

            calls_CatIII=dataframe[(dataframe["CYTOPATHOLOGIST"]==pathologist)&(dataframe["YEAR"]
            ==year)&(dataframe["Bethesda Cathegory"]==3)].shape[0]
            if calls_CatIII>0:
                call_rate_CatIII=calls_CatIII/size

                positive_rate_CatIII=dataframe[(dataframe["CYTOPATHOLOGIST"]==pathologist)&(dataframe["YEAR"]
                ==year)&(dataframe["Bethesda Cathegory"]==3)&(dataframe["RESULT"]=="POSITIVE")].shape[0]/calls_CatIII
                new_row["Pathologist"]=[pathologist]
                new_row["Year"]=[year]
                new_row["Case Count"]=[size]
                new_row["Call rate category III"]=[call_rate_CatIII]
                new_row["Positive rate category III"]=[positive_rate_CatIII]
                new_row=pd.DataFrame.from_dict(new_row)
                gap_minder_data=pd.concat([gap_minder_data,new_row])
    for year in years:
        new_row=dict()
        size=dataframe[(dataframe["YEAR"]==year)].shape[0]

        calls_CatIII=dataframe[(dataframe["YEAR"]
        ==year)&(dataframe["Bethesda Cathegory"]==3)].shape[0]
        if calls_CatIII>0:
            call_rate_CatIII=calls_CatIII/size

            positive_rate_CatIII=dataframe[(dataframe["YEAR"]
            ==year)&(dataframe["Bethesda Cathegory"]==3)&(dataframe["RESULT"]=="POSITIVE")].shape[0]/calls_CatIII
            new_row["Pathologist"]=["All pathologists"]
            new_row["Year"]=[year]
            new_row["Case Count"]=[size]
            new_row["Call rate category III"]=[call_rate_CatIII]
            new_row["Positive rate category III"]=[positive_rate_CatIII]
            new_row=pd.DataFrame.from_dict(new_row)
            gap_minder_data=pd.concat([gap_minder_data,new_row])
    return gap_minder_data