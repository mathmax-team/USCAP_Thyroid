

from plotly import graph_objs as go


def make_table_graph(column_names,columns,title):
    fig = go.Figure(data=[go.Table(header=dict(
                            values=column_names,
                            fill_color="#121212",
                            line_color="white",
                            font = dict(color = 'white', size = 17),
                            height=28)
                            ,
                            cells=dict(values=columns,line_color='white',height=25,
                fill_color='#121212',font = dict(color = 'white', size = 15)
                ),
                ),
                ],
                )

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
            "text":title,
            'y':0.98,
            'x':0.46,
            'xanchor': 'center',
            'yanchor': 'top',
            },
            legend_title="",
            xaxis_title=None,


            # legend_traceorder="reversed",

        )
    return fig