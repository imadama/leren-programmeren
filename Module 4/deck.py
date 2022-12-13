import random
deckkleuren = ["harten", "klaveren", "schoppen", "ruiten"]
deckkaarten = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
jokers = ["joker", "joker2"]
deck = []

for i in range(len(deckkaarten)):
    for x in range(len(deckkleuren)):
        deck.append(deckkleuren[x] + ' ' + deckkaarten[i])
deck.append('Joker'), deck.append('Joker')
random.shuffle(deck)

for i in range(1, 8):
    print(f'Kaarten {i}: {deck.pop()}')
print(f'''
[Deck] Kaarten: {len(deck)}
{deck}''')