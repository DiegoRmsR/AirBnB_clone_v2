#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
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
    """route that diplay n if is an integer"""
    return (str(n) + " is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """route that diplay a HTML page n if is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """route that diplay a HTML page n if is an integer"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
