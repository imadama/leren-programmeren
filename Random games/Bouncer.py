leeftijd = input("hoe oud bent u?")
if int(leeftijd) >= 17:
    print("U mag naar binnen!")
    naam = input("wat is uw naam?")
    if int(leeftijd) >= 21:
        if naam ==  "Rudi" or naam == "Arnold" or naam == "jeroen" or naam == "Kjeld":
            print("U krijgt een sticker.")  
            quit()  
    if int(leeftijd) < 21:
        print ("U krijft een alcoholbandje")
    else:
            print("U krijgt een alcoholbandje.")
    drinken = input("Wat wil je drinken? A)Bier B)Cola:")
    if drinken == "b" and int(leeftijd) < 21:
            print("U mag geen bier.")
    else:
            print("Hier is uw bier!")
else:
    print("U mag niet naar binnen!")
 