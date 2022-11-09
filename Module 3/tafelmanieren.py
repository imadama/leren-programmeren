nummer = int(input("Welke tafel wil jij weten?"))

for i in range(1,11):
    print(f"{i} *  {nummer} = {i * nummer}")