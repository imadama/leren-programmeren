import random
AantalRondes = 20
punten = 0
ronde = 0

while ronde < AantalRondes:
    getal = random.randint(0, 1000) 
    print(getal)
    print("Hallo welkom bij het raden van het getal!")
    print("De game kiest een getal tussen 1 en 1000 uit, jij moet kiezen wat het getal is.")
    print("Je hebt 10 pogingen om te raden.")
    poging = 10

    while poging > 0:

        while True: 
	        keuze = int(input("Enter a number: ")) 
	            if keuze not in range(1,1001): 
		            print("enter a valid number between 1 and 1000)