from flask import Flask
import requests

app = Flask(__name__)
worker_host = 'http://worker:5000'


@app.route('/')
def hello_world():
    # async/await?
    response = requests.get(worker_host)
    return response.text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

