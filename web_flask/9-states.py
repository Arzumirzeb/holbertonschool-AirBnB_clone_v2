#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    n = storage.all(State)
    if not id:
        return render_template('7-states_list.html', n=n.values())
    key = f'State.{id}'
    state = None
    try:
        state = n[key]
    except KeyError:
        pass
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
