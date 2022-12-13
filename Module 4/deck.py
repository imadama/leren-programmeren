import random
deckkleuren = ["harten", "klaveren", "schoppen", "ruiten"]
deckkaarten = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
jokers = ["joker", "joker2"]

for x in range (len(deckkleuren)):
    a = deckkleuren[x]
    for y in range(len(deckkaarten)):
        b = deckkaarten [y]
        ab = a + b
        jokers.append(ab)

random.shuffle(jokers)

for i in range(1,6):
    print(f'kaart {i}: {jokers[i]}')
print(jokers)