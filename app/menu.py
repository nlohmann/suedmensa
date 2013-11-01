#!/usr/bin/env python

import bs4
import urllib2
import json

def getmenu(mensa):
    """
    Returns the current menu as dictionary.
    """

    # build the url from the given mensa
    baseurl = "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2="
    detailurls = {
        "suedmensa": "8432",
        "stgeorg": "8437",
        "kleineulme": "8444",
        "ulme69": "8443",
        "einstein": "8431"
    }
    url = baseurl + detailurls[mensa]

    # load and parse the menu website
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
        "url": url,
        "theken": {}
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

        if item == 'THEKE 3':
            theke = 'theke3'
            praedikat = ''
            continue

        # deal also with "VITALTHEKE (Theke 2)"
        if item[0:10] == 'VITALTHEKE':
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

        # deal with mensas with only one (unnamed) counter
        if theke == "":
            theke = "theke1"

        # add entry to current counter
        if not theke in menu["theken"]:
            menu["theken"][theke] = []
        menu["theken"][theke].append((item + praedikat))

    return menu

if __name__ == "__main__":
    print json.dumps(getmenu('suedmensa'), indent=2)
