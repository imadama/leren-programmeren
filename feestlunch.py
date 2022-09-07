
croissant =  input("Hoeveel croissant's:")
stokbrood =  input("Hoeveel stokbrood:")
kortingsbonnen=  input("Hoeveel coupons:")
kosten =  ((float (croissant)*2)+(float (stokbrood)*2)-(float (kortingsbonnen)*5))

print ("De feestlunch kost je {} euro". format (kosten))