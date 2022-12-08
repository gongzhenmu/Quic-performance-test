webName=$1
#port 8888 is for web, port 6121 is for quic
tcpdump -i any -w $webName "port 8888 or port 6121"