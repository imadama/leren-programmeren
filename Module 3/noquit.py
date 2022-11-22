#elke vraag is +1
vraag = ''
teller = 0
#stel de gebruiker als vraag "wat?""
while vraag != "quit":
    vraag = input("wat? ")
    teller += 1

print(f"De vraag is {teller} keer gesteld")