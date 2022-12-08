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
    tcp_avgs = []
    tcp_stds = []
    quic_avgs = []
    quic_stds = []
    for key,value in quic_time_dict.items():
        quic_avgs.append(np.mean(value))
        quic_stds.append(np.std(value))
        tcp_avgs.append(np.mean(tcp_time_dict[key]))
        tcp_stds.append(np.std(tcp_time_dict[key]))
       
    fig = go.Figure(data=[
            go.Bar(name='tcp', x=websites, y=tcp_avgs),
            go.Bar(name='quic', x=websites, y=quic_avgs)
        ])
    fig.update_layout(
        title=f"QUIC vs TCP time to request webpage (average) From US to Germany",
        yaxis_title="Time (ms)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    fig.show()

   