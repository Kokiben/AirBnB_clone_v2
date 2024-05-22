#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session after each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list"""
    states = storage.all(State)
    s_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=s_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
