import pandas as pd
import plotly.express as px

def make_gapminder(dataframe,x_column,y_column,animation_column,animation_group_column,size_column,color_column,hover_name_column):
    this_figure=px.scatter(dataframe, x=x_column, y=y_column, animation_frame=animation_column, animation_group=animation_group_column,
            size=size_column, color=color_column, hover_name=hover_name_column,)
            # log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    this_figure.update_layout(
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
                "text":"Overview Molecular Results",
                'y':0.98,
                'x':0.46,
                'xanchor': 'center',
                'yanchor': 'top'
                },
                legend_title="",
                xaxis_title="",
                # legend_traceorder="reversed",

            )
    this_figure.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 3000
    this_figure.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 200000
    return this_figure

