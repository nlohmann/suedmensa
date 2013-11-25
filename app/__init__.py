# coding: utf8

# everything for Flask
from flask import Flask, Response, url_for, render_template, request, redirect
from flask.ext.cache import Cache
from flask.ext.compress import Compress
from werkzeug.contrib.atom import AtomFeed
import iso8601
import datetime
import locale
import urllib

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

# Suedmensa
import json
from menu import getmenu

# the Flask app
app = Flask(__name__)
app.debug = True

# remove some whitespace in the templated code
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# set cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# enable gzip compression
Compress(app)

@app.route("/")
@app.route("/<mensa>")
def menu_negotiate(mensa='suedmensa'):
    if request.accept_mimetypes.best == 'application/json':
        return menu_json(mensa)
    elif request.accept_mimetypes.best == 'application/atom+xml':
        return menu_atom(mensa)
    elif request.accept_mimetypes.best == 'application/image/png':
        return menu_png(mensa)
    else:
        return menu_html(mensa)

@app.route("/<mensa>.html")
@cache.cached(timeout=120)
def menu_html(mensa):
    menu = getmenu(mensa)
    return render_template('menu.html', menu=menu)

@app.route("/<mensa>.json")
@cache.cached(timeout=120)
def menu_json(mensa):
    menus = getmenu(mensa)
    status = int(menus['status'])
    if status == 200:
        menus['href'] = url_for('menu_json', mensa=mensa, _external=True)
    payload = json.dumps(menus, indent=4, sort_keys=True).decode('unicode-escape').encode('utf-8')
    return Response(payload, status=status, mimetype="application/json; charset=utf-8")

@app.route('/<mensa>.atom')
@cache.cached(timeout=120)
def menu_atom(mensa):
    menu = getmenu(mensa)
    menudate = iso8601.parse_date(menu['datum'])

    feed = AtomFeed(title=menu['name'],
                    title_type='text',
                    subtitle=u'Täglicher Speiseplan der %s.' % menu['name'],
                    subtitle_type='text',
                    author=[
                        {
                            "name": "Studentenwerk Rostock (Rohdaten)",
                            "uri": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=109"
                        },
                        {
                            "name": "Niels Lohmann (Feed)",
                            "email": "niels.lohmann@gmail.com"
                        }
                    ],
                    links=[
                        {
                            "href": "https://twitter.com/%s" % menu['twitter'],
                            "title": "%s auf Twitter" % menu['name'],
                            "hreflang": "de-DE"
                        }
                    ],
                    updated=menudate,
                    url=url_for('menu_html', mensa=mensa, _external=True),
                    icon=url_for('static', filename='%s/favicon-256.png' % mensa, _external=True),
                    feed_url=request.url)

    feed.add(title='Speiseplan %s' % datetime.datetime.strftime(menudate, "%A, %d.%m.%Y"),
             title_type='text',
             content=render_template('atom.html', menu=menu),
             content_type='html',
             summary=u'Speiseplan der %s für den %s' % (menu['name'], datetime.datetime.strftime(menudate, "%A, %d.%m.%Y")),
             summary_type='text',
             author=[
                 {
                     "name": "Studentenwerk Rostock (Rohdaten)",
                     "uri": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=109"
                 },
                 {
                     "name": "Niels Lohmann (Feed)",
                     "email": "niels.lohmann@gmail.com"
                 }
             ],
             url=menu['url'],
             updated=menudate,
             published=menudate)

    return feed.get_response()

@app.route("/<mensa>.png")
@cache.cached(timeout=120)
def menu_png(mensa):
    img = urllib.urlopen("https://dl.dropboxusercontent.com/u/3658551/suedmensa/%s.png" % mensa).read()
    return Response(img, mimetype="image/png")

@app.route("/<mensa>-pic.html")
@cache.cached(timeout=120)
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
        "vital": u"Vitaltheke",
        "beilagen": u"Sättigungsbeilagen"
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
        "vital": u"Vital",
        "beilagen": u"Beilagen"
    }
    return names[s]

if __name__ == "__main__":
    app.run()
