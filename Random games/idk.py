from schoenen_data import *

# opdracht 4:
# vraag de maat van de klant en print vervolgens:
# "fonetische_kleuren Merknaam Modelnaam, prijs"
# uiteraard alleen de schoenen die beschikbaar zijn in betreffende maat.


maat = input('Hallo wat is je maat? ')

for schoen in schoenen_lijst:
    #print(schoen)  # print alle schoenen in de lijst om te controleren of de lus correct werkt
    if schoen['maten'] == maat:
        print('Beschikbare schoenen:', schoen['kleur'], schoen['merk'], schoen['model'], schoen['prijs'])
