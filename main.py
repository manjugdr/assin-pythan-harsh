from flask import Flask
import socket, os

app = Flask(_name_)
@app.route('/')
def prinf_ip():
    hostname = socket.gethostname()
    localip = socket.hethostbyname(hostname)
    return localip

if__name_== "__main__":
    app.run(debug=True="0.0.0.0", port=80)
