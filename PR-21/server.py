from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address=('', 8000)

    class MyHandler(handler_class):
     def do_GET(self):
        if self.path == '/ping':
         self.send_response(200, "PONG")
    
    httpd = server_class(server_address, MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
