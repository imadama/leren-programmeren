print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
    aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
    try:
        aantal_bolletjes = int(aantal_bolletjes)
        if aantal_bolletjes in range(1, 4):
            keuze = input(f"Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje? ")
            if keuze == "hoorntje":
                print(f"Hier is uw hoorntje met {aantal_bolletjes} bolletje(s).")
            elif keuze == "bakje":
                print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s).")
            else:
                print("Sorry, dat snap ik niet...")
        elif aantal_bolletjes in range(4, 9):
            print(f"Dank u wel! Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes.")
        elif aantal_bolletjes >= 9:
            print("Sorry, zulke grote bakken hebben we niet.")
        else:
            print("Sorry, dat snap ik niet...")
    except ValueError:
        print("Sorry, dat snap ik niet...")

    meer_bestellen = input("Wilt u nog meer bestellen? ")
    if meer_bestellen.lower() == "ja":
        continue
    elif meer_bestellen.lower() == "nee":
        print("Bedankt en tot ziens!")
        break
    else:
        print("Sorry, dat snap ik niet...")
