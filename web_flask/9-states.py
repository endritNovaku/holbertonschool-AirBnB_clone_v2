#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays a html page with states and cities"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html', states=state)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
