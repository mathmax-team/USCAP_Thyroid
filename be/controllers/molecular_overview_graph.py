from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

def make_molecular_overview(pie_df,bar_df):
    fag = make_subplots(rows=2, cols=1,
                        specs=[[{"type": "domain"}],
            [{"type": "xy"}]],
            subplot_titles=("Molecular Tests by Result","Mutation Count by Gene"),
            )
        # first=make_bar(female_df,"AGES","COUNTS","SOmethig")

    X=bar_df["GENE MUTATED"]
    Y=bar_df["Count"]
    colores=px.colors.qualitative.T10
    fag.add_trace(
    go.Pie(labels=pie_df["labels"], values=pie_df["values"]),
    row=1, col=1,
    )

    for i in range(len(X)):
        fag.add_trace(go.Bar(x=[X[i]], y=[Y[i]],name=X[i],#color="red"
                        marker=dict(color = colores[i%len(colores)],
                        #  colorscale=px.colors.qualitative.Pastel1
                        )
                        ),row=2,col=1)


    fag.update_layout(
                autosize=True,
                margin=dict(
                    l=0,
                    r=0,
                    b=0,
                    t=60,
                    pad=0
                ),
                template="plotly_dark",
                title=None,
                legend_title="Gene Mutated",
                xaxis_title=None,
                showlegend=True,
                xaxis={"visible":False})

    for trace in fag['data']:
        if (not trace['name'] in list(X)):
            trace['showlegend'] = False
            trace["name"]=""#
                # colorscale=px.colors.qualitative.Pastel1
    for annotation in fag['layout']['annotations']:
        if annotation["text"]=="Mutation Count by Gene":
            annotation['y']=0.5
        else:
            annotation['y']=1.1

    return fag