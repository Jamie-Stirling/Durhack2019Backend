import http.server
import socketserver
import json

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

PYtotal_saved = json.loads(total_saved)
PYtotal_worth = json.loads(total_worth)