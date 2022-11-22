dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

while True:
    welkeDag = input("Welke dag is het vandaag? ")
    if welkeDag in dagen:
        break
    else:
        print("Voer de huidige dag in...")

index = 0
while True:
    print(dagen[index])
    if dagen[index] == welkeDag:
        break

    index += 1