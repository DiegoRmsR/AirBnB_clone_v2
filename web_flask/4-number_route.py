#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """route / that display Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route /hbnb that display HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def d_text(text):
    """route /c/<text> that display C + text"""
    text = text.replace('_', ' ')
    return ("C " + text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """route that display Python + text"""
    text = text.replace('_', ' ')
    return ("Python " + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """route that siplay n if is an integer"""
        return (str(n) + "is a number")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
