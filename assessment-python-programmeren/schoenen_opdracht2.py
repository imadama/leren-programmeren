from schoenen_check_data import *

# opdracht 2:
# Vraag een merk en print vervolgens alle modellen van het merk en de bijbehorende prijs.

gewenst_merk = input("Welk merk wil je zien? ").capitalize()

for schoen in schoenen_lijst:
    if schoen["merk"] == gewenst_merk:
        print(schoen["model"], "€" + str(schoen["prijs"]))