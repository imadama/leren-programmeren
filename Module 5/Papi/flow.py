from function import *
from data import *

nieuwe_bestelling = True

intro()
klant = klant_soort()

while nieuwe_bestelling:
    
    aantal_bolletjes = aantal(klant)
    verpakking_soort = verpakking(aantal_bolletjes,klant)
    bol_smaak = smaken(aantal_bolletjes,klant)
    verpakking_bon(verpakking_soort)
    toppings = topping(klant)
    totaal_topping_kosten += topping_prijs(toppings,verpakking_soort,aantal_bolletjes)
    afsluiten(aantal_bolletjes,verpakking_soort,klant)
    nieuwe_bestelling = doorbestellen(klant)
    
bon(totaal_topping_kosten,klant)