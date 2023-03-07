restart = True
print("Welkom bij de quiz van hoofdsteden van alle landen!\n")
score = 0
hoofdstad = {"Afghanistan": "Kabul",
                "Algeria": "Algiers",
                "Belgium": "Brussels",
                "Bulgaria": "Sofia",
                "Czech Republic": "Praag",
                "Denmark": "Kopenhagen",
                "France": "Parijs",
                "Griekenland": "Athene",
                "Ijsland": "Reykjavik",
                "Iraq": "Bagdad",
                "Ireland": "Dublin",
                "Japan": "Tokyo",
                "Latvia": "Riga"}

for land in hoofdstad:
    antwoord = input(f"Wat is de hoofdstad van {land}?")
    if antwoord == hoofdstad[land]:
        print("Goed!")
        score = score + 1
    else:
        print("Fout!")
        print(f"De hoofdstad van {land} is {hoofdstad[land]}.")
        print("Game over!")
        print(f"Jouw score is {score} van de 13.")
        opnieuw = input("Wil je opnieuw spelen? [y/n]")
        if opnieuw == "y":
            restart = True
        if opnieuw == "n":
            print("OKAY BYEBYE!!!")
            break