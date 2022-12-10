# from http.server import HTTPServer,SimpleHTTPRequestHandler
# import ssl

# httpd = HTTPServer(('0.0.0.0', 8888), SimpleHTTPRequestHandler)
# # Since version 3.10: SSLContext without protocol argument is deprecated. 
# sslctx = ssl.SSLContext()
# #sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# sslctx.minimum_version = ssl.TLSVersion.TLSv1_3
# sslctx.maximum_version = ssl.TLSVersion.TLSv1_3
# sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
# sslctx.load_cert_chain(keyfile="/workdir/temp/certificates/private.key", certfile="/workdir/temp/certificates/selfsigned.crt")
# httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
# httpd.serve_forever()


#openssl s_client -cert /workdir/temp/certificates/selfsigned.crt -key /workdir/temp/certificates/private.key -connect 10.0.0.1:8888


from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl


httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="/workdir/10.0.0.1-key.pem", 
        certfile='/workdir/10.0.0.1.pem', server_side=True)

httpd.serve_forever()
