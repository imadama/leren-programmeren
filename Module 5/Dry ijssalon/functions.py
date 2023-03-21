def welkom_bericht():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

def hoeveel_bollen():
    while True:
        try:
            aantal_bollen = int(input("Hoeveel bollen wilt u? "))
            if aantal_bollen < 1:
                print("Sorry, dat hebben we niet.")
            elif aantal_bollen > 8:
                print("Sorry, zulke grote bakken hebben we niet")
            else: 
                return aantal_bollen
        except ValueError:
            print("Sorry, dat begrijp ik niet.")

def get_bakje_hoorn():
    while True:
        bakje_hoorn = input("Wilt u deze bolletjes in een hoorntje of een bakje? ").lower()
        if bakje_hoorn == "hoorntje" or bakje_hoorn == "bakje":
            return bakje_hoorn
        else:
            print("Sorry, we hebben alleen hoorntjes en bakjes. Probeer opnieuw.")