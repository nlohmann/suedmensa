# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./suedmensa/menu.py

```json
{
  "datum": "30.10.2013", 
  "aktion": [
    "Coq au Vin - Hähnchen in Rotwein und Pilzen (L-)"
  ], 
  "pasta": [
    "Tomatensoße mit Rucola (vegan) (L-)", 
    "Puten-Curry-Soße"
  ], 
  "vital": [
    "Grießsuppe mit Basilikum", 
    "Chicken Tikka masala (ind. Hähnchen-Curry)", 
    "Bolognese mit Rinderhackfleisch", 
    "Nudelpfanne mit Gemüse (L-) (vegan)", 
    "Falafel mit Dip (vegan)", 
    "Käseschnitzel (fleischlos)"
  ], 
  "theke1": [
    "Kartoffel-Gemüseauflauf"
  ], 
  "theke2": [
    "Steak mit Tomate und Mozzarella überbacken", 
    "griechisches Hacksteak", 
    "Fischfilet, Püree mit Sellerie (Tagestipp)"
  ]
}
```

## Installation

Der Speiseplan läuft unter Python und nutzt [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Danksagung

Das [Icon](http://thenounproject.com/noun/restaurant/#icon-No2392) von [@Suedmensa](https://twitter.com/suedmensa) wurde von [Saman Bemel-Benrud](http://thenounproject.com/samanbb/#) entworfen und als [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/) veröffentlicht.
