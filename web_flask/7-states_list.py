#!/usr/bin/python3
"""starts a Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list"""
    states = storage.all(State)
    s_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=s_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
