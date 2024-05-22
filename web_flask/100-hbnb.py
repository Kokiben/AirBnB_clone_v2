#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session after each reqst"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a HTML page like"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    ames = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states, amenities=ames, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
