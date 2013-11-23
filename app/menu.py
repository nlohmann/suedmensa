#!/usr/bin/env python
# coding: utf8

import bs4
import urllib2
import json
import datetime

THEKEN = {
    "theke1": {
        "short": "Theke 1",
        "long": "Theke 1"
    },
    "theke2": {
        "short": "Theke 2",
        "long": "Theke 2"
    },
    "theke3": {
        "short": "Theke 3",
        "long": "Theke 3"
    },
    "aktion": {
        "short": "Aktion",
        "long": "Aktionstheke"
    },
    "pasta": {
        "short": "Pasta",
        "long": "Pastatheke"
    },
    "vital": {
        "short": "Vital",
        "long": "Vitaltheke"
    }
}

MENSEN = {
    "suedmensa": {
        "name": u"Südmensa",
        "color": "#00b2ff",
        "twitter": "suedmensa",
        "foursquare": "4b54317cf964a52041b427e3"
    },
    "stgeorg": {
        "name": u"Mensa St.-Georg-Straße",
        "color": "#ffe900",
        "twitter": "mensastgeorg",
        "foursquare": "4c612da4048b9521cc654278"
    },
    "kleineulme": {
        "name": "Kleine Mensa Ulme",
        "color": "#92ec00",
        "twitter": "kleineulme",
        "foursquare": "4e450efc1f6e0a1ba5e4bc84"
    },
    "ulme69": {
        "name": "Mensa Ulme 69",
        "color": "#d8005f",
        "twitter": "ulme69",
        "foursquare": "4e96b65b9adf7f572e0908f4"
    },
    "einstein": {
        "name": "Campus Cafeteria Einstein",
        "color": "#ffa500",
        "twitter": "campuseinstein",
        "foursquare": "51b1b494498ee6881086d1d0"
    }
}

# 

def getmenu(mensa):
    """
    Returns the current menu as dictionary.
    """

    # the known mensas
    detailurls = {
        "suedmensa": 0,
        "stgeorg": 1,
        "kleineulme": 2,
        "ulme69": 3,
        "einstein": 4
    }

    # abort if mensa is unknown
    if not mensa in detailurls:
        return {"status": 400, "error": "mensa unknown"}

    # get the menu url from the index page
    baseurl = 'http://www.studentenwerk-rostock.de'
    url = baseurl + '/index.php?lang=de&mainmenue=4&submenue=47'

    # load and parse the menu website
    try:
        html = urllib2.urlopen(url=url, timeout=10).read()
    except urllib2.URLError as e:
        # abort if server times out or is unreachable
        return {"status": 503, "error": "server not reachable"}

    soup = bs4.BeautifulSoup(html, "lxml")
    menu_links = soup.find_all('a', { "class" : "link_text" })

    # abort if no menus found
    if not menu_links:
        return {"status": 502, "error": "no menus found"}

    # select the chosen mensa menu link (ordered as on the index page)
    url = baseurl + menu_links[detailurls[mensa]]['href']

    # load and parse the menu website
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "lxml")

    # find the last table the contains the word "Speiseplan"
    tables = soup.find_all('table')
    table_index = 0
    for table_index in range(len(tables)-1,0,-1):
        if "Speiseplan" in tables[table_index].text:
            break

    # this table contains the menu
    menu_raw = soup.find_all('table')[table_index]

    # replace the 'VITALTHEKE' icon with text
    pic = '<img border="0" src="../../grafiken/webseite/de/vital_theke_100.jpg"/>'
    menu_raw = str(menu_raw).replace(pic, "VITALTHEKE")

    # re-parse the edited menu
    menu_raw = bs4.BeautifulSoup(menu_raw, "lxml")

    # translate into list; remove empty lines
    menu_list = [x for x in menu_raw.text.split('\n') if x != '']

    try:
        # convert the date
        datestring = datetime.datetime.strptime(menu_list[0].split()[-1], "%d.%m.%Y").date().isoformat()
    except:
        return {"status": 502, "error": "no menus found"}

    # the structure of the return object
    menu = {
        "datum": datestring,
        "url": url,
        "mensa": mensa,
        "theken": {},
        "status": 200
    }

    # in case of holidays, return commented, empty menu
    if menu_list[1] == 'Feiertag':
        menu["kommentar"] = 'Feiertag'
        return menu

    theke = ''
    praedikat = ''

    for line in menu_list[1:]:
        line = line.strip()

        if line == 'THEKE 1':
            theke = 'theke1'
            praedikat = ''
            continue

        if line == 'THEKE 2':
            theke = 'theke2'
            praedikat = ''
            continue

        if line == 'THEKE 3':
            theke = 'theke3'
            praedikat = ''
            continue

        # deal also with "VITALTHEKE (Theke 2)"
        if line[0:10] == 'VITALTHEKE':
            theke = 'vital'
            praedikat = ''
            continue

        if line == 'AKTIONSTHEKE':
            theke = 'aktion'
            praedikat = ''
            continue

        if line in ['PASTATHEKE', u'PASTASOßE', "PASTASAUCE"]:
            theke = 'pasta'
            praedikat = ''
            continue

        if line == 'KINDERTELLER' or line == 'freie Auswahl (halbe Portion)':
            continue

        if line == 'vegan':
            praedikat = ' (vegan)'
            continue

        if line == 'fleischlos':
            praedikat = ' (fleischlos)'
            continue

        i = line.find("(Preisvorteil")
        if i != -1:
            line = line[0:i]

        if "TAGESTIPP: " in line:
            line = line[11:] + "(Tagestipp)"

        # deal with mensas with only one (unnamed) counter
        if theke == "":
            theke = "theke1"

        # add entry to current counter
        if not theke in menu["theken"]:
            menu["theken"][theke] = []

        # add to list if not empty
        if line != '':
            meal = dict()

            if '(fleischlos)' in praedikat:
                meal['vegetarisch'] = True
            if '(vegan)' in praedikat:
                meal['vegan'] = True
            if '(Tagestipp)' in line:
                line = line.replace('(Tagestipp)', '').strip()
                meal['tagestipp'] = True
            if '(L-)' in line:
                line = line.replace('(L-)', '').strip()
                meal['laktosefrei'] = True

            meal['name'] = line
            menu["theken"][theke].append(meal)

    # move further predicates
    for theke in menu['theken']:
        for meal in menu['theken'][theke]:
            if '(vegan)' in meal['name']:
                meal['name'] = meal['name'].replace('(vegan)', '')
                meal['name'] = meal['name'].replace('  ', ' ')
                meal['name'] = meal['name'].strip()
                meal['vegan'] = True

    # add global information
    menu['name'] = MENSEN[mensa]['name']
    menu['twitter'] = MENSEN[mensa]['twitter']
    menu['foursquare'] = MENSEN[mensa]['foursquare']
    menu['color'] = MENSEN[mensa]['color']

    return menu

if __name__ == "__main__":
    print json.dumps(getmenu('suedmensa'), indent=2, sort_keys=True)
