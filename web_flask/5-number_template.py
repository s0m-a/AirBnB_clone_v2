#!/usr/bin/python3
"""Module with a flask script"""
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method  returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Method  returns a str with a variable"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False, defaults={"text": "is_cool"})
def python_text(text):
    """Method  returns a str with a variable"""
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Method returns a str with a num"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """Method returns a template"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
