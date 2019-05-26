from flask import Flask, jsonify
import requests
import redis

app = Flask(__name__)
worker_host = 'http://api-worker:5000'
cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
    # async/await?
    response = requests.get(worker_host)
    app.logger.info("hello world")
    return response.text


@app.route('/notifications/add')
def add_notification():
    app.logger.info("adding notification")
    cache.incr('notifications_count')

    response = jsonify(success=True)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

