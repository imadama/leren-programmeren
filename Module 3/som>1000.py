nummer = 50
totaal = 0
output = ""
getal = 0

while totaal < 1000:
    totaal += nummer
    nummer += 1
    output += f" + {nummer}"
    getal += 1
    print(f"{getal}. 50{output} ={totaal}")