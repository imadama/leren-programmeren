#Vacature: Circusdirecteur voor Circus HotelDeBotel


print("U gaat een sollicitatie invullen")

geslacht = input("Bent u een man of vrouw? ")
if geslacht == "man":
    snor = int(input("Hoelang is uw snor? Antwoord in centimeters. Als u geen snor heeft, antwoord dan met 0. "))
elif geslacht == "vrouw":
    roodkrulhaar = int(input("Hoelang is uw rood krulhaar? Antwoord in centimeters. Als u geen rood krulhaar heeft, antwoord dan met 0. "))


lengte = int(input("Hoelang bent u in centimeters? "))
gewicht = int(input("Hoe zwaar weegt u in kilogram? "))
input("hoe oud bent u? ")

dierendressuur = int(input("Hoeveel jaar heeft u ervaring met dieren dressuur? " ))
jongleren = int(input("Hoeveel jaar heeft u ervaring met jongleren? " ))    
acrobatiek = int(input("Hoeveel jaar heeft u ervaring met acrobatiek? ")) 

mbodiploma = input("Bezit u een MBO-4 diploma? ")
input("Hoelang was uw MBO-4 opleiding? ")
input("Wat voor MBO-4 opleiding heeft u gevolgd? ")
vrachtwagen = input("Heeft u een geldig vrachtwagenbewijs? ")
hogehoed = input("Bent u in bezit van een hoge hoed? ")
certificaat = input("Heeft u een certificaat voor overleven met gevaarlijk personeel? ")

if ((geslacht == "man" and snor >= 10) or (geslacht == "vrouw" and roodkrulhaar >= 20)) and lengte >= 150 and gewicht >= 90 and (dierendressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and mbodiploma == "ja" and vrachtwagen == "ja" and hogehoed == "ja" and certificaat == "ja":
    print("U bent aangenomen")
else:
    print("U voldoet helaas niet aan de eisen en u bent daardoor niet aangenomen. Nog een prettige dag verder.")