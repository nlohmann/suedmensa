#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
random.seed()

from suedmensa.menu import getmenu

m = getmenu()

#m = {
#  "datum": "30.10.2013", 
#  "aktion": [
#    "Coq au Vin - H\u00e4hnchen in Rotwein und Pilzen (L-)"
#  ], 
#  "pasta": [
#    "Tomatenso\u00dfe mit Rucola (vegan) (L-)", 
#    "Puten-Curry-So\u00dfe"
#  ], 
#  "vital": [
#    "Grie\u00dfsuppe mit Basilikum", 
#    "Chicken Tikka masala (ind. H\u00e4hnchen-Curry)", 
#    "Bolognese mit Rinderhackfleisch", 
#    "Nudelpfanne mit Gem\u00fcse (L-) (vegan)", 
#    "Falafel mit Dip (vegan)", 
#    "K\u00e4seschnitzel (fleischlos)"
#  ], 
#  "theke1": [
#    "Kartoffel-Gem\u00fcseauflauf"
#  ], 
#  "theke2": [
#    "Steak mit Tomate und Mozzarella \u00fcberbacken", 
#    "griechisches Hacksteak", 
#    "Fischfilet, P\u00fcree mit Sellerie (Tagestipp)"
#  ]
#}
#
#m = {
#    "datum": "31.10.2013", 
#    "aktion": [], 
#    "pasta": [], 
#    "vital": [], 
#    "theke1": [], 
#    "theke2": [], 
#    "kommentar": "Feiertag"
#}

if 'kommentar' in m:
    print m['kommentar']

shorten_list = [
    ('PASTASOßE', 'Soße'),
    ('TAGESTIPP: ', ''),
    ('(ind. Hähnchen-Curry)', ''),
    ('(Preisvorteil 0,50 €)', ''),
    (' mit ', '+'),
    (' in ', '+'),
    (' im ', '+'),
    (' an ', '+'),
    (' auf ', '+'),
    (' und ', '+'),
    ('/', '/'),
    (' - ', ': '),
    ('süss', 'süß'),
    ('zwei ', '2 '),
    ('Preiselbeeren', 'Preiselb.'),
    ('drei ', '3 '),
    ('vier ', '4 '),
    ('(L-)', ''),
    ('(L+)', ''),
    ('(vegan)', ''),
    ('(Tagestipp)', ''),
    ('(fleischlos)', ''),
    ('pfanne', 'pf.'),
    ('Tomaten', 'Tom.'),
    ('Hähnchen', 'Hähn.'),
    ('hähnchen', 'hähn.'),
    ('hausgemachte', 'hausg.'),
    ('mediterranes', 'medit.'),
    ('mediterranem', 'medit.'),
    ('panade', 'pan.'),
    ('suppe', 'sup.'),
    ('Suppe', 'Sup.'),
    ('chinesisches', 'chin.'),
    ('chinesische', 'chin.'),
    ('hackfleisch', 'hackfl.'),
    ('grünen', 'gr.'),
    ('wahlweise', ''),
    ('streifen', ''),
    ('gebacken', 'geb.'),
    ('gebraten', 'gebr.'),
    (' / ', '/'),
    (' +', '+')
]

def bon_appetit():
    # de, fr, sp, ru, hy, en, is, ca, nl, fa
    # ro, sv, sw, pl, zh, eo, et, fi, el, he
    # ja, la, lv, pt, cs, tr
    appetit = ['Guten Appetit', 'Buon appetito', 'Buen provecho',
               'приятного аппетита', 'բարի ախորժակ', 'Enjoy your meal',
               'Verði þér að góðu', 'Bon profit', 'Eet smakelijk', 'نوش جان',
               'Poftă bună', 'Smaklig måltid', 'Karibu chakula', 'Smacznego',
               '慢慢吃', 'Bonan apetiton', 'Labu apetiti', 'Hyvää ruokahalua',
               'καλή όρεξη', 'בתיאבון', ' 戴きます', 'Bene sapiat',
               'Labu apetīti', 'Bom apetite', 'Dobrou chuť', 'Afiyet olsun']
    return appetit[random.randint(0, len(appetit)-1)]

def cap_length(tweet):
    """
    Shortens the tweet to 140 characters.
    """
    if len(tweet) > 140:
        return tweet[0:137]+'…'
    else:
        return tweet

def shorten(entry):
    for x in shorten_list:
        entry = entry.replace(x[0], x[1])
    entry = entry.replace("  ", " ")
    return entry.strip()

def tweets(theke):
    l = [shorten(x.encode('utf-8')) for x in theke]
    return " | ".join(l)

tweet1 = "THEKE 1: %s ‖ PASTA: %s ‖ AKTION: %s" % (tweets(m['theke1']), tweets(m['pasta']), tweets(m['aktion']))
tweet2 = "VITAL: %s" % tweets(m['vital'])
tweet3 = "THEKE 2: %s ‖ %s!" % (tweets(m['theke2']), bon_appetit())

print cap_length(tweet1)
print cap_length(tweet2)
print cap_length(tweet3)

