#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tweepy
import os
import random
import sys

from menu import getmenu

random.seed()
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

MENSA = sys.argv[1]

CREDENTIAL_FILE = {
    "suedmensa": "credentials_suedmensa.json",
    "stgeorg": "credentials_mensastgeorg.json",
    "kleineulme": "credentials_kleineulme.json",
    "ulme69": "credentials_ulme69.json",
    "einstein": "credentials_campuseinstein.json"
}

CREDENTIALS = json.load(open(os.path.join(__location__, CREDENTIAL_FILE[MENSA]), 'r'))

def bon_appetit():
    """
    Add "Good appetite!" in one of 36 langugages.
    """
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
    if len(tweet) >= 140:
        return tweet[0:139]+'…'
    else:
        return tweet

def shorten(entry):
    """
    Shorten a tweet based on some patterns.
    """
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
        (', ', ','),
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
        ('paniertes', 'pan.'),
        ('panade', 'pan.'),
        ('suppe', 'sup.'),
        ('Suppe', 'Sup.'),
        ('chinesisches', 'chin.'),
        ('chinesische', 'chin.'),
        ('hackfleisch', 'hackfl.'),
        ('grünen', 'gr.'),
        ('wahlweise', ''),
        ('streifen', 'str.'),
        ('gebacken', 'geb.'),
        ('gebraten', 'gebr.'),
        (' / ', '/'),
        (' +', '+')
    ]

    for x in shorten_list:
        entry = entry.replace(x[0], x[1])
    entry = entry.replace("  ", " ")
    return entry.strip()

def get_tweets(m):
    """
    Collect the tweets.
    """
    result = []
    for theke in m['theken']:
        names = {
            "vital": "VITAL",
            "theke1": "THEKE 1",
            "theke2": "THEKE 2",
            "theke3": "THEKE 3",
            "pasta": "PASTA",
            "aktion": "AKTION"
        }

        meals = [shorten(x['name'].encode('utf-8')) for x in m['theken'][theke]]
        meals = shorten(" | ".join(meals))

        tweet = "%s: %s" % (names[theke], meals)

        result.append(tweet)

    return result

def combine(tweets):
    """
    Combines short tweets.
    """
    tweets.sort(key = len)

    l = 0
    indices = []
    short_tweets = []
    for index in range(len(tweets)):
        if l + len(tweets[index]) < 137:
            l = l + len(tweets[index])
            short_tweets.append(tweets[index])
            indices.append(index)

    new_tweet = " ‖ ".join(short_tweets)
    new_tweets = [new_tweet]
    for i in range(len(tweets)):
        if not i in indices:
            new_tweets.append(tweets[i])

    return new_tweets

def add_appetite(tweets):
    """
    Adds "Good appetite" to shortest tweet
    """
    tweets.sort(key = len)
    
    tweets[0] += " ‖ %s!" % bon_appetit()
    return tweets

m = getmenu(MENSA)

# don't tweet on holidays
if 'kommentar' in m:
    sys.exit()

tweets = combine(get_tweets(m))
tweets = add_appetite(tweets)
tweets = [cap_length(x) for x in tweets]

auth = tweepy.OAuthHandler(CREDENTIALS['CONSUMER_KEY'], CREDENTIALS['CONSUMER_SECRET'])
auth.set_access_token(CREDENTIALS['ACCESS_KEY'], CREDENTIALS['ACCESS_SECRET'])
api = tweepy.API(auth)

for tweet in tweets:
    print tweet, len(tweet)
    api.update_status(tweet)
