# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./app/menu.py

```json
{
    "url": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8492", 
    "status": 200, 
    "href": "http://localhost:5000/suedmensa", 
    "datum": "2013-11-12", 
    "theken": {
        "theke1": [
            {
                "name": "Eintopf"
            }
        ], 
        "aktion": [
            {
                "name": "American Roast, Remoulade"
            }
        ], 
        "theke2": [
            {
                "name": "Steak mit Zwiebelrahm"
            }, 
            {
                "name": "Geflügelhacksteak", 
                "laktosefrei": true
            }, 
            {
                "name": "Flunder, paniert", 
                "laktosefrei": true
            }
        ], 
        "pasta": [
            {
                "name": "Hackfleischsoße mit frischen Champignons"
            }, 
            {
                "name": "Tomatensoße mit Hirtenkäse"
            }
        ], 
        "vital": [
            {
                "name": "Möhren-Mango-Suppe"
            }, 
            {
                "name": "Hähnchenbrust im Karotten-Zucchinimantel", 
                "laktosefrei": true
            }, 
            {
                "name": "Gemüse-Kartoffelpfanne mit Mini-Hacksteaks, Joghurt Dip"
            }, 
            {
                "name": "Curry-Burger", 
                "vegan": true
            }, 
            {
                "vegetarisch": true, 
                "name": "Gemüsestrudel"
            }, 
            {
                "vegetarisch": true, 
                "name": "zwei gekochte Eier mit Senfsauce"
            }
        ]
    }
}
```

## Installation

Der Speiseplan läuft unter Python und nutzt [Flask](http://flask.pocoo.org) und [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Danksagung

Das [Icon](http://thenounproject.com/noun/restaurant/#icon-No2392) von [@Suedmensa](https://twitter.com/suedmensa) wurde von [Saman Bemel-Benrud](http://thenounproject.com/samanbb/#) entworfen und als [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/) veröffentlicht.
