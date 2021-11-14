from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def all():
    return "The unix time now is {}, (refresh the page for updated time)".format(time.time())


if __name__ == "__main__":
    app.run(host='127.1.0.0', port=8000)
