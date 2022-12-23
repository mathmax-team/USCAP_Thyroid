import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
def make_adequacy_graph(Adequate,Inadequate_processed,Inadequate_not_proccessed):
    my_green="#42D7A7"
    my_orange="#FFC006"
    bg="#f5f3f4"
    newbg="#807b6f"
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['Inadequate','Adequate','Total'],
        x=[Inadequate_processed, Adequate,Adequate+Inadequate_processed],
        name='Processed',
        orientation='h',
        marker=dict(
            color=my_green,
            #line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=["Inadequate","Adequate",'Total'],
        x=[Inadequate_not_proccessed, 0,Inadequate_not_proccessed],
        name='Not Processed',
        orientation='h',
        marker=dict(
            color=my_orange,
            #line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))

    fig.update_layout(barmode='stack')
    fig.update_layout(margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin
    ),
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    height=60,
    width=300,

    # bargap=0.30,
    # bargroupgap=0.0
    )
    fig.update_traces(width=0.5)
    fig.update_layout(xaxis=dict(showgrid=False,showline=False,showticklabels=False),
              yaxis=dict(showgrid=False,showline=False)
)
    return fig
