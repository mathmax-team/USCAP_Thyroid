import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def make_adequacy_graph(Adequate,Inadequate_processed,Inadequate_not_proccessed):
    my_green="#42D7A7"
    my_orange="#FFC006"

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['Inadequate','Adequate','Total'],
        x=[Inadequate_processed, Adequate,Adequate+Inadequate_processed],
        name='Processed',
        orientation='h',
        marker=dict(
            color=my_green,
        )
    ))
    fig.add_trace(go.Bar(
        y=["Inadequate","Adequate",'Total'],
        x=[Inadequate_not_proccessed, 0,Inadequate_not_proccessed],
        name='Not Processed',
        orientation='h',
        marker=dict(
            color=my_orange,
        )
    ))

    fig.update_layout(barmode='stack')
    fig.update_layout(margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin
    ),
    height=80,
    template="plotly_dark",
    plot_bgcolor= 'rgba(0, 0, 0, 0)',
    paper_bgcolor= 'rgba(0, 0, 0, 0)',
    )
    fig.update_traces(width=0.5)
    fig.update_layout(xaxis=dict(showgrid=False,showline=False,showticklabels=False),
              yaxis=dict(showgrid=False,showline=False)
)
    return fig
