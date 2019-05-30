import sys
sys.path.append('../')

from flask import Flask, jsonify
import requests
import redis
from common.PikaWrapper import PikaWrapper
import common.configurations as configurations

app = Flask(__name__)
worker_host = 'http://api-worker:5000'
cache = redis.Redis(host='redis', port=6379)
pika_wrapper = PikaWrapper(configurations.rabbit_mq_config['host_name'])


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


@app.route('/comments/add')
def add_comment():
    comment = 'hello world'
    #           '{
    #     #     'value': 'Hello world'
    #     # }

    pika_wrapper.send_message(comment, routing_key=configurations.rabbit_mq_config['comments_queue_name'])

    response = jsonify(success=True)
    return response


def __initialize_queue():
    pika_wrapper.declare_queue(configurations.rabbit_mq_config['comments_queue_name'])


if __name__ == '__main__':
    __initialize_queue()

    app.run(debug=True, host='0.0.0.0')



