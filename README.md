# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./app/menu.py

```json
{
    {
        "url": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8451", 
        "datum": "2013-11-06", 
        "theken": {
            "theke1": [
                {
                    "name": "Spaghetti Pesto"
                }
            ], 
            "aktion": [
                {
                    "name": "gerolltes Ofenschnitzel in Tomatensauce"
                }
            ], 
            "theke2": [
                {
                    "name": "Kräuter-Puten-Frikadelle"
                }, 
                {
                    "name": "Schnitzel XXL", 
                    "laktosefrei": true
                }, 
                {
                    "name": "Hähnchenpfanne mit Paprika und Erdnüssen", 
                    "laktosefrei": true
                }
            ], 
            "pasta": [
                {
                    "name": "Frischkäse-Schinken-Soße"
                }, 
                {
                    "name": "Hähnchenstreifen in pikanter Tomatensoße"
                }
            ], 
            "vital": [
                {
                    "name": "Paprika-Zucchinisuppe"
                }, 
                {
                    "name": "magere Schweinefleischstreifen mit Champignons, Erbsen, Zwiebeln, Paprika und Käse überbacken"
                }, 
                {
                    "name": "Seelachsfilet Spreewälder Art"
                }, 
                {
                    "name": "Gemüsechili", 
                    "vegan": true
                }, 
                {
                    "vegetarisch": true, 
                    "name": "Backcamembert mit Preiselbeeren"
                }, 
                {
                    "vegetarisch": true, 
                    "name": "Kartoffelpizza mit Gemüse"
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
