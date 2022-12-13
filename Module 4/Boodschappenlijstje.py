boodschappenlijst = {}
door = "ja"
while door == "ja":
    product = input("Welke product wil je toevoegen aan uw boodschappenlijst?: ").capitalize()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    
    if product not in boodschappenlijst:
        boodschappenlijst.update({product: aantal})    
    
    else:
        boodschappenlijst[product] += aantal
    door = input("Wil je nog een product toevoegen?: ").lower()
print("-----------------")
print("BOODSCHAPPENLIJST")
for aantal, product in boodschappenlijst.items():
    print(f"{product} x {aantal}")