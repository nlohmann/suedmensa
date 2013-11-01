# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./app/menu.py

```json
{
    "url": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8432", 
    "datum": "01.11.2013", 
    "aktion": [
        "Asia-Curry (vegan) wahlweise mit Hähnchenstreifen mit Basmatireis (Tagestipp)"
    ], 
    "pasta": [
        "Pfifferlings-Sahnesoße", 
        "Tomatensoße mit Hackbällchen"
    ], 
    "vital": [
        "Hühnersuppe", 
        "Rindersauerbraten mit Sauce (L-)", 
        "Kabeljau, natur, gebraten (L-)", 
        "Auberginen, gebacken (L-) (vegan)", 
        "Makkaroni mit Cashew-Paprikasauce (vegan)", 
        "vier Mozzarella-Sticks (fleischlos)", 
        "Pilzgemüse auf Kichererbsenpüree mit Lauch (fleischlos)"
    ], 
    "theke1": [
        "Brathering (L-) / Sahnehering (L+)"
    ], 
    "theke2": [
        "Hähnchensteak in Knusperpanade", 
        "Steak in Kräuterpanade", 
        "Nudelauflauf", 
        "Köfta (Rindfleisch-Gemüsebällchen)"
    ]
}
```

## Installation

Der Speiseplan läuft unter Python und nutzt [Flask](http://flask.pocoo.org) und [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Danksagung

Das [Icon](http://thenounproject.com/noun/restaurant/#icon-No2392) von [@Suedmensa](https://twitter.com/suedmensa) wurde von [Saman Bemel-Benrud](http://thenounproject.com/samanbb/#) entworfen und als [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/) veröffentlicht.
