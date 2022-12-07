import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 4, 8, 3],
    fill=None,
    mode='lines',
    line_color='indigo',
    ))
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 6, 2, 6],
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()