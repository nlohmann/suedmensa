# coding: utf8

# everything for Flask
from flask import Flask, Response, url_for, render_template, request
from flask.ext.cache import Cache
from flask.ext.compress import Compress
from werkzeug.contrib.atom import AtomFeed
import iso8601
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

# Suedmensa
import json
from menu import getmenu

# the Flask app
app = Flask(__name__)
app.debug = True

# set cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# enable compression
Compress(app)

@app.route("/")
@app.route("/<mensa>")
def menu_negotiate(mensa='suedmensa'):
    if request.accept_mimetypes.best == 'application/json':
        return menu_json(mensa)
    elif request.accept_mimetypes.best == 'application/atom+xml':
        return menu_atom(mensa)
    else:
        return menu_html(mensa)

@app.route("/<mensa>.html")
#@cache.cached(timeout=120)
def menu_html(mensa):
    menu = getmenu(mensa)
    return render_template('menu.html', menu=menu)

@app.route("/<mensa>.json")
#@cache.cached(timeout=120)
def menu_json(mensa):
    menus = getmenu(mensa)
    status = int(menus['status'])
    if status == 200:
        menus['href'] = url_for('menu_json', mensa=mensa, _external=True)
    payload = json.dumps(menus, indent=4).decode('unicode-escape').encode('utf-8')
    return Response(payload, status=status, mimetype="application/json; charset=utf-8")

@app.route('/<mensa>.atom')
#@cache.cached(timeout=120)
def menu_atom(mensa):
    feed = AtomFeed(mensaname(mensa).encode('ascii', 'xmlcharrefreplace'),
                    feed_url=request.url, url=request.url_root)
    menu = getmenu('suedmensa')
    menudate = iso8601.parse_date(menu['datum'])

    feed.add('Speiseplan %s' % datetime.datetime.strftime(menudate, "%A, %d.%m.%Y"), render_template('atom.html', menu=menu),
             content_type='html',
             author=u'Studentenwerk Rostock',
             url=menu['url'],
             updated=menudate,
             published=menudate,
             )
    return feed.get_response()


@app.template_filter('mensaname')
def mensaname(s):
    names = {
        "suedmensa": u"Südmensa",
        "stgeorg": u"Mensa St.-Georg-Straße",
        "kleineulme": u"Kleine Mensa Ulme",
        "ulme69": u"Mensa Ulme 69",
        "einstein": u"Campus Cafeteria Einstein"
    }
    return names[s]

@app.template_filter('thekenname')
def thekenname(s):
    names = {
        "theke1": u"Theke 1",
        "theke2": u"Theke 2",
        "theke3": u"Theke 3",
        "aktion": u"Aktionstheke",
        "pasta": u"Pastatheke",
        "vital": u"Vitaltheke"
    }
    return names[s]

@app.template_filter('twitter')
def twitter(s):
    names = {
        "suedmensa": "suedmensa",
        "stgeorg": "mensastgeorg",
        "kleineulme": "kleineulme",
        "ulme69": "ulme69",
        "einstein": "campuseinstein"
    }
    return names[s]

@app.template_filter('foursquare')
def foursquare(s):
    names = {
        "suedmensa": "4b54317cf964a52041b427e3",
        "stgeorg": "4c612da4048b9521cc654278",
        "kleineulme": "4e450efc1f6e0a1ba5e4bc84",
        "ulme69": "4e96b65b9adf7f572e0908f4",
        "einstein": "51b1b494498ee6881086d1d0"
    }
    return names[s]

if __name__ == "__main__":
    app.run()
