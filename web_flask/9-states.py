#!/usr/bin/python3
"""Module with a flask script"""
from models import storage
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Method closes storage"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Returns a template"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, found=True)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_states(id):
    """Returns a template"""
    found = False
    cities = True
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            found = True
            return render_template(
                    '9-states.html', state=state, cities=cities, found=found)
    if not found:
        return render_template('9-states.html', found=found)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
