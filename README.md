# CS536

## 1. First install Chromium QUIC
a. Follow these instructions here for building dependencies in Linux: https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md

In short, we want to do most of the steps up until building chromium since we don't need to build it. These are the steps:

You must be in this directory or the dependencies will not work.<br />
```cd CS536```<br />
```git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git```<br />

Don't use ~ when setting directory.<br />
```export PATH="$PATH:${HOME}/CS536/depot_tools"```

```cd depot_tools``` <br />
```fetch --nohooks --no-history chromium```<br />

Build dependencies: <br />
```cd src```<br />
```./build/install-build-deps.sh```<br />

There may be some additional libraries you have to install alongside this (i.e. bzip2):<br />
```gclient runhooks```<br />

These directories will hold the builds: <br />
```gn gen out/Debug```<br />


b. Afterwards, we can start building the QUIC client and server, some sample data, and running it. This is the official doc: https://chromium.googlesource.com/playground/chromium-org-site/+/refs/heads/master/quic/playing-with-quic.md

In short, these are the commands we need:<br />

Building server and client: <br />
```ninja -C out/Debug quic_server quic_client``` <br />

Get some sample data and save it in our directory:  <br />
```mkdir quic-data```  <br />
```cd quic-data``` <br />
```wget -p --save-headers https://www.example.org```  <br />

In the index.html file inside the "www.example.org" file, we need to add the following line to its headers. <br />
```X-Original-Url: https://www.example.org/```<br />

Remove these lines if they are in other headers of sites you test on:<br />
```"Transfer-Encoding: chunked"```<br />
```"Alternate-Protocol: ..."```<br />

Now, we need to generate certificates for the server and client TLS handshakes:<br />
```cd net/tools/quic/certs``` <br />
```./generate-certs.sh``` <br />
```cd -``` <br />

## 2. Set up mininet structure using the Makefile.
You may need to give provide permissions to some files first. <br />
```chmod -R +x scripts``` <br />

In one terminal:  <br />
```make controller``` <br />

In a second terminal: <br />
```make mininet``` <br />

In a third terminal: <br />
```make cli``` <br />
```app activate fwd``` <br />

Enter "rocks" as the password.

In a fourth terminal: <br />
```make netcfg``` <br />
```make mininet-prereqs``` <br />


## 3. Running the QUIC server and client
More info is here: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/linux/cert_management.md <br />

In short, follow these steps: <br />

a. In one terminal, login to host 1:
```make host-h1``` <br />

Then, we need to add a certificate. This should be run inside the "depot_tools/src" directory. "quic_cert" is the name we will be giving the certificate:  <br />
```mkdir -p $HOME/.pki/nssdb```  <br />
```certutil -d $HOME/.pki/nssdb -N```  <br />
```certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n quic_cert -i net/tools/quic/certs/out/2048-sha256-root.pem``` <br />

Start the server inside "depot_tools/src" directory: <br />
```
./out/Debug/quic_server \
  --quic_response_cache_dir=/workdir/quic-data/www.example.org \
  --certificate_file=net/tools/quic/certs/out/leaf_cert.pem \
  --key_file=net/tools/quic/certs/out/leaf_cert.pkcs8
```
or inside the CS536 directory: <br />
```
/workdir/depot_tools/src/out/Debug/quic_server \
  --quic_response_cache_dir=/workdir/quic-data/www.example.org \
  --certificate_file=net/tools/quic/certs/out/leaf_cert.pem \
  --key_file=net/tools/quic/certs/out/leaf_cert.pkcs8
```

b. In a second terminal, login to host 2:
```make host-h2``` <br />

Start the client: <br />
```./out/Debug/quic_client --host=10.0.0.1 --port=6121 --allow_unknown_root_cert https://www.example.org/``` <br />
or (inside CS536) <br />
```/workdir/depot_tools/src/out/Debug/quic_client --host=10.0.0.1 --port=6121 --allow_unknown_root_cert https://www.example.org/```


## 4. Running QUIC tests
Set permission for bash scripts:

```chmod +x quicWebTestOne.sh ```<br />
```chmod +x quicVideoTestOne.sh ```<br />


Then create quic-data folder:<br />
```mkdir quic-data``` <br />

Copy getWebsite.sh to quic-data:<br />
```cd quic-data```<br />
```./getWebsite.sh```<br />
```rm getWebsite.sh```<br />
```cd ..```<br />


For video tests, put mp4 files and add_headers.py under the same folder, then <br />
```python3 add_headers.py <video name list>``` <br />
`exmpale: python3 add_headers.py test3.mp4 test5.mp4 test66.mp4`

Move the `with_folder `to /quic-data/www.example.org, run<br />
```mv with_headers/* .```<br />
Go back to the folder where Makefile is located and run:<br />
```make host-h1```<br />

```python3 changeHeaderWeb.py /workdir/quic-data/```<br />
```
./out/Debug/quic_server \
  --quic_response_cache_dir=/workdir/quic-data/www.example.org \
  --certificate_file=net/tools/quic/certs/out/leaf_cert.pem \
  --key_file=net/tools/quic/certs/out/leaf_cert.pkcs8
```


In a second terminal:<br />
```make host-h2```<br />
```python3 quicWebTest.py 1 ```<br />
```python3 quicVideoTest.py 1 ```<br />



