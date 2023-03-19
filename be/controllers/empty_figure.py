import plotly.graph_objects as go

def empty_fig():
    ans= go.Figure()
    ans.update_layout(
    autosize=True,
    #width=470,
    #height=300,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    template="plotly_dark",
    paper_bgcolor=" rgb(18, 18, 18)",
    plot_bgcolor=" rgb(18, 18, 18)"
)
    return ans