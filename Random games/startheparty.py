gastheer = input("Wat is de naam van de gastheer?")
gasten = 5
drank = True
chips = True

# het feest kan alleen beginnen als de gastheer er is tenzij 
#                               er gasten, chips en drank zijn
# een feest met chips, maar zonder drank kan niet beginnen
# een feest met gasten kan niet beginnen als er geen chips en geen drank is
# een gastheet kan een feest geven zonder chips en gasten,
#                                   maar niet zonder drank
# een feest moet minimaal gasten of een gastheer hebben
# alleen chips is geen feest
# een feest met gasten kan alleen beginnen als er miniaal 5 zijn
# een feest met meer dan 12 kan niet beginnen

if gastheer != "rudi" and ((gasten <= 5 and gasten >= 12) or gasten == 0 and gastheer != " "):
    print("Start the Party")
else: 
    print("No Party")