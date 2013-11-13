# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./app/menu.py

```json
{
    "status": 200, 
    "mensa": "suedmensa", 
    "theken": {
        "theke1": [
            {
                "name": "Spätzle-Pilz-Pfanne"
            }
        ], 
        "aktion": [
            {
                "name": "Putensteak Champignons"
            }
        ], 
        "theke2": [
            {
                "name": "Steak mit Würzfleisch überbacken"
            }, 
            {
                "name": "Buntbarschfilet, gebraten", 
                "laktosefrei": true
            }, 
            {
                "tagestipp": true, 
                "name": "Dönerpfanne mit Tzatziki (Kalbfleisch), Reis"
            }, 
            {
                "name": "Hefeklöße mit Fruchtsuppe ODER Germknödel"
            }
        ], 
        "pasta": [
            {
                "name": "Käsesoße mit Putenstreifen"
            }, 
            {
                "name": "Tomatensauce mit frischem Gemüse"
            }
        ], 
        "vital": [
            {
                "name": "Kartoffelsuppe"
            }, 
            {
                "name": "marinierte Hähnchenbruststreifen  auf frischem Salat (L+)", 
                "laktosefrei": true
            }, 
            {
                "name": "Puten-Gemüse-Bällchen in Paprikasauce"
            }, 
            {
                "name": "Spaghetti Carbonara Art", 
                "vegan": true
            }, 
            {
                "laktosefrei": true, 
                "vegan": true, 
                "name": "Kartoffelschnitzel"
            }, 
            {
                "vegetarisch": true, 
                "name": "Gnocchipfanne mit Gemüse und Hirtenkäse"
            }, 
            {
                "vegetarisch": true, 
                "name": "Kartoffelrösti mit Tomate und Mozzarella überbacken"
            }
        ]
    }, 
    "url": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8511", 
    "datum": "2013-11-13", 
    "href": "http://localhost:5000/suedmensa.json"
}
```

## Installation

Der Speiseplan läuft unter Python und nutzt [Flask](http://flask.pocoo.org) und [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Danksagung

Das [Icon](http://thenounproject.com/noun/restaurant/#icon-No2392) von [@Suedmensa](https://twitter.com/suedmensa) wurde von [Saman Bemel-Benrud](http://thenounproject.com/samanbb/#) entworfen und als [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/) veröffentlicht.
