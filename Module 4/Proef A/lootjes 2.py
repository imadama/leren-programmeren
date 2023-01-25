from random import shuffle

namen_lijst = []

while len(namen_lijst) < 3:
    print(f"voeg minimaal {3 - len(namen_lijst)} namen toe")
    voegnaamtoe = input("Voeg een naam toe:\n\n>> ").capitalize()
    if voegnaamtoe in namen_lijst:
        print("Naam bestaat al\n")
    else:
        namen_lijst.append(voegnaamtoe)

while True:
    print("type quit om te stoppen\n")
    voegnaamtoe = input("Voeg nog een naam toe:\n\n>> ").capitalize()
    if voegnaamtoe.lower() == "quit":
        break
    elif voegnaamtoe in namen_lijst:
        print("Naam bestaat al\n")
    else:
        namen_lijst.append(voegnaamtoe)

geschudde_namen = namen_lijst.copy()
shuffle(geschudde_namen)

for i in range(len(geschudde_namen)):
    print(f"{geschudde_namen[i]} heeft {geschudde_namen[i-1]} getrokken\n")
