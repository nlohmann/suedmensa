# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./app/menu.py

```json
{
    "url": "http://www.studentenwerk-rostock.de/index.php?lang=de&mainmenue=4&submenue=47&type=details&detail1=1&detail2=8451", 
    "datum": "2013-11-05", 
    "theken": {
        "theke1": [
            "Milchreis mit Früchten"
        ], 
        "aktion": [
            "Rumpsteak (L-)"
        ], 
        "theke2": [
            "Seelachsfilet in Knusperpanade (L-)", 
            "Steak Strindberg in Senf-Ei-Hülle (L-)", 
            "Hackbraten mit Soße, Kartoffeln, Rotkohl (Tagestipp)"
        ], 
        "pasta": [
            "Pastasoße Mexiko", 
            "Käsesauce mit Gemüse"
        ], 
        "vital": [
            "Tomatensuppe", 
            "Putenbruststreifen mit Gemüse und Paprikasauce", 
            "gefüllte Zucchini mediterran", 
            "Gemüsepfanne mit Bulgur (vegan)", 
            "Kichererbsen-Bohnen-Curry mit Cashewkernen (L-) (vegan)", 
            "Käsespätzle (fleischlos)"
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
