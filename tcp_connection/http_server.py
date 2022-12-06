from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('0.0.0.0', 8889), SimpleHTTPRequestHandler)
# Since version 3.10: SSLContext without protocol argument is deprecated. 
# sslctx = ssl.SSLContext()
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
sslctx.minimum_version = ssl.TLSVersion.TLSv1_3
sslctx.maximum_version = ssl.TLSVersion.TLSv1_3
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='mycert.pem',keyfile = 'mycert.pem')
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
