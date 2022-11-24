import random
AantalRondes = 20
punten = 0
ronde = 0

while ronde < AantalRondes:
    getal = random.randint(0, 1000) 
    print("Hallo welkom bij het raden van het getal!")
    print("De game kiest een getal tussen 1 en 1000 uit, jij moet kiezen wat het getal is.")
    print("Je hebt 10 pogingen om te raden.")
    poging = 10

    while poging > 0:
        keuze = int(input("Welk getal kies je?"))
        if keuze <= getal:
            print("Hoger!")
        elif keuze >= getal:
            print("Lager!")

        if keuze == getal:
            print("Gefeliciteerd, je hebt het getal goed geraden!!")
            punten+=1
            break
        if (getal - keuze) <= 20:
            print("Je bent heel warm")
        elif (getal - keuze) <= 50:
            print("Je bent warm")
        poging-=1
        print(f"Ronde: {ronde}")

        print(f"punt(en):{punten}") #geeft aan hoeveel punten je heb
        ronde +=1 #telt een ronde op
        print(f"Ronde: {ronde}") #laat zien hoeveel ronde's je heb gehad
        
        if ronde == 10: 
            rondeMAX = input("U heeft nu 10 rondes gehad. Wilt u nog verder?")#als je 10 rondes heb gehad vraagt het programma of je nog door wil
            if rondeMAX == "nee":
                exit()#als je nee zegt dan stopt het programma, anders gaat hij verder
            elif ronde == AantalRondes:
                print(f"Je heb nu 20 rondes gespeeld. je totale score is: {punten}.") #laat zien wat je totale score is    