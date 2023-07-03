from schoenen_check_data import *

# Opdracht 5:
# print van de duurste schoen: merk en model en doe dat ook voor de goedkoopste.

max_prijs = 0
min_prijs = float("inf")

for schoen in schoenen_lijst:
    if schoen["prijs"] > max_prijs:
        max_prijs = schoen["prijs"]
        duurste_schoen = schoen
    if schoen["prijs"] < min_prijs:
        min_prijs = schoen["prijs"]
        goedkoopste_schoen = schoen

print(f"De duurste schoen is:", duurste_schoen["merk"], duurste_schoen["model"])
print("De goedkoopste schoen is:", goedkoopste_schoen["merk"], goedkoopste_schoen["model"])