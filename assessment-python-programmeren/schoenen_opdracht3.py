from schoenen_check_data import *


# opdracht 3:
# Vraag een merk en print vervolgens alle witte schoenen mits duurder dan €100.

gewenst_merk = input("Welk merk wil je zien? ").capitalize()


for schoen in schoenen_lijst:
    if schoen["merk"] == gewenst_merk and schoen["kleur"] == "wit" and schoen["prijs"] > 100:
        print(schoen['merk'] , schoen['model'] , schoen['prijs'] , schoen['kleur'],)