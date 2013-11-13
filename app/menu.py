#!/usr/bin/env python

import bs4
import urllib2
import json
import datetime

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
        html = urllib2.urlopen(url).read()
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

    # convert the date
    datestring = datetime.datetime.strptime(menu_list[0].split()[-1], "%d.%m.%Y").date().isoformat()

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

        if line == 'PASTATHEKE':
            theke = 'pasta'
            praedikat = ''
            continue

        if line[0:10] == 'PASTASAUCE':
            theke = 'pasta'
            praedikat = ''
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

            #menu["theken"][theke].append((line + praedikat))

    return menu

if __name__ == "__main__":
    print json.dumps(getmenu('suedmensa'), indent=2)
