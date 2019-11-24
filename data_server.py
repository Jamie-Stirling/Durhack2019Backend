from extract_receipt import process_file
from retirement_plan_calc import handle_request
import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/processImage", methods=["POST"])
def hello():
    image = request.data
    response = process_file(image)
    return jsonify(response)


@app.route("/calc", methods=["POST"])
def anothr_one():
    print(request.json)
    response = handle_request(request.json)
    print(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=3001, debug=True)

# class KacperHTTPRequestHandler(BaseHTTPRequestHandler):
#
#     def do_POST(self):
#         if self.path == "/processImage":
#             # try:
#             content_length = int(self.headers['Content-Length'])
#             body = self.rfile.read(content_length)
#
#             response = process_file(body)
#             response_body = json.dumps(response).encode()
#
#             print(response_body)
#
#             self.send_response(200)
#             self.send_header('Access-Control-Allow-Credentials', 'true')
#             self.send_header('Access-Control-Allow-Origin', 'http://localhost:3001')
#             self.send_header("Content-Type", "application/json")
#             # self.send_header("Content-Length", str(len(response_body)))
#             self.send_header("Accept-Ranges", "bytes")
#             self.end_headers()
#
#             self.wfile.write(response_body)
#             self.wfile.close()
#             #     print(str(e))
#             #     self.send_error(400)
#             #     self.end_headers()
#             # except Exception as e:
#
#         elif self.path == "/calc":
#
#             try:
#                 content_length = int(self.headers['Content-Length'])
#                 body = self.rfile.read(content_length)
#
#                 request = json.loads(body.decode())
#                 response = handle_request(request)
#                 response_body = json.dumps(response).encode()
#
#                 self.send_response(200)
#                 self.send_header('Access-Control-Allow-Credentials', 'true')
#                 self.send_header('Access-Control-Allow-Origin', 'http://localhost:3001')
#                 self.send_header("Content-Type", "application/json")
#                 self.send_header("Content-Length", str(len(response_body)))
#                 self.send_header("Accept-Ranges", "bytes")
#                 self.end_headers()
#
#
#                 self.wfile.write(response_body)
#                 self.wfile.close()
#             except Exception as e:
#                 print(e)
#                 self.send_error(400)
#                 self.end_headers()
#
#         else:
#             self.send_response(404)
#             self.end_headers()
#     # def do_OPTIONS(self):
#     #     self.send_response(200, "ok")
#     #     self.send_header('Access-Control-Allow-Credentials', 'true')
#     #     self.send_header('Access-Control-Allow-Origin', 'http://localhost:3001')
#     #     self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
#     #     self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
#     #     self.end_headers()


# httpd = HTTPServer(('localhost', 3001), KacperHTTPRequestHandler)

# httpd.serve_forever()
