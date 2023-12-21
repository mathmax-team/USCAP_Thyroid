# Import necessary libraries
import dash
from dash import html, dcc, callback,no_update,dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output,State
from datetime import date,timedelta
import pandas as pd
#from plotly.subplots import make_subplots
from be.controllers.pie_chart import make_pie
from be.controllers.roman import make_roman
# from be.controllers.bar_chart import make_bar
# from be.controllers.ROM_chart import make_rom
from be.controllers.Gene_mutated import make_gene
# from be.controllers.table_chart import make_table_graph
from be.controllers.stacked_bar_graph import make_stacked_bar
from be.controllers.counters import count_by_result,count_cases,count_categories,count_result_by_category
from be.controllers.CatIII_Call_Rate_over_time import make_CatIII_Call_Rate_time
# from be.controllers.make_table_graph_from_df import make_table_graph_from_df
from be.controllers.ages_graph import make_ages_graph
from be.controllers.scater_graph_bethesda_time import make_scatter_graph_time_bethesda
# from be.controllers.gap_minder_graph import make_gapminder
from be.controllers.movie import gap_movie
from be.controllers.tab_names import Movie,Overall,ComparingCP
from be.controllers.gap_minder_data import make_gap_minder_data
from be.controllers.empty_figure import empty_fig
from be.controllers.scat_callrate_vs_positiverate import scat_callrate_vs_positive
# from be.controllers.molecular_overview_graph import make_molecular_overview
from be.controllers.default_times_ranges import Default_time_ranges,first_day,last_day,df,pathologists,years
import numpy as np
##################################################


############################## SOME INFO FROM DATA FRAME

# df=pd.read_csv("data/USCAP_Large.csv")
# for col in ["ACCESS_DATE","SIGN_DATE"]:
#     df[col]=df[col].apply(lambda z:pd.Timestamp(z))

# first_day=min(df["SIGN_DATE"].to_list())
# last_day=max(df["SIGN_DATE"].to_list())
############DICTIONARY FOR DEFAULT TIME RANGES
##################################################

# Default_time_ranges=dict()
# Default_time_ranges["Historical"]=[first_day,last_day]

# Default_time_ranges["Last year"]=[date.today().replace(day=1,month=1,year=date.today().year-1),date.today().replace(day=31,month=12,year=date.today().year-1)]

# Default_time_ranges["Current month"]=[date.today().replace(day=1),date.today()]
# Default_time_ranges["Current year"]=[date.today().replace(day=1,month=1),date.today()]



################################################RENAME PATHOLOGISTS
# df["CYTOPATHOLOGIST"]=df["CYTOPATHOLOGIST"].apply(lambda z: "Pathologist " + str(int(z)) if(str(z) != 'nan') else z)
# ###################################### LIST OF PATHOLOGISTS

# pathologists=df["CYTOPATHOLOGIST"].tolist()
# pathologists=[x for x in pathologists if str(x) !="nan"]
# #pathologists=list(map(lambda z:int(z),pathologists))
# pathologists=list(set(pathologists))

# pathologists=[x for x in pathologists if df[df["CYTOPATHOLOGIST"]==x].shape[0]>=200]

# pathologists=sorted(pathologists,key=lambda z: eval(z[11:]))
# df=df[df["CYTOPATHOLOGIST"].isin(pathologists)]
# pathologists=+pathologists

##########################
#########   TABLE I
##########################
x=str(last_day)

table_headerI = [
    html.Thead(html.Tr([html.Th("Tests"),html.Th("Molecular Tests"),html.Th("+ Tests")]))
]

row1I = html.Tr([html.Td("345",id="id_tests"), html.Td("45.6",id="id_molecular_tests"),html.Td("---",id="id_positive_tests")])


table_bodyI = [html.Tbody([row1I])]

tableI = dbc.Table(table_headerI + table_bodyI, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"0px"})

################# TABLE II

table_headerII = [
    html.Thead(html.Tr([html.Th("Currently -"),html.Th("Cat III"),html.Th("Cat IV")]))
]

row1II = html.Tr([html.Td("0",id="id_currently-"),html.Td("345",id="id_catIII_tests"), html.Td("0",id="id_catIV_tests")])


table_bodyII = [html.Tbody([row1II])]

tableII = dbc.Table(table_headerII + table_bodyII, bordered=True,style={"width":"100%","height":"20px","margin-bottom":"0px"})



############################# TABS
# header_tabs=dbc.Tabs(id="id_tabs",
#                         children=[
#                         dbc.Tab( label="Overall Information",tab_id="Overall"),
#                         dbc.Tab( label="Mutations by Category",tab_id="Mutations by Category"),
#                         dbc.Tab(label="Mutations by Result",tab_id="Mutations by Result"),
#                         dbc.Tab(label="ROM",tab_id="ROM"),
#                         ]
#                             )

##############################
# def oldmake_drop(lista:list,id:str):
#     menu=dcc.Dropdown(id=id,
#     options=[ {"label": html.Span([i],style={"color":"yellow"}), "value": i} for i in lista],
#     value=lista[-1],
#     clearable=False,
#     style={"color":"red",}

#         )
#     return {"drop":menu}

############################################################
def make_drop(lista:list,id:str):
    menu=dcc.Dropdown(
    lista,
    lista[0],
    id=id,
    maxHeight=300,
    clearable=False,
        )
    return menu


###################  GENERATE THE DROPDOWN ELEMENTS  #######################

time_period_choice=make_drop(list(Default_time_ranges.keys()),"id_time_period_choice")
sex_choice=make_drop(["All sexes","Female","Male"],"id_sex_choice")
responsable_choice=make_drop(["All pathologists"]+pathologists,"id_responsable_choice")
ages=["All ages","Less than 40","40 to 49","50 to 59","60 to 69","70 or older"]
age_choice=make_drop(ages,"id_age_choice")

newdrop=dcc.Dropdown(
    [
        {
            "label": html.Span(['Montreal'], style={'color': 'Gold', 'font-size': 20}),
            "value": "MTL",
            "search": "Montreal"
        },
        {
            "label": html.Span(['New York City'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            "value": "NYC",
            "search": "New York City"
        },
        {
            "label": html.Span(['London'], style={'color': 'LightGreen', 'font-size': 20}),
            "value": "LON",
            "search": "London"
        },
    ], value='Montreal',
)

dropletter=make_drop(['Last year','Last month','Last week','All time'],"dropletter")


choices=dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Math"),
        dbc.DropdownMenuItem("Physics"),
        # dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Computing"),
    ],
    # nav=True,
    # in_navbar=True,
    label="Menu",
)

# fig = go.Figure()
# fig.update_layout(
#     autosize=False,
#     # width=470,
#     # height=300,
#     margin=dict(
#         l=0,
#         r=0,
#         b=0,
#         t=0,
#         pad=0
#     ),
#     template="plotly_dark",
#     paper_bgcolor=" rgb(18, 18, 18)",
#     plot_bgcolor=" rgb(18, 18, 18)"
# )
def make_card(id):
    card = dbc.Card(
        dbc.CardBody(
            [dcc.Graph(id=id,
        figure=empty_fig(),
    # style={"height":"100%"},
    config={
                            'displayModeBar': False
                        },style={"height":"35vh"})
                # html.H4("Title", id="card-title"),
                # html.H2("100", id="card-value"),
                # html.P("Description", id="card-description")
            ]
        )
    ,style={"width":"30vw","height":"35vh"," background-color":"rgb(18, 18, 18)"},
    )
    return card

content= [
                    html.Div([
                    dbc.Row([
                        dbc.Col(make_card("id_first_graph")), dbc.Col([make_card("id_second_graph")])
                    ]),
                    dbc.Row([
                        dbc.Col([make_card("id_third_graph")]), dbc.Col([make_card("id_fourth_graph")]),
                    ]),
                ])
                    ]
short_content=html.Div([
    html.P("",style={"height":"150px"}),
    dcc.Graph(
        figure=gap_movie,
        # style={"height":"100%"},
        config={
                            'displayModeBar': False
                        },id="id_movie_content",style={"margin-top":"200px"})
]
)
# smallcard = dbc.Card(
#     dbc.CardBody(
#         [table,
#             # html.H4("Title", id="card-title"),
#             # html.H2("100", id="card-value"),
#             # html.P("Description", id="card-description")
#         ]
#     )
# ,style={"height":"20vh","background-color":"#8af2a6","margin-top":"40px"})

tab1_content = dbc.Card(
    dbc.CardBody(
        # [
        #     html.P("This is tab 1!", className="card-text"),
        #     dbc.Button("Click here", color="success"),
        # ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        # [
        #     html.P("This is tab 2!", className="card-text"),
        #     dbc.Button("Don't click here", color="danger"),
        # ]
    ),
    className="mt-3",
)

layout = html.Div([
    html.Div(
     children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="three columns div-user-controls",
                    children=[

                    html.Div(className="div_for_text",
                    children=[html.H5("Cytopathology Monitor")
                    ]),
                    html.Div(className="div_for_text",
                        children=[html.P("Default time periods")],style={"height":"25px"}),

                        # className="row",
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            time_period_choice
                        ],
                    ),
                    html.Div(className="div_for_text",
                        children=[html.P("Custom time period")],style={"height":"25px"}),
                    html.Div(
                    className="div-for-dropdown",
                    children=[
                        dcc.DatePickerRange(
                            id = 'id_date_range',
                            # style={"width":"100%"}
                                )
                    ],
                ),
                html.Div(className="div_for_text",
                        children=[html.P("Filter by pathologist")],style={"height":"25px"}),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                            responsable_choice
                        ],
                    ),
                html.Div(className="div_for_text",
                        children=[html.P("Filter by age")],style={"height":"25px"}),
                    html.Div(
                        className="div-for-dropdown",
                        children=[
                           age_choice
                        ],
                    ),

                html.Div(className="div_for_text",
                        children=[html.P("Filter by sex")],style={"height":"25px"}),
                html.Div(
                        className="div-for-dropdown",
                        children=[
                            sex_choice
                        ],
                    ),
                tableI,
                tableII,
                # smallcard,
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="nine columns div-for-charts bg-grey",
                    children=content,
                ),


        ],
        style={"margin-top":"0px","padding":"0px","background-color":"1f1f1f"}
    )

                    ],id="id_dashboard_content"),
    short_content])

############################################CALL BACK FOR SET CUSTOM
#@callback(
#     Output(component_id='id_time_period_choice', component_property='value'),
#     Input(component_id= 'id_date_range', component_property='start_date'),
#     Input(component_id= 'id_date_range', component_property='end_date'),

#         )
# def update_time_range(start,end):
#     """Control time range selection."""
#     ans=0
#     for item in ["Historical","Last year"]:
#         if [pd.to_datetime(start),pd.to_datetime(end)]==list(map(lambda z:pd.to_datetime(z),Default_time_ranges[item])):
#             ans=item

#     return no_update if ans!=0 else None

#############################################CALL BACK FOR DATES
# @callback(
#     Output(component_id= 'id_date_range', component_property='start_date'),
#     Output(component_id= 'id_date_range', component_property='end_date'),
#     Input(component_id='id_time_period_choice', component_property='value'),
#     # State(component_id= 'id_date_range', component_property='start_date'),
#     # State(component_id= 'id_date_range', component_property='end_date'),
# )

# @callback(
#     Output(component_id= 'id_date_range', component_property='start_date'),
#     Output(component_id= 'id_date_range', component_property='end_date'),
#     Input(component_id='id_time_period_choice', component_property='value'),

# )
# def update_time_range(input_range):
#     """Control time range selection."""

#     start_date=first_day
#     end_date=last_day
#     if input_range != None:
#         [start_date,end_date]=Default_time_ranges[input_range]



#     return no_update if input_range==None else start_date,end_date

@callback(
    Output(component_id= 'id_date_range', component_property='start_date'),
    Output(component_id= 'id_date_range', component_property='end_date'),
    Input(component_id='id_time_period_choice', component_property='value'),

)
def update_time_range(input_range):
    """Control time range selection."""

    start_date=first_day
    end_date=last_day
    if input_range != None:
        [start_date,end_date]=Default_time_ranges[input_range]



    return no_update if input_range==None else start_date,end_date

#############################################CALL BACK FOR SET CUSTOM
# @callback(
#     Output(component_id='id_time_period_choice', component_property='value'),
#     Input(component_id= 'id_date_range', component_property='start_date'),
#     Input(component_id= 'id_date_range', component_property='end_date'),

#         )
# def update_time_range(start,end):
#     """Control time range selection."""
#     ans=0
#     for item in ["Historical","Last year"]:
#         if [pd.to_datetime(start),pd.to_datetime(end)]==list(map(lambda z:pd.to_datetime(z),Default_time_ranges[item])):
#             ans=item

#     return no_update if ans!=0 else None
@callback(
    Output(component_id='id_dashboard_content', component_property='style'),
    Output(component_id='id_movie_content',component_property='style'),
    Input(component_id='id_tabs', component_property='active_tab'),
)
def update_visibility(active_tab):
    if active_tab==Movie:
        ans={"display":"none"},{"display":"inherit"}
    else:
        ans={"display":"inherit"},{"display":"none"}
    return ans

#############################################CALL BACK FOR GRAPHS
@callback(
    Output(component_id= 'id_first_graph', component_property='figure'),
    Output(component_id= 'id_second_graph', component_property='figure'),
    Output(component_id= 'id_third_graph', component_property='figure'),
    Output(component_id= 'id_fourth_graph', component_property='figure'),
    Output(component_id= 'id_tests', component_property='children'),
    Output(component_id= 'id_molecular_tests', component_property='children'),
    Output(component_id= 'id_positive_tests', component_property='children'),
    Output(component_id= 'id_currently-', component_property='children'),
    Output(component_id= 'id_catIII_tests', component_property='children'),
    Output(component_id= 'id_catIV_tests', component_property='children'),
    Input(component_id= 'id_date_range', component_property='start_date'),
    Input(component_id= 'id_date_range', component_property='end_date'),
    Input(component_id='id_responsable_choice', component_property='value'),
    Input(component_id='id_age_choice', component_property='value'),
    Input(component_id='id_sex_choice', component_property='value'),
    Input(component_id='id_tabs', component_property='active_tab'),

)



def update_graphs(start_date,end_date,responsable,age,sex,active_tab):

    first_graph=empty_fig()
    second_graph=empty_fig()
    third_graph=empty_fig()
    fourth_graph=empty_fig()

    data=df

    """Apply Date filter"""

    data=data[(data["SIGN_DATE"]>=pd.to_datetime(start_date))&(data["SIGN_DATE"]<=pd.to_datetime(end_date))]

    time_fitered_data=data

    """Apply Sex filter"""
    if sex !="All sexes":
        data=data[data["SEX"]==sex]

    """Apply Age filter"""


    if age =="Less than 40":
        data=data[data["AGE"]<40]
    if age =="40 to 49":
        data=data[(data["AGE"]>=40)&(data["AGE"]<50)]
    if age =="50 to 59":
        data=data[(data["AGE"]>=50)&(data["AGE"]<60)]
    if age =="60 to 69":
        data=data[(data["AGE"]>=60)&(data["AGE"]<70)]
    if age =="70 or older":
        data=data[data["AGE"]>=70]
    all_pathologists_df=data

    """Apply Pathologist filter"""
    if responsable !="All pathologists":
        data=data[data["CYTOPATHOLOGIST"]==responsable]

        #################################### FILTERED DATA
    positive_data=data[data["RESULT"]=="POSITIVE"]
    negative_data=data[data["RESULT"]=="NEGATIVE"]
    category3_data=data[data["Bethesda Cathegory"]==3]
    category4_data=data[data["Bethesda Cathegory"]==4]

###################################
####################################
#####################################
################# TABLE DATA


    tests=data.shape[0]
    molecular_tests=data[data["MOLECULAR "]=="THYROSEQ"].shape[0]
    positives_overall=data[data["RESULT"]=="POSITIVE"].shape[0]
    currently_negative=data[data["RESULT"]=="CURRENTLY NEGATIVE"].shape[0]
    catIII_tests=data[data["Bethesda Cathegory"]==3].shape[0]
    catIV_tests=data[data["Bethesda Cathegory"]==4].shape[0]




   ######## PIE GRAPH CATEGORIES
    def  pie_graph_beth(data_frame):
        title="Bethesda Category Distribution"
        Beth_info=data_frame["Bethesda Cathegory"].value_counts().to_dict()
        # numeric_names=sorted(list(Beth_info.keys()))
        numeric_names=sorted(list(data_frame["Bethesda Cathegory"].unique()))
        values=[Beth_info[x] for x in numeric_names]
        names=["Cat "+make_roman(x) for x in numeric_names]
        pie_data=pd.DataFrame()
        pie_data["Category"]=names
        pie_data["Count"]=values
        return make_pie(pie_data,"Category","Count",title)

####### Bethesda Category count over time
########################
    def Bethesda_time_graph(dataframe,sexo,edad,medicoresponsable):
        yearly_data=dataframe
        """Apply Sex filter"""
        if sexo !="All sexes":
            yearly_data=yearly_data[yearly_data["SEX"]==sexo]

        """Apply Age filter"""


        if edad =="Less than 40":
            yearly_data=yearly_data[yearly_data["AGE"]<40]
        if edad =="40 to 49":
            yearly_data=yearly_data[(yearly_data["AGE"]>=40)&(yearly_data["AGE"]<50)]
        if edad =="50 to 59":
            yearly_data=yearly_data[(yearly_data["AGE"]>=50)&(yearly_data["AGE"]<60)]
        if edad =="60 to 69":
            yearly_data=yearly_data[(yearly_data["AGE"]>=60)&(yearly_data["AGE"]<70)]
        if edad =="70 or older":
            yearly_data=yearly_data[yearly_data["AGE"]>=70]


        """Apply Pathologist filter"""
        if medicoresponsable !="All pathologists":
            yearly_data=yearly_data[yearly_data["CYTOPATHOLOGIST"]==medicoresponsable]


        beth_df=pd.DataFrame()
        for i in range(1,7):
            temp_df=pd.DataFrame()
            temp_df["Year"]=years
            temp_df["Call Count"]=[yearly_data[(yearly_data["Bethesda Cathegory"]==i)&(yearly_data["YEAR"]==year)].shape[0] for year in years]
            temp_df["Category"]=["Cat "+make_roman(i) for year in years]
            beth_df=pd.concat([beth_df,temp_df],ignore_index=True)
        return make_scatter_graph_time_bethesda(beth_df)
######################  OVERALL GENE GRAPH
    def gene_graph(dataframe):
        labels_bar=list(dataframe["GENE MUTATED"].unique())
        labels_bar=[x for x in labels_bar if str(x) not in ["?","nan","0"]]
        def count_instances(x):
            return dataframe[dataframe["GENE MUTATED"]==x].shape[0]

        labels_bar=sorted(labels_bar,key=lambda z:count_instances(z),reverse=True)
        values_bar=[count_instances(x) for x in labels_bar]
        bar_data=pd.DataFrame()
        bar_data["Count"]=values_bar
        bar_data["GENE MUTATED"]=labels_bar
        bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)






        return make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Molecular Tests")

        """Apply Pathologist filter"""
    def sex_distribution_graph(dataframe,medicoresponsable):
        sex_data=dataframe
        if responsable !="All pathologists":
            sex_data=dataframe[dataframe["CYTOPATHOLOGIST"]==medicoresponsable]
        return make_ages_graph(sex_data)

######################    RESULTS OVERALL ##############################################################

    if active_tab==Overall:
        first_graph=pie_graph_beth(data)
        second_graph=Bethesda_time_graph(df,sex,age,responsable)
        third_graph=gene_graph(data)
        fourth_graph=sex_distribution_graph(time_fitered_data,responsable)

    #########################
    ######################### GRAPHS COMPARING CYTOPATHOLOGISTS
    #########################


    #### MOLECULAR BY RESULT GRAPH
    def molecular_by_result_graph(dataframe):
        count_results=dataframe["RESULT"].value_counts().to_dict()
        pie_data=pd.DataFrame()
        pie_data["Result"]=list(count_results.keys())
        pie_data["Count"]=list(count_results.values())
        return make_pie(pie_data,"Result","Count","Molecular Tests By Result")

############# CATEGORY RATIOS BY PATHOLOGISTS
    def count_data(all_paths_df):
        count_data=pd.DataFrame()

        count_data["Pathologists"]=pathologists
        for i in range(1,7):
            count_data[make_roman(i)]=[count_categories(all_paths_df,pathologist,i) for pathologist in pathologists]
        count_data["Cases"]=[count_cases(all_paths_df,pathologist) for pathologist in pathologists]
        count_data["Positives"]=[count_by_result(all_paths_df,pathologist,"POSITIVE") for pathologist in pathologists]
        count_data["Currently Negative"]=[count_by_result(all_paths_df,pathologist,"CURRENTLY NEGATIVE") for pathologist in pathologists]
        count_data["Positives or CN"]=count_data["Positives"]+count_data["Currently Negative"]
        count_data["positive_rate"]=count_data["Positives or CN"]/count_data["Cases"]
        count_data["positive_rate"]=count_data["positive_rate"].apply(lambda z:round(z,2))
        for i in range(1,7):
            count_data["Cat "+make_roman(i)]=count_data[make_roman(i)]/count_data["Cases"]
            count_data["Cat "+make_roman(i)]=count_data["Cat "+make_roman(i)].apply(lambda z:round(z,2))
        # count_data["Pathologists"]=pathologists

        count_data["Cat III Positives"]=[count_result_by_category(df,pathologist,3,"POSITIVE") for pathologist in pathologists]
        count_data["Cat III + Rate"]=round(count_data["Cat III Positives"]/count_data["III"],2)


    #################################### ADD ALL PATHOLOGISTS ROW
    ###################################
        new_row=dict()
        new_row["Pathologists"]=["All pathologists"]
        new_row["Cases"]=[count_data["Cases"].sum()]
        for i in range(1,7):
            new_row[make_roman(i)]=[count_data[make_roman(i)].sum()]
        for i in range(1,7):
            new_row["ratio category "+make_roman(i)]=[new_row[make_roman(i)][0]/new_row["Cases"][0]]
        new_row["Positives"]=[count_data["Positives"].sum()]
        new_row["positive_rate"]=[count_data["Positives"].sum()/count_data["Cases"].sum()]
        new_row["Cat III Positives"]=[count_data["Cat III Positives"].sum()]
        new_row["Cat III + Rate"]=[round(count_data["Cat III Positives"].sum()/count_data["III"].sum(),2)]
        for i in range(1,7):
            new_row["Cat "+ make_roman(i)]=[round(count_data[make_roman(i)].sum()/count_data["Cases"].sum(),2)]

        new_row=pd.DataFrame.from_dict(new_row)
        count_data=pd.concat([count_data,new_row])
        count_data["Cat III Call Rate"]=count_data["Cat III"]
        return count_data

    #######################################
    #######################################

    def compare_ratios(dataframe):
        return make_stacked_bar(dataframe,"Pathologists",["Cat "+make_roman(i)  for i in range(1,7)], "Category Distribution By Pathologist","Rate")

    def scat_call_vs_pos(dataframe):
        return scat_callrate_vs_positive(dataframe)


    ##############################COMPARING CP
    if active_tab==ComparingCP:

        gap_minder_data=make_gap_minder_data(df)
        time_df=pd.DataFrame()
        for path in pathologists+["All pathologists"]:
            time_path=pd.DataFrame()
            time_path["Year"]=list(gap_minder_data[gap_minder_data["Pathologist"]==path]["Year"].unique())
            time_path["Cat III Call Rate"]=list(gap_minder_data[gap_minder_data["Pathologist"]==path]["Call rate category III"])
            time_path["Pathologist"]=[path for i in range(time_path["Cat III Call Rate"].shape[0]) ]
            time_df=pd.concat([time_df,time_path])


        counting_data=count_data(all_pathologists_df)


        first_graph=molecular_by_result_graph(data)
        second_graph=compare_ratios(counting_data)
        third_graph=scat_callrate_vs_positive(counting_data)
        fourth_graph=make_CatIII_Call_Rate_time(time_df)


    return first_graph,second_graph,third_graph,fourth_graph,tests,molecular_tests,positives_overall,currently_negative,catIII_tests,catIV_tests


     ##############
     # ############  MAYBE LATER

    # ######################  BAR GRAPH CATEGORIES
    # labels_bar=sorted(list(data["Bethesda Cathegory"].unique()))
    # values_bar=[len(data[data["Bethesda Cathegory"]==label])for label in labels_bar]
    # bar_data=pd.DataFrame()
    # bar_data["Count"]=values_bar
    # bar_data["Category"]=[make_roman(x) for x in labels_bar]
    # # bar_data["labels"]=bar_data["labels"].astype(str)
    # bar_categories=make_bar(bar_data,"Category","Count","Bethesda Category Counts","Count")

    ######################  ROM GRAPH OVERALL
    # labels_bar=list(data["ROM"].unique())
    # labels_bar=sorted([x for x in labels_bar if str(x) not in ["?","nan"]])
    # values_bar=[len(data[data["ROM"]==label])for label in labels_bar]
    # labels_bar=[str(x)+ "%" for x in labels_bar]
    # bar_data=pd.DataFrame()
    # bar_data["Count"]=values_bar
    # bar_data["ROM"]=labels_bar
    # bar_data["ROM"]=bar_data["ROM"].astype(str)
    # rom_graph=make_rom(bar_data,"ROM","Count","Risk of Malignancy Overall")
######################  ROM GRAPH CAT III
    # labels_bar=list(category3_data["ROM"].unique())
    # labels_bar=sorted([x for x in labels_bar if str(x) not in ["?","nan"]])
    # values_bar=[len(category3_data[category3_data["ROM"]==label])for label in labels_bar]
    # labels_bar=[str(x)+ "%" for x in labels_bar]
    # bar_data=pd.DataFrame()
    # bar_data["Count"]=values_bar
    # bar_data["ROM"]=labels_bar
    # bar_data["ROM"]=bar_data["ROM"].astype(str)
    # rom_graph_cat3=make_rom(bar_data,"ROM","Count","Risk of Malignancy Category III")
    ######################  ROM GRAPH CAT IV
    # labels_bar=list(category4_data["ROM"].unique())
    # labels_bar=sorted([x for x in labels_bar if str(x) not in ["?","nan"]])
    # values_bar=[len(category4_data[category4_data["ROM"]==label])for label in labels_bar]
    # labels_bar=[str(x)+ "%" for x in labels_bar]
    # bar_data=pd.DataFrame()
    # bar_data["Count"]=values_bar
    # bar_data["ROM"]=labels_bar
    # bar_data["ROM"]=bar_data["ROM"].astype(str)
    # rom_graph_cat4=make_rom(bar_data,"ROM","Count","Risk of Malignancy Category IV")



    # make_molecular_overview(pie_data,bar_data)
    #make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Molecular Tests")

#     ######################  OVERALL MUTATION GRAPH
#     labels_bar=list(data["MUTATION"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(data[data["MUTATION"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["MUTATION"]=labels_bar
#     bar_data["MUTATION"]=bar_data["MUTATION"].astype(str)
#     mutation_graph=make_gene(bar_data,"MUTATION","Count","Mutation Count Molecular Tests")

#     ######################  POSITIVE GENE GRAPH
#     labels_bar=list(positive_data["GENE MUTATED"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(positive_data[positive_data["GENE MUTATED"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["GENE MUTATED"]=labels_bar
#     bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)
#     positive_gene_graph=make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Positive Tests")

#     ######################  POSITIVE MUTATION GRAPH
#     labels_bar=list(positive_data["MUTATION"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(positive_data[positive_data["MUTATION"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["MUTATION"]=labels_bar
#     bar_data["MUTATION"]=bar_data["MUTATION"].astype(str)
#     positive_mutation_graph=make_gene(bar_data,"MUTATION","Count","Mutation Count Positive Tests")
#     ######################  NEGATIVE GENE GRAPH
#     labels_bar=list(negative_data["GENE MUTATED"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(negative_data[negative_data["GENE MUTATED"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["GENE MUTATED"]=labels_bar
#     bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)
#     negative_gene_graph=make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Negative Tests")

#     ######################  NEGATIVE MUTATION GRAPH
#     labels_bar=list(negative_data["MUTATION"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(negative_data[negative_data["MUTATION"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["MUTATION"]=labels_bar
#     bar_data["MUTATION"]=bar_data["MUTATION"].astype(str)
#     negative_mutation_graph=make_gene(bar_data,"MUTATION","Count","Mutation Count Negative Tests")
# ######################### CATEGORY GRAPHS
# #########################

# ######################  CATEGORY III GENE GRAPH
#     labels_bar=list(category3_data["GENE MUTATED"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(category3_data[category3_data["GENE MUTATED"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["GENE MUTATED"]=labels_bar
#     bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)
#     category3_gene_graph=make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Category III")

#     ######################  CATEGORY III MUTATION GRAPH
#     labels_bar=list(category3_data["MUTATION"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(category3_data[category3_data["MUTATION"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["MUTATION"]=labels_bar
#     bar_data["MUTATION"]=bar_data["MUTATION"].astype(str)
#     category3_mutation_graph=make_gene(bar_data,"MUTATION","Count","Mutation Count Category III")
#     ######################  CATEGORY IV GENE GRAPH
#     labels_bar=list(category4_data["GENE MUTATED"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(category4_data[category4_data["GENE MUTATED"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["GENE MUTATED"]=labels_bar
#     bar_data["GENE MUTATED"]=bar_data["GENE MUTATED"].astype(str)
#     category4_gene_graph=make_gene(bar_data,"GENE MUTATED","Count","Gene Mutated Count Category IV")

#     ######################  CATEGORY IV MUTATION GRAPH
#     labels_bar=list(category4_data["MUTATION"].unique())
#     labels_bar=[x for x in labels_bar if str(x) not in ["?","nan"]]
#     values_bar=[len(category4_data[category4_data["MUTATION"]==label])for label in labels_bar]
#     bar_data=pd.DataFrame()
#     bar_data["Count"]=values_bar
#     bar_data["MUTATION"]=labels_bar
#     bar_data["MUTATION"]=bar_data["MUTATION"].astype(str)
#     category4_mutation_graph=make_gene(bar_data,"MUTATION","Count","Mutation Count Category IV")

##

###################################### DURATION GRAPH

    # data["duration"]=(data["SIGN_DATE"]-data["ACCESS_DATE"])
    # data["duration"]=data["duration"].apply(lambda z:z.days)
    # Duration=data["duration"].value_counts().to_dict()
    # numeric_names=sorted(list(Duration.keys()))
    # names=[str(x) for x in numeric_names]
    # values=[Duration[x] for x in numeric_names]
    # duration_data=pd.DataFrame()
    # duration_data["Processing days"]=values
    # duration_data["duration_names"]=names
    # duration_graph=make_rom(duration_data,"duration_names","Processing days","Processing Time in Days")





    # fig_tab = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
    #              cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
    #                  ])
    # fig_tab.update_layout(
    #         autosize=True,
    #         margin=dict(
    #             l=0,
    #             r=0,
    #             b=0,
    #             t=40,
    #             pad=0
    #         ),
    #         template="plotly_dark",
    #         title={
    #         "text":"Somethings else",
    #         'y':0.98,
    #         'x':0.46,
    #         'xanchor': 'center',
    #         'yanchor': 'top',
    #         },
    #         legend_title="",
    #         xaxis_title=None,


    #         # legend_traceorder="reversed",

    #     )
    #################### MUTATIONS BY RESULT
    # if active_tab=="Mutations by Result":
    #     first_graph=positive_gene_graph
    #     second_graph=positive_mutation_graph
    #     third_graph=negative_gene_graph
    #     fourth_graph=negative_mutation_graph

    ###############################################
    ################### GRAPHS FOR COMPARING PATHOLOGISTS
    #########################

    ##################
    ###################### MUTATIONS BY CATEGORY
    # if active_tab=="Mutations by Category":
    #     first_graph=category3_gene_graph
    #     second_graph=category3_mutation_graph
    #     third_graph=category4_gene_graph
    #     fourth_graph=category4_mutation_graph
######################################
######################################
    # dfLarge=pd.read_csv("data/USCAP_Large.csv")
    # gap_pathologists=[pathologist for pathologist in list(dfLarge["CYTOPATHOLOGIST"].unique()) if dfLarge[dfLarge["CYTOPATHOLOGIST"]==pathologist].shape[0]>200]

    # gap_pathologists=["Pathologist "+ str(pathologist) for pathologist in sorted(gap_pathologists)]

    # years=list(dfLarge["YEAR"].unique())
    # gap_minder_data=pd.DataFrame()
    # for year in years:
    #     for pathologist in gap_pathologists:
    #         new_row=dict()
    #         size=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]==year)].shape[0]

    #         calls_CatIII=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]
    #         ==year)&(dfLarge["Bethesda Cathegory"]==3)].shape[0]
    #         if calls_CatIII>0:
    #             call_rate_CatIII=calls_CatIII/size

    #             positive_rate_CatIII=dfLarge[(dfLarge["CYTOPATHOLOGIST"]==eval(pathologist[12:]))&(dfLarge["YEAR"]
    #             ==year)&(dfLarge["Bethesda Cathegory"]==3)&(dfLarge["RESULT"]=="POSITIVE")].shape[0]/calls_CatIII
    #             new_row["Pathologist"]=[pathologist]
    #             new_row["Year"]=[year]
    #             new_row["Case Count"]=[size]
    #             new_row["Call rate category III"]=[call_rate_CatIII]
    #             new_row["Positive rate category III"]=[positive_rate_CatIII]
    #             new_row=pd.DataFrame.from_dict(new_row)


    #             gap_minder_data=pd.concat([gap_minder_data,new_row])
    # gap_movie=make_gapminder(gap_minder_data,"Call rate category III","Positive rate category III","Year","Pathologist","Case Count","Pathologist","Pathologist")
##############################ROM
    # if active_tab=="ROM":
    #     first_graph=gap_movie#rom_graph
    #     second_graph=rom_graph_cat3
    #     third_graph=rom_graph_cat4
    #     fourth_graph=make_table_graph(["Group","BCR","PCR"],[["All tests","Molecular","Category III","Category IV"],[negativity_overall,negativity_molecular,negativity_catIII,negativity_catIV],[positivity_overall,positivity_molecular,positivity_catIII,positivity_catIV]],"Call Rates")

    ##################
    # tests=data.shape[0]
    # positivity="No data"
    # positives=data[data["RESULT"]=="POSITIVE"].shape[0]


    # if tests>0:
    #     positivity=round(positives/tests,2)
    # if active_tab=="tab-1":
    #     first_graph=rom_graph

