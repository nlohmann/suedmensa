# everything for Flask
from flask import Flask, Response, url_for
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

@app.route("/")
@app.route("/<mensa>")
@cache.cached(timeout=120)
def menu(mensa='suedmensa'):
    menus = getmenu(mensa)
    status = int(menus['status'])
    if status == 200:
        menus['href'] = url_for('menu', mensa=mensa, _external=True)
    payload = json.dumps(menus, indent=4).decode('unicode-escape').encode('utf-8')
    return Response(payload, status=status, mimetype="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run()
