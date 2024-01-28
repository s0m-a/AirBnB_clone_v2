#!/usr/bin/python3
"""Module with flask script"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method returns Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
