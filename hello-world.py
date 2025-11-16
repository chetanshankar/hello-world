from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hi there')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5370), MyHandler)
    print('Server running on port 5370...')
    server.serve_forever()
    