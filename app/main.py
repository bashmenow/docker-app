from flask import Flask, request
import requests
import redis

cache = redis.StrictRedis( host='redis', port=6379, db=0 )
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, custom docker!"

@app.route('/ip', methods=['GET'])
def get_ip():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ptr = cache.get(ip)
    if ptr is None:
        print("miss cache get http request....", flush=True)
        r = requests.get('http://resolver:8000/' + ip)
        ptr = r.content.decode('utf-8')
        cache.set(ip, ptr)
    else:
        ptr = ptr.decode('utf-8')
    header = '<html><head><title>Resolver APP</title></head><body>'
    body =  f'''<p>Your ip address is:  {ip}
                <p>PTR record is:  {ptr}'''
    footer = '</body></html>'
    return header + body + footer

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)