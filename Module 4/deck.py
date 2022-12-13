import random
deckkleuren = ["harten", "klaveren", "schoppen", "ruiten", "cirkel"]
deckkaarten = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas", "timmerman"]
jokers = ["joker", "joker2"]
deck = []

for i in range(13):
    for x in range(3):
        deck.append(deckkleuren[x] + ' ' + deckkaarten[i])
deck.append('Joker'), deck.append('Joker')
random.shuffle(deck)

for i in range(1, 8):
    print(f'Kaarten {i}: {deck.pop()}')
print(f'''
[Deck] Kaarten: {len(deck)}
{deck}''')