import plotly.graph_objs as go
import numpy as np
import pandas as pd


time_dict = {}
target_key = ""
with open("./data/tcp_output_html_germany.log", 'r') as f:
    data = f.readlines()
    for line in data:
        if line[0] == '$' or line[0] == "w":
            target_key = line[1:]
            time_dict[line[1:]] = []
        else:
            time_dict[target_key].append(float(line)*1000)
print(target_key)    
hist, bin_edges = np.histogram(time_dict[target_key], bins=5, density=True)
cdf = np.cumsum(hist * np.diff(bin_edges)) 
fig = go.Figure(data=[
    go.Bar(x=bin_edges, y=hist, name='Histogram'),
    go.Scatter(x=bin_edges, y=cdf, name='CDF'),
    
])

fig.update_layout(
    title="CDFs of time to request webpage",
    xaxis_title="Time (ms)",
    yaxis_title="CDF",
    # legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.show()