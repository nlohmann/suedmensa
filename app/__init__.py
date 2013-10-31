# everything for Flask
from flask import Flask, Response
from flask.ext.cache import Cache

# Suedmensa
import json
from suedmensa.menu import getmenu

# the Flask app
app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route("/")
@cache.cached(timeout=120)
def menu():
    menu = response=json.dumps(getmenu(), indent=4)
    resp = Response(menu, status=200, mimetype="application/json")
    return resp

if __name__ == "__main__":
    app.run()
