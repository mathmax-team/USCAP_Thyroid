import plotly.express as px
from be.controllers.roman import make_roman



def scat_callrate_vs_positive(dataframe):
    scat=px.scatter(dataframe,x='Cat '+make_roman(3)+ " Call Rate",
                    y='Cat III + Rate',
                    color='Pathologists',
                    size='Cases',
                    hover_data=['Pathologists'],color_discrete_sequence=px.colors.qualitative.T10
                    )
    scat.update_layout(
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
            "text":"Cat III  Calling Rate vs Positivity",
            'y':0.98,
            'x':0.46,
            'xanchor': 'center',
            'yanchor': 'top'
            },
            legend_title="",
            # xaxis_title=None,
            # legend_traceorder="reversed",

        )
    return scat