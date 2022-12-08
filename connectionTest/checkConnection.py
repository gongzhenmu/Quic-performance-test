#TCP
from scapy.all import *
import sys
filename = sys.argv[1]
scapy_cap = rdpcap(filename)
name = filename.split("/")[-1]
startTime = scapy_cap[0].time*1000
for packet in scapy_cap:

    stringPacket = str(packet)
    if "GET" in stringPacket:
        endTime = packet.time*1000
        print(name,round(endTime-startTime,2))
        break







#quic
# from scapy.all import *
# import sys
# import pyshark
# filename = sys.argv[1]
# cap = pyshark.FileCapture(filename)
# name = filename.split("/")[-1]
# #startTime = cap[0].sniff_timestamp*1000
# for packet in cap:
#     print(packet)
    
