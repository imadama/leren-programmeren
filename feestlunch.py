from http.client import OK

croissant =  input("Hoeveel croissant's:")
stokbrood =  input("Hoeveel stokbrood:")
kortingsbonnen=  input("Hoeveel coupons:")
kosten =  ((int (croissant)*2)+(int (stokbrood)*2)-(int (kortingsbonnen)*5))

print ("De feestlunch kost je {} euro". format (kosten))