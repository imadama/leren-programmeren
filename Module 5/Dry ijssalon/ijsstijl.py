from functions import welkom_bericht, hoeveel_bollen, get_bakje_hoorn

def stijl():
    welkom_bericht()

    while True:
        aantal_bollen = hoeveel_bollen()
        if aantal_bollen <= 3:
            bakje_hoorn = get_bakje_hoorn()
        else:
            bakje_hoorn = "bakje"
            print(f"Dan krijgt u van mij een bakje met {aantal_bollen} bolletjes.")

        print(f"Hier is uw {bakje_hoorn} met {aantal_bollen} bolletje(s).")
        meer_bestellen = input("Wilt u nog meer bestellen? (ja/nee) ").lower()
        if meer_bestellen == "ja":
            continue
        elif meer_bestellen == "nee":
            print("Bedankt en tot ziens!")
            break
        else:
            print("Sorry, dat snap ik niet. Probeer opnieuw.")

stijl()
