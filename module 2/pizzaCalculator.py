#Imad Amazyan   opdracht: Pizza calculator
from re import L


print ("""  
    Pizza's in het assortiment:
            Small pizza=    €5.99
            Medium pizza=   €7.99
            Large pizza=    €9.99""")

try:
    smallpizza = input("Hoeveel Small pizza's wilt u?:")
    smallpizza = int(smallpizza)
except:
    print("Oops!  That was no valid number.  Try again...")


try:
    mediumpizza = input("Hoeveel Medium pizza's wilt u?:")
    mediumpizza = int(smallpizza)
except:
    print("Oops!  That was no valid number.  Try again...")
    

try:
    largepizza = input("Hoeveel Large pizza's wilt u ?:")
    largepizza = int(largepizza)
except:
    print("Oops!  That was no valid number.  Try again...")
  
totalkost =  ((smallpizza * 5.99) + (mediumpizza * 7.99) + (largepizza * 9.99))


print ("De totalenkosten zijn €{}". format (totalkost))