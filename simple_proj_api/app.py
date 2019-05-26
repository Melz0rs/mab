from flask import Flask
import requests
import redis

app = Flask(__name__)
worker_host = 'http://worker:5000'
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    # async/await?
    response = requests.get(worker_host)
    app.logger.info("hello world")
    return response.text


@app.route('/notification/add')
def add_notification():
    cache.incr('notifications_count')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

