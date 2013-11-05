#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tweepy
import os
import random
random.seed()

from menu import getmenu

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


CREDENTIALS = json.load(open(os.path.join(__location__, 'credentials_kleineulme.json'), 'r'))

m = getmenu('kleineulme')

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
    l = [shorten(x['name'].encode('utf-8')) for x in theke]
    return " | ".join(l)

tweet1 = "VITAL: %s ‖ %s!" % (tweets(m['theken']['vital']), bon_appetit())
tweet2 = "THEKE 2: %s" % tweets(m['theken']['theke2'])
tweet3 = "THEKE 1: %s" % tweets(m['theken']['theke1'])

tweets = [cap_length(tweet1), cap_length(tweet2), cap_length(tweet3)]

auth = tweepy.OAuthHandler(CREDENTIALS['CONSUMER_KEY'], CREDENTIALS['CONSUMER_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'], CREDENTIALS['ACCESS_SECRET'])
api = tweepy.API(auth)

for tweet in tweets:
    print tweet
    #api.update_status(tweet)
