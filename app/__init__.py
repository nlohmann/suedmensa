# everything for Flask
from flask import Flask, Response
from flask.ext.cache import Cache
from flask.ext.compress import Compress

# Suedmensa
import json
from menu import getmenu

# the Flask app
app = Flask(__name__)

# set cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# enable compression
Compress(app)

@app.route("/<mensa>")
@cache.cached(timeout=120)
def menu(mensa):
    try:
        menu = json.dumps(getmenu(mensa), indent=4).decode('unicode-escape').encode('utf-8')
        resp = Response(menu, status=200, mimetype="application/json; charset=utf-8")
    except:
        error = {"error": "Mensa is unknown."}
        resp = Response(json.dumps(error), status=400, mimetype="application/json; charset=utf-8")

    return resp

if __name__ == "__main__":
    app.run()
