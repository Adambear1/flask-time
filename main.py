import os
from time import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_unix():
    unix = int(time())
    return str(unix)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)