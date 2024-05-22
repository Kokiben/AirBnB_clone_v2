#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage session after each rqst"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like"""
    states = storage.all(State).values()
    ames = storage.all(Amenity).values()

    s_sts = sorted(states, key=lambda state: state.name)
    s_ames = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=s_sts, ames=s_ames)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
