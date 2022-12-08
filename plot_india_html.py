import plotly.graph_objs as go
import numpy as np
import pandas as pd


if __name__ == "__main__":
    tcp_file = "./data/tcp_output_html_india.log"
    quic_file = "./data/quic_output_html_india.log"

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
        title=f"QUIC vs TCP time to request webpage (average) From US to India",
        yaxis_title="Time (ms)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    fig.show()
   
    for key,value in tcp_time_dict.items():
        fig = go.Figure()
        print(key)
        fig.add_trace(go.Box(
            y=value,
            name="TCP",
            marker_color='#3D9970'
        ))
        fig.add_trace(go.Box(
            y=quic_time_dict[key],
            name="QUIC",
            marker_color='#FF4136'
        ))
        fig.update_layout(
            title=f"QUIC vs TCP time to request webpage (std) From US to India",
            yaxis_title="Time (ms)",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            ),
            boxmode='group' # group together boxes of the different traces for each value of x

        )
    fig.show()



    