# Südmensa Speiseplan

Lädt den Speiseplan der großartigen [Südmensa](http://tinyurl.com/suedmensa) herunter und bietet ihn als JSON-Datei an. Diese wird unter anderem genutzt, um täglich über den Account [@Suedmensa](https://twitter.com/suedmensa) zu twittern.

## Beispiel

    ./suedmensa/menu.py

```json
{
  "datum": "30.10.2013", 
  "aktion": [
    "Coq au Vin - H\u00e4hnchen in Rotwein und Pilzen (L-)"
  ], 
  "pasta": [
    "Tomatenso\u00dfe mit Rucola (vegan) (L-)", 
    "Puten-Curry-So\u00dfe"
  ], 
  "vital": [
    "Grie\u00dfsuppe mit Basilikum", 
    "Chicken Tikka masala (ind. H\u00e4hnchen-Curry)", 
    "Bolognese mit Rinderhackfleisch", 
    "Nudelpfanne mit Gem\u00fcse (L-) (vegan)", 
    "Falafel mit Dip (vegan)", 
    "K\u00e4seschnitzel (fleischlos)"
  ], 
  "theke1": [
    "Kartoffel-Gem\u00fcseauflauf"
  ], 
  "theke2": [
    "Steak mit Tomate und Mozzarella \u00fcberbacken", 
    "griechisches Hacksteak", 
    "Fischfilet, P\u00fcree mit Sellerie (Tagestipp)"
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
