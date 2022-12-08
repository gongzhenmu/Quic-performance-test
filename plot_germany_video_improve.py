import plotly.graph_objs as go
import numpy as np
import pandas as pd


if __name__ == "__main__":
    tcp_file = "./data/tcp_output_video_germany.log"
    quic_file = "./data/quic_output_video_germany.log"

    tcp_time_dict = {}
    target_key = ""
    with open(tcp_file, 'r') as f:
        data = f.readlines()
        for line in data:
            line = line.strip().replace("$","")
            if line[0] == 't':
                target_key = line[4:][:-4]
                tcp_time_dict[target_key] = []
            else:
                tcp_time_dict[target_key].append(float(line)*1000)
    quic_time_dict = {}
    target_key = ""
    with open(quic_file, 'r') as f:
        data = f.readlines()
        for line in data:
            line = line.strip().replace("$","")
            if line[0] == 't':
                target_key = line[4:][:-4]
                quic_time_dict[target_key] = []
            else:
                quic_time_dict[target_key].append(float(line)*1000)

    websites = [key+"MB" for key in quic_time_dict.keys()]
    improvements = []
    for key,value in quic_time_dict.items():
        improvements.append((np.mean(tcp_time_dict[key])-np.mean(value))/np.mean(tcp_time_dict[key])*100)
       
    fig = go.Figure(data=[
            go.Bar(name='Improvements', x=websites, y=improvements),
        ])
    fig.update_layout(
        title=f"QUIC improvement over TCP request video From US to Germany",
        yaxis_title="Precentage (%)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    fig.show()

   