import pandas as pd
from be.controllers.gap_minder_graph import make_gapminder
from be.controllers.default_times_ranges import df
from be.controllers.gap_minder_data import make_gap_minder_data


gap_minder_data=make_gap_minder_data(df)

new=pd.DataFrame(gap_minder_data.loc[10].to_dict(),index=[0])
new["Year"]=[2018]
gap_minder_data=pd.concat([gap_minder_data,new],ignore_index=True)


gap_movie=make_gapminder(gap_minder_data,"Call rate category III","Positive rate category III","Year","Pathologist","Case Count")