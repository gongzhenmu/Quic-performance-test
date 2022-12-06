# run http server
## 0. Setup Environment 
use "2. Set up mininet structure using the Makefile." in main branch

## 1. Fetch website resource
```
cd tcp_connection/data/html
chmodx +x getWebsite.sh
./getWebsite.sh
```

## 2. launch server with script
2.1 go back to tcp_connection dir
```
cd ../..
```
2.2 log into host h1
```
make host-h1
```

2.3 launch server
```
chmod +x run_server.sh
./run_server.sh
```
## 2. run client with script
start a new terminal
```
make host-h2
./run_client.sh
```