import json

with open("./deck.ydk", "r") as f:
    cards = []
    for line in f.readlines():
        line = line.strip()
        if line.isnumeric():
            cards.append(line)


with open("./deck.json", "w", encoding="utf-8") as f:
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
            "rarity": "rare holo v",
            "images": f"https://cdn.233.momobako.com/ygopro/pics/{card}.jpg",
        }
        deck.append(single)

    json.dump(deck, f, ensure_ascii=False)
