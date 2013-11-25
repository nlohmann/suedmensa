#!/usr/bin/env python
# coding: utf8

import bs4
import urllib2
import json
import datetime
import re

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

def getweek(link):
    # get the menu url from the index page
    baseurl = 'http://www.studentenwerk-rostock.de'
    url = baseurl + link

    # load and parse week plan
    html = urllib2.urlopen(url=url, timeout=10).read()
    soup = bs4.BeautifulSoup(html, "lxml")

    # get the table after the one that says "download as Excel": this table
    # contains the menu
    tables = soup.find_all('table')
    table_index = 0
    for table_index in range(len(tables)-1,0,-1):
        if "Download als MS-Excel-Dokument" in tables[table_index].text:
            break

    # this table contains the menu
    menu_raw = tables[table_index+1]

    # replace the 'VITALTHEKE' icon with text
    pic = '<img border="0" src="../../grafiken/webseite/de/vital_theke_100.jpg"/>'
    menu_raw = str(menu_raw).replace(pic, "VITALTHEKE")

    # re-parse the edited menu
    menu_raw = bs4.BeautifulSoup(menu_raw, "lxml")

    data = [[], [], [], [], [], []]

    for line in menu_raw.findAll('tr'):
        rows = line.findAll('td')
        for row in range(len(rows)):
            if len(rows[row].text) > 1:
                data[row].append(rows[row].text.strip())

    return data


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
    url = baseurl + '/index.php?lang=de&mainmenue=4&submenue=48'

    # load and parse the menu website
    try:
        html = urllib2.urlopen(url=url, timeout=10).read()
    except urllib2.URLError as e:
        # abort if server times out or is unreachable
        return {"status": 503, "error": "server not reachable"}

    soup = bs4.BeautifulSoup(html, "lxml")
    menu_links = soup.find_all('a', { "class" : "link_text" })

    for menu_link in menu_links:
        if menu_link['href'] != None:
            print "get menu"
            menu = getweek(menu_link['href'])
            print json.dumps(menu, indent=2)

            print [int(x) for x in re.findall(r'\d+', menu_link.text)]
            
            #break
    
    return "done"

if __name__ == "__main__":
    print json.dumps(getmenu('suedmensa'), indent=2, sort_keys=True)
