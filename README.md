#mtg bases converter
------------------------------------------------------------
##Introduction
This is a simple program for converting MTG cards in csv format into a .md format
intended for obsidian bases.

##Prerequisites
In order to use this tool you simply require a '.csv' file containing the data related to the cards you want converted to a '.md' format,
and an internet connection to recieve the 'img uri' related to the cards, as this tool runs the scryfall API to recieve the correct uri's (https://scryfall.com/docs/api)

##Commands
Launch the conversion process from CLI:
```
python .\main.py c 'source csv directory' 'destination directory'
```
Launch the GUI:
```
python .\main.py 
```

##Output
A successful output of the converter should provide a sorted dirctory in the format:
Dest_folder/Cube/Color/CardType/CMC
```
+---Dest_folder
|   
\---Cube
    +---B
    |   +---Creature
    |   |   +---1
    |   ...
    |   +---Enchantment
    |   |   +---1
    |   |   \---3
    |   ...
    |   +---Instant
    |   |   +---1
    |   ...
    |   +---Legendary Creature
    |   |   \---2
    |   ...
    |   +---Legendary Planeswalker
    |   |   \---6
    |   ...
    |   \---Sorcery
    |       +---1
    |  ...
```
and each '.md' file should have the following format, with the name 'Card_name.md':
```
---
 tags: 
 - Bird
 Type: Creature
 Color: W
 CMC: 1
 Number of cards: 44
 Img_uri: https://cards.scryfall.io/normal/front/c/c/cc8e4563-04bb-46b5-835e-64ba11c0e972.jpg?1730489133
 In my cube: False
 set: fdn
---
```
