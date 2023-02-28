
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def make_ages_graph(df):

    fre=df[["SEX","AGE"]].value_counts().to_dict()
    female_ages=[x[1] for x in sorted(fre.keys()) if x[0]=="Female"]
    female_ages_count=[fre[x] for x in sorted(fre.keys()) if x[0]=="Female"]
    male_ages=[x[1] for x in sorted(fre.keys()) if x[0]=="Male"]
    male_ages_count=[fre[x] for x in sorted(fre.keys()) if x[0]=="Male"]
    female_df=pd.DataFrame()
    female_df["AGES"]=female_ages
    female_df["COUNTS"]=female_ages_count
    male_df=pd.DataFrame()
    male_df["AGES"]=male_ages
    male_df["COUNTS"]=male_ages_count

    # overall_fre=df["AGE"].value_counts().to_dict()
    # overall_df=pd.DataFrame()
    # overall_df["AGES"]=sorted(overall_fre.keys())
    # overall_df["COUNTS"]=[overall_fre[x] for x in sorted(overall_fre.keys())]

    colors=px.colors.qualitative.Plotly

    fig = make_subplots(rows=2, cols=1,
                         )
    # first=make_bar(female_df,"AGES","COUNTS","SOmethig")
    female_age_hist= go.Bar(x=female_df["AGES"], y=female_df["COUNTS"],name="Female",marker=dict(color=colors[5]))
    male_age_hist=go.Bar(x=male_df["AGES"], y=male_df["COUNTS"],name="Male",marker=dict(color=colors[9]))

    fig.add_trace(
        female_age_hist,
        row=1, col=1,
    )


    # overall_age_dist=go.Bar(x=overall_df["AGES"], y=overall_df["COUNTS"],name="Overall",marker=dict(color=colors[2]))
    fig.add_trace(
        male_age_hist,
        row=2, col=1,
    )
    #
    fig.update_layout(
                autosize=True,
                margin=dict(
                    l=0,
                    r=0,
                    b=0,
                    t=40,
                    pad=0
                ),
                template="plotly_dark",
                title={
                "text":"Age Distribution By Sex",
                'y':0.98,
                'x':0.46,
                'xanchor': 'center',
                'yanchor': 'top'
                },
                legend_title="",
                # xaxis_title="Age",
                # yaxis_title="Count",
                # barmode="stack",
                # legend_traceorder="reversed",

            )
    # Update xaxis properties
    # fig.update_xaxes(title_text="xaxis 1 title", row=1, col=1)
    # fig.update_xaxes(title_text="xaxis 2 title", row=2, col=1)
    # fig.update_xaxes(title_text="xaxis 3 title", showgrid=False, row=2, col=1)
    # fig.update_xaxes(title_text="xaxis 4 title", type="log", row=2, col=2)

    # Update yaxis properties
    fig.update_yaxes(title_text="Count Female",row=1, col=1)
    fig.update_yaxes(title_text="Count Male",row=2, col=1)
    # fig.update_yaxes(title_text="yaxis 3 title", showgrid=False, row=2, col=1)
    # fig.update_yaxes(title_text="yaxis 4 title", row=2, col=2)
    # fig.update_layout(barmode='stack')
    return fig