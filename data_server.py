from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from extract_receipt import process_file
from retirement_plan_calc import handle_request

class KacperHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/processImage":
            try:
                content_length = int(self.headers['Content-Length'])

                #body = self.rfile.read(content_length)
                print(process_file(self.rfile))
                #request = json.loads(body)
                # otherwise, you can pass self.rfile to a png/jpeg decoder
                #print(request)

                response = {  # example response dict
                    "name": "anotherone"
                }

                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except:
                self.send_error(400)
                self.end_headers()

        elif self.path == "/calc":

            try:
                content_length = int(self.headers['Content-Length'])

                body = self.rfile.read(content_length)
                request = json.loads(body.decode())
                response = handle_request(request)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except:
                self.send_error(400)
                self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()


httpd = HTTPServer(('localhost', 3001), KacperHTTPRequestHandler)

httpd.serve_forever()
