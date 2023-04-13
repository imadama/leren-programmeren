from data import *
from termcolor import colored

def intro():
    print (colored("Welkom bij Papi Gelato.","red"))    

def klant_soort():
    
        repeat = True   
        while repeat == True:
    
            klant = input("Bent u een particulier of zakelijke klant?:\n(A) Particulier \n(B) Zakelijke\n").lower()
    
            if klant == "a":
                klant = "Particuliere"
                repeat = False
                return klant

            elif klant == "b" : 
                klant = "Zakelijke"
                repeat = False
                return klant    
    
            else:
                print (error_message)
                repeat = True


def aantal(klant) -> int: 
    repeat = True   
    while repeat == True:
        if klant == "Particuliere":
            try:
                aantal = int(input("Hoeveel bolletjes wilt u?:\n"))

                if aantal > 8 :
                    print ("Sorry, zulke grote bakken hebben we niet!")
                    repeat = True
            
                elif aantal < 1 :
                    print ("U moet minimaal 1 bolletje kiezen!")
                    repeat = True
                    
                elif aantal in range (1,9):
                    repeat = False
                    break

            except:
                print (error_message)

                repeat = True

        elif klant == "Zakelijke":
            try:
                aantal= int(input("Hoeveel liter ijs wilt u?:\n"))

                if aantal < 1 :
                    print ("U moet minimaal 1 liter bestellen!")
                    repeat = True

                else:
                    repeat = False
                    break

            except:
                print (error_message)
                repeat = True

    bonnetje["aantal_bollen"] += aantal
    return aantal

        

def smaak(bolletjeNummer,klant):

    if klant == "Particuliere":
        eenheid = "bolletje"
    else:
        eenheid = "liter"
    repeat = True
    while repeat == True:

        keuze = input("Welke smaak wilt u voor " + eenheid + " nummer "+ str(bolletjeNummer)+"?: \n(A) Aardbei \n(C) Chocolade \n(V) Vanille?\n").lower()

        if keuze in smaak_soort.keys():
            return keuze

        else:
            print(error_message)
            repeat = True
    
def smaken(aantal_bollen:int,klant):

    for i in range(aantal_bollen):
        keuze = smaak_soort.get(smaak(i+1,klant))
        bonnetje[keuze] += 1 

def verpakking(aantal_bolletjes:int,klant) :

    repeat = True   
    while repeat == True:

        if klant == "Particuliere":
            if aantal_bolletjes in range(1,4):
                verpakking_soort = input("Wilt u deze "+str(aantal_bolletjes)+" bolletje's in een [hoorntje] of een [bakje]?:\n").lower()

                if verpakking_soort == "hoorntje" or verpakking_soort == "bakje" :     
                    repeat = False
                    verpakking = verpakking_soort
                    return verpakking

                else:
                    print (error_message)
                    repeat = True

            if aantal_bolletjes in range (4,9):
                print ("Dan krijgt u van mij een bakje met " +str(aantal_bolletjes)+" bolletjes.")
                verpakking = "bakje"
                repeat = False
                return verpakking

        elif klant == "Zakelijke":
            return ""

        

def verpakking_bon(verpakking):

    if verpakking == "hoorntje":
        bonnetje["aantal_hoorn"] += 1 

    elif verpakking == "bakje":
        bonnetje["aantal_bakjes"] += 1 
    else:
        pass

def topping(klant):

    repeat = True
    while repeat == True:
        if klant == "Particuliere":
            keuze = input("Wat voor topping wilt u?: \n(A) Geen \n(B) Slagroom \n(C) Sprinkels \n(D) Caramel Saus\n").lower()
            
            if keuze in topping_soort.keys():
                toppings = topping_soort.get(keuze)
                bonnetje[toppings] += 1
                return toppings

            else:
                print(error_message)
                repeat = True

        else:
            return ""

def afsluiten(aantal_bolletjes,verpakking,klant):
    if klant == "Particuliere":

        if aantal_bolletjes == 1:
            print ("Hier is uw ",verpakking, " met",aantal_bolletjes, "bolletje.")

        else:
            print ("Hier is uw ",verpakking, " met ", aantal_bolletjes, " bolletje's.")

    else:
        pass


def doorbestellen(klant):
    
    vraag = True

    while vraag:
        if klant == "Particuliere":
            opnieuw = input("Wilt u nog meer bestellen?: [JA/NEE]\n").lower()

            if opnieuw == "ja":
                nieuwe_bestelling = True
                vraag = False
                return nieuwe_bestelling

            elif opnieuw == "nee":
                nieuwe_bestelling = False
                vraag = False
                return nieuwe_bestelling

            else:
                print(error_message)
                vraag= True
                nieuwe_bestelling = False
                return nieuwe_bestelling
        else:
            nieuwe_bestelling = False
            return nieuwe_bestelling

def Fprijs_per_bol(aantal:int,prijs):

    prijs_per_bol = aantal * prijs
    return prijs_per_bol

def Fprijs_per_hoorn(aantal:int, prijs):

    prijs_per_hoorn = aantal * prijs
    return prijs_per_hoorn

def Fprijs_per_bak(aantal:int, prijs):

    prijs_per_bak = aantal * prijs
    return prijs_per_bak


def topping_prijs(topping,verpakking,aantal_bollen):


    if topping == "geen":
        totaal_topping_kosten =  0
    

    elif topping == "slagroom":
        totaal_topping_kosten =  0.50


    elif topping == "sprinkels":  
         totaal_topping_kosten =  0.30 * aantal_bollen


    elif topping == "Caramel Saus" and verpakking == "bakje":
        totaal_topping_kosten =  0.90


    elif topping == "Caramel Saus" and verpakking == "hoorntje":
        totaal_topping_kosten =  0.60

    else:
        totaal_topping_kosten = 0


    return totaal_topping_kosten

def totale_prijs(totaal_topping_kosten,klant):

    if klant == "Particuliere":
        prijs = prijs_per_bolletje

    elif klant == "Zakelijke":
        prijs = prijs_per_liter

    totaal = Fprijs_per_bak(bonnetje.get("aantal_bakjes"),prijs_per_bak) + Fprijs_per_bol(bonnetje.get("aantal_bollen"),prijs) + Fprijs_per_hoorn(bonnetje.get("aantal_hoorn"),prijs_per_hoorentje)
    totaal = totaal + totaal_topping_kosten
    return totaal

def BTW(prijs):
    Btw = (prijs / 106)
    Btw  = format(Btw * 6,".2f")
    return Btw

def bon(totaal_topping_kosten,klant):

    if klant == "Particuliere":
        ijs_soort = "Bolletje(s)"
        prijs = prijs_per_bolletje
        Btw = ""

    elif klant == "Zakelijke":
        ijs_soort = "Liter(s)"
        prijs = prijs_per_liter
        Btw = ("BTW (6%)                   =    €",BTW(prijs))
        

    if bonnetje.get("aantal_bakjes") == 0:
        print_bakje = ""
    else:
        print_bakje = ("Bakje(s)                  ",bonnetje.get("aantal_bakjes"), "x", format(prijs_per_bak,".2f"), "= €", format(Fprijs_per_bak(bonnetje.get("aantal_bakjes"),prijs_per_bak),".2f"),"\n") 
    

    if bonnetje.get("aantal_hoorn") == 0:
        print_hoorn = ""
    else:
        print_hoorn = ("Hoorntjes                 ",bonnetje.get("aantal_hoorn"), "x", format(prijs_per_hoorentje,".2f"), "= €", format(Fprijs_per_hoorn(bonnetje.get("aantal_hoorn"),prijs_per_hoorentje),".2f"),"\n") 
    

    if bonnetje.get("aardbei") == 0:
        print_aardbei = ""
    else:
        print_aardbei = (ijs_soort+" aardbei       ",bonnetje.get("aardbei"), "x", format(prijs,".2f"), "= €", format(Fprijs_per_bol(bonnetje.get("aardbei"),prijs),".2f"),"\n") 
    

    if bonnetje.get("chocolade") == 0:
        print_chocolade = ""
    else:
        print_chocolade = (ijs_soort,"chocolade     ",bonnetje.get("chocolade"), "x", format(prijs,".2f"), "= €", format(Fprijs_per_bol(bonnetje.get("chocolade"),prijs),".2f"),"\n") 
    
    if bonnetje.get("vanille") == 0:
        print_vanille = ""
    else:
        print_vanille = (ijs_soort,"vanille       ",bonnetje.get("vanille"), "x", format(prijs,".2f"), "= €", format(Fprijs_per_bol(bonnetje.get("vanille"),prijs),".2f"),"\n") 


    if totaal_topping_kosten == 0:
        print_topping = ""
    else:
        print_topping = ("Toppings                   = €",format(totaal_topping_kosten,".2f"))

    print('''
-------------["Papi Gelato"]-------------

''',
*print_aardbei,
*print_chocolade,
*print_vanille,
*print_bakje,
*print_hoorn,
*print_topping,


'''              
                            --------- +\nTotaal                      =    €''',format(totale_prijs(totaal_topping_kosten,klant),".2f"),'''\n''',
*Btw,'''

Bedankt en tot ziens!        
        ''')