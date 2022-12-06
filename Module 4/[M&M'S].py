import random
kleuren = ("oranje", "blauw", "groen", "bruin")
hoeveel = int(input("Hoeveel M&M's wil je toevoegen?"))
zak = []

for x in range (hoeveel):
     randomkleur = random.choice(kleuren)
     zak.append(randomkleur)
print(f'Je hebt {hoeveel} kleuren in de zak!')
print(zak)