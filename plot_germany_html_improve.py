import plotly.graph_objs as go
import numpy as np
import pandas as pd


if __name__ == "__main__":
    tcp_file = "./data/tcp_output_html_germany.log"
    quic_file = "./data/quic_output_html_germany.log"

    tcp_time_dict = {}
    target_key = ""
    with open(tcp_file, 'r') as f:
        data = f.readlines()
        for line in data:
            if line[0] == '$' or line[0] == "w":
                target_key = line.split(".")[1]
                tcp_time_dict[target_key] = []
            else:
                tcp_time_dict[target_key].append(float(line)*1000)
    quic_time_dict = {}
    target_key = ""
    with open(quic_file, 'r') as f:
        data = f.readlines()
        for line in data:
            if line[0] == '$' or line[0] == "w":
                target_key = line.split(".")[1]
                quic_time_dict[target_key] = []
            else:
                quic_time_dict[target_key].append(float(line)*1000)

    websites = [key for key in tcp_time_dict.keys()]
    improves = []
    for key,value in quic_time_dict.items():
        improves.append((np.mean(tcp_time_dict[key]-np.mean(value) )/np.mean(tcp_time_dict[key]))*100)
       
    fig = go.Figure(data=[
            go.Bar(name='improvement', x=websites, y=improves),
        ])
    fig.update_layout(
        title=f"QUIC improvement over TCP to request webpage From US to Germany",
        yaxis_title="Percentage (%)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    fig.show()
 


    