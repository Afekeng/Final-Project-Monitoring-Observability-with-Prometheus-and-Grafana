from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter('requests_total', 'Total number of requests')

@app.route('/')
def hello():
    REQUESTS.inc()
    return "Hello World!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REQUESTS), mimetype=CONTENT_TYPE_LATEST)

app.run(host='0.0.0.0', port=9977)
