import json
import random

rarity = [
    "rare holo v",
    "trainer gallery rare holo",
    "Radiant Rare",
    "Rare Ultra",
    "Rare Holo VMAX",
    "Rare Rainbow",
    "Rare Holo VSTAR",
]

showcase = {
    "id": "swsh12pt5-160",
    "set": "swsh12pt5",
    "name": "Pikachu",
    "supertype": "pokémon",
    "subtypes": ["Normal"],
    "types": ["Lightning"],
    "number": "160",
    "rarity": "rare holo v",
    "images": "/demo.png",
}




decks_dict = {
    "showcase": showcase,
    "decks": [],
}
decks = []

def convert_deck(cards):
    deck = []
    for card in cards:
        single = {
            "id": card,
            "set": card,
            "name": card,
            "supertype": "Pokémon",
            "subtypes": ["Normal"],
            "types": ["Water"],
            "number": card,
            "rarity": random.choice(rarity),
            "images": f"https://cdn.233.momobako.com/ygopro/pics/{card}.jpg",
        }
        deck.append(single)
    return deck

with open("./deck.json", "w", encoding="utf-8") as out:
    deck = {}
    mainDeck = []
    extraDeck = []
    sideDeck = []
    stat = None
    with open("./deck.ydk", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#main'):
                stat = "main"
                continue
            elif line.startswith('#extra'):
                stat = "extra"
                continue
            elif line.startswith('!side'):
                stat = "side"
                continue
            
            if line.isnumeric():
                if stat == "main":
                    mainDeck.append(line)
                elif stat == "extra":
                    extraDeck.append(line)
                elif stat == "side":
                    sideDeck.append(line)

    mainDeck = convert_deck(mainDeck)
    extraDeck = convert_deck(extraDeck)
    sideDeck = convert_deck(sideDeck)
    deck = {
        "main": mainDeck,
        "extra": extraDeck,
        "side": sideDeck,
    }

    decks.append(deck)
    decks_dict["decks"] = decks

    json.dump(decks_dict, out, ensure_ascii=False)
