import os
import redis
from flask import Flask, request

app = Flask(__name__)
r = redis.Redis(host=os.environ.get('REDIS_URL', 'http://localhost:6379'))

@app.route('/', methods=['GET'])
def get_value():
    key = request.args.get('key')
    return r.get(key) or 'No value found'


@app.route('/', methods=['POST'])
def set_value():
    key = request.args.get('key')
    value = request.args.get('value')
    if key and value:
        r.set(key, value)
    return 'Saved'
