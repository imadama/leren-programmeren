from schoenen_check_data import *

# opdracht 4:
# vraag de maat van de klant en print vervolgens:
# "fonetische_kleuren Merknaam Modelnaam, prijs"
# uiteraard alleen de schoenen die beschikbaar zijn in betreffende maat.

gewenste_maatsize = int(input("Welke maat zoek je? "))

for schoen in schoenen_lijst:
    if gewenste_maatsize in schoen["maten"]:
        kleur = fonetische_kleuren[schoen["kleur"]]
        print(f"{kleur} {schoen['merk']} {schoen['model']}, €{schoen['prijs']}")
