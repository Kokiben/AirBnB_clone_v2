#!/usr/bin/python3
"""print for starts a Flask web app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbn():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_tex(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_pyt_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def sh_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def nbr_template(n):
    return render_template('number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def nmbr_odd_or_even(n):
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', number=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
