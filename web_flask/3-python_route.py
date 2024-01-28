#!/usr/bin/python3
"""Module with a flask script"""
from flask import Flask, escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Method  returns a str  with a variable"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False, defaults={"text": "is_cool"})
def python_text(text):
    """Method  returns a str with a variable"""
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
