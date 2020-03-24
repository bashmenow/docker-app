from flask import Flask
import requests
app = Flask(__name__)

from flask import request

@app.route('/')
def index():
    return "Hello, custom docker!"

@app.route('/ip', methods=['GET'])
def get_ip():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    r = requests.get('http://resolver:8000/' + ip)
    ptr = r.content
    header = '<html><head><title>Resolver APP</title></head><body>'
    body =  f'''<p>Your ip address is:  {ip}
                <p>PTR record is:  {ptr}'''
    footer = '</body></html>'
    return header + body + footer

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)