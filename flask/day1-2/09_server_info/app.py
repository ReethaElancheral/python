from flask import Flask, request
import os
import socket

app = Flask(__name__)

@app.route('/')
def server_info():
    ip_address = request.host.split(':')[0]
    port = request.host.split(':')[1] if ':' in request.host else 'Unknown'
    env = os.getenv('FLASK_ENV', 'Not Set')
    
    return f"""
    <h1>Server Info</h1>
    <p><b>IP Address:</b> {ip_address}</p>
    <p><b>Port:</b> {port}</p>
    <p><b>Environment:</b> {env}</p>
    <hr>
    """

@app.route('/status')
def status():
    if app.debug:
        return "<p style='color:green;'>Running in <b>Debug Mode</b></p>"
    else:
        return "<p style='color:red;'>Running in <b>Production Mode</b></p>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
