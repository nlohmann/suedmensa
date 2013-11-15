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
    payload = json.dumps(menus, indent=4, sort_keys=True).decode('unicode-escape').encode('utf-8')
    return Response(payload, status=status, mimetype="application/json; charset=utf-8")

@app.route('/<mensa>.atom')
#@cache.cached(timeout=120)
def menu_atom(mensa):
    menu = getmenu('suedmensa')
    menudate = iso8601.parse_date(menu['datum'])

    feed = AtomFeed(title=menu['name'].encode('ascii', 'xmlcharrefreplace'),
                    title_type='html',
                    updated=menudate,
                    icon=url_for('static', filename='%s/favicon-256.png' % mensa, _external=True),
                    feed_url=request.url, url=request.url_root)

    feed.add(title='Speiseplan %s' % datetime.datetime.strftime(menudate, "%A, %d.%m.%Y"),
             content=render_template('atom.html', menu=menu),
             content_type='html',
             author=u'Studentenwerk Rostock',
             url=menu['url'],
             updated=menudate,
             published=menudate)

    return feed.get_response()

@app.route("/<mensa>-pic.html")
#@cache.cached(timeout=120)
def menu_pic_html(mensa):
    menu = getmenu(mensa)
    return render_template('pics.html', menu=menu)

@app.template_filter('thekenname')
def filter_thekenname(s):
    names = {
        "theke1": u"Theke 1",
        "theke2": u"Theke 2",
        "theke3": u"Theke 3",
        "aktion": u"Aktionstheke",
        "pasta": u"Pastatheke",
        "vital": u"Vitaltheke"
    }
    return names[s]

@app.template_filter('thekennameshort')
def filter_thekennameshort(s):
    names = {
        "theke1": u"Theke 1",
        "theke2": u"Theke 2",
        "theke3": u"Theke 3",
        "aktion": u"Aktion",
        "pasta": u"Pasta",
        "vital": u"Vital"
    }
    return names[s]

if __name__ == "__main__":
    app.run()
