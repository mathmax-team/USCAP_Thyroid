import pandas as pd
import plotly.express as px

def make_gapminder(dataframe,x_column,y_column,animation_frame_column,animation_group_column,size_column):
    this_figure=px.scatter(dataframe, x=x_column, y=y_column, animation_frame=animation_frame_column, animation_group=animation_group_column,
            size=size_column,color=animation_group_column, hover_name=animation_group_column,
            color_discrete_sequence=px.colors.qualitative.T10,range_x=[0,0.5], range_y=[0,0.5])
            #  log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    A=str(list(dataframe[dataframe[animation_group_column]=="All pathologists"][size_column]))
    B=str(list(dataframe[dataframe[animation_group_column]=="Pathologist 7"][size_column]))
    C=str(A==B)
    this_figure.update_layout(
                autosize=True,
                # width=1400,
                #  height=700,

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
                # xaxis_title="",
                font=dict(
            # family="Courier New, monospace",
            size=18,
            # color="RebeccaPurple"
    )
                # legend_traceorder="reversed",

            )
    this_figure.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 3000
    this_figure.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 200000
    return this_figure

