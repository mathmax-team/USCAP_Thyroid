import pandas as pd
from be.controllers.gap_minder_graph import make_gapminder
dfLarge=pd.read_csv("data/USCAP_Large.csv")
gap_pathologists=[pathologist for pathologist in list(dfLarge["CYTOPATHOLOGIST"].unique()) if dfLarge[dfLarge["CYTOPATHOLOGIST"]==pathologist].shape[0]>200]

gap_pathologists=["Pathologist "+ str(pathologist) for pathologist in sorted(gap_pathologists)]

years=list(dfLarge["YEAR"].unique())
gap_minder_data=pd.DataFrame()
for year in years:
    for pathologist in gap_pathologists:
        new_row=dict()
        size=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]==year)].shape[0]

        calls_CatIII=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]
        ==year)&(dfLarge["Bethesda Cathegory"]==3)].shape[0]
        if calls_CatIII>0:
            call_rate_CatIII=calls_CatIII/size

            positive_rate_CatIII=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]
            ==year)&(dfLarge["Bethesda Cathegory"]==3)&(dfLarge["RESULT"]=="POSITIVE")].shape[0]/calls_CatIII
            new_row["Pathologist"]=[pathologist]
            new_row["Year"]=[year]
            new_row["Case Count"]=[size]
            new_row["Call rate category III"]=[call_rate_CatIII]
            new_row["Positive rate category III"]=[positive_rate_CatIII]
            new_row=pd.DataFrame.from_dict(new_row)


            gap_minder_data=pd.concat([gap_minder_data,new_row])
gap_movie=make_gapminder(gap_minder_data,"Call rate category III","Positive rate category III","Year","Pathologist","Case Count","Pathologist","Pathologist")