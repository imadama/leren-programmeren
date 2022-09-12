a = int(input("Getal voor a:"))
b = int(input("Getal voor b:"))

if a > b:
    a = max
    print("a is het grootste getal")

elif a < b:
    a = min
    print("a is het kleinste getal")

else :
    print("a en b zijn even groot")
    max = a
    min = b

print ("Het minimum is:{}". format (max))
print ("Het maximum is:{}". format (min))
