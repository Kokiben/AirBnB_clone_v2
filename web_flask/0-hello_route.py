#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False  # Set globally for all routes


@app.route('/', strict_slashes=False)  # Route definition
def hello_hbnb():
    """Returns the content of the / route."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # Correctly running app
