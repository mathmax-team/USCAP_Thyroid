
from datetime import date,timedelta
import pandas as pd


df=pd.read_csv("data/USCAP_Large.csv")
for col in ["ACCESS_DATE","SIGN_DATE"]:
    df[col]=df[col].apply(lambda z:pd.Timestamp(z))
################################################RENAME PATHOLOGISTS
df["CYTOPATHOLOGIST"]=df["CYTOPATHOLOGIST"].apply(lambda z: "Pathologist " + str(int(z)) if(str(z) != 'nan') else z)
###################################### LIST OF PATHOLOGISTS

pathologists=df["CYTOPATHOLOGIST"].tolist()
pathologists=[x for x in pathologists if str(x) !="nan"]
#pathologists=list(map(lambda z:int(z),pathologists))
pathologists=list(set(pathologists))

pathologists=[x for x in pathologists if df[df["CYTOPATHOLOGIST"]==x].shape[0]>=200]

pathologists=sorted(pathologists,key=lambda z: eval(z[11:]))
df=df[df["CYTOPATHOLOGIST"].isin(pathologists)]


first_day=min(df["SIGN_DATE"].to_list())
last_day=max(df["SIGN_DATE"].to_list())

yearsa=34553
years=list(df["YEAR"].unique())


Default_time_ranges=dict()

Default_time_ranges["Historical"]=[first_day,date.today()]
Default_time_ranges["2022"]=[date(2022,1,1),date(2022,12,31)]
Default_time_ranges["2021"]=[date(2021,1,1),date(2021,12,31)]
Default_time_ranges["2020"]=[date(2020,1,1),date(2020,12,31)]
Default_time_ranges["2019"]=[date(2019,1,1),date(2019,12,31)]
Default_time_ranges["2018"]=[date(2018,1,1),date(2018,12,31)]
# Default_time_ranges["Last year"]=[date.today().replace(day=1,month=1,year=date.today().year-1),date.today().replace(day=31,month=12,year=date.today().year-1)]
# Default_time_ranges["Current month"]=[date.today().replace(day=1),date.today()]
# Default_time_ranges["Current year"]=[date.today().replace(day=1,month=1),date.today()]
