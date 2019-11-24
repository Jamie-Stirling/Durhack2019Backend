import socket
import os
import json
import requests
url ="http://api.openweathermap.org/data/2.5/weather?q=London?"
def login_page():
    # get the hostname
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    # POST with JSON

    r = requests.get(url)

    # Response, status etc
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    conn.send(r.encode())
login_page()