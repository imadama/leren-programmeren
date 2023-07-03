import random
from lingowords import words
from termcolor import colored

def get_random_word(words):
    return random.choice(words) 

def get_first_letter(random_woord):
    eerste_letter = random_woord[0]
    return eerste_letter

while True:
    print('Welkom bij Lingo!\n')
    print("Voer een 5-letterwoord in en druk op Enter!")
    print("Je krijgt 5 pogingen om het woord te raden.")
    print("Als de letter in het woord zit, maar niet op de juiste plek staat, dan wordt de letter geel.")
    print("Als je een letter goed hebt, en op de juiste plek, dan wordt de letter groen.")
    print("Als je een letter fout hebt en de letter zit niet in het woord, dan wordt de letter rood.\n")

    woord = get_random_word(words)
    eerste_letter = get_first_letter(woord)
    print("Het woord begint met de letter: " + eerste_letter)
    # print(woord)

    for poging in range(1,6):
        while True:
            raden = input(f"Poging {poging}: ").lower()
            if len(raden) == 5:
                break
            else:
                print("Het woord moet 5 letters lang zijn!")

        correcte_letters = list("_"*5)
        temp_woord = list(woord)

        # Eerste loop voor de groene letters
        for i in range(5):
            if raden[i] == woord[i]:
                correcte_letters[i] = colored(raden[i], 'green')
                temp_woord[i] = '_'

        # Tweede loop voor de gele en rode letters
        for i in range(5):
            if correcte_letters[i] == "_":
                if raden[i] in temp_woord:
                    correcte_letters[i] = colored(raden[i], 'yellow')
                    temp_woord[temp_woord.index(raden[i])] = '_'
                else:
                    correcte_letters[i] = colored(raden[i], 'red')

        print(''.join(correcte_letters))

        if raden == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging}!", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'quit' om af te sluiten. Klik Enter om door te spelen.\n")
    if opnieuw_spelen.lower() == 'quit':
        break
