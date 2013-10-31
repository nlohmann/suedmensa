#!/usr/bin/env python

import bs4
import urllib2
import json

def getmenu():
    """
    Returns the current menu as dictionary.
    """

    # load and parse the menu website
    url = ("http://www.studentenwerk-rostock.de/index.php?lang=de"
           "&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8432")
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "lxml")

    # the 21st table contains the menu
    menu_raw = soup.find_all('table')[21]

    # replace the 'VITALTHEKE' icon with text
    pic = '<img border="0" src="../../grafiken/webseite/de/vital_theke_100.jpg"/>'
    menu_raw = str(menu_raw).replace(pic, "VITALTHEKE")

    # re-parse the edited menu
    menu_raw = bs4.BeautifulSoup(menu_raw, "lxml")

    # translate into list; remove empty lines
    menu_list = [x for x in menu_raw.text.split('\n') if x != '']

    # the structure of the return object
    menu = {
        "datum": menu_list[0].split()[-1],
        "theke1": [],
        "theke2": [],
        "vital": [],
        "aktion": [],
        "pasta": [],
        "url": url
    }

    # in case of holidays, return commented, empty menu
    if menu_list[1] == 'Feiertag':
        menu["kommentar"] = 'Feiertag'
        return menu

    theke = ''
    praedikat = ''

    for item in menu_list[1:]:
        item = item.strip()

        if item == 'THEKE 1':
            theke = 'theke1'
            praedikat = ''
            continue

        if item == 'THEKE 2':
            theke = 'theke2'
            praedikat = ''
            continue

        if item == 'VITALTHEKE':
            theke = 'vital'
            praedikat = ''
            continue

        if item == 'AKTIONSTHEKE':
            theke = 'aktion'
            praedikat = ''
            continue

        if item == 'PASTATHEKE':
            theke = 'pasta'
            praedikat = ''
            continue

        if item == 'vegan':
            praedikat = ' (vegan)'
            continue

        if item == 'fleischlos':
            praedikat = ' (fleischlos)'
            continue

        i = item.find("(Preisvorteil")
        if i != -1:
            item = item[0:i]

        if "TAGESTIPP: " in item:
            item = item[11:] + "(Tagestipp)"

        menu[theke].append((item + praedikat))

    return menu

if __name__ == "__main__":
    print json.dumps(getmenu(), indent=2)
