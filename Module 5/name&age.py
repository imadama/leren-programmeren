def naam_leeftijd():
    name = input("What is your name? ")
    age = input("What is your age? ")
    return {'name': name, 'age': age}

people = []

while True:
    answer = input("Press enter to continue or type 'stop' to print: ")
    if answer == 'stop':
        break
    person = naam_leeftijd()
    people.append(person)

for person in people:
    print(f'Name: {person["name"]}, Age: {person["age"]}')




# Maak een functie genaamd "naam_leeftijd" die de gebruiker vraagt om de naam en leeftijd te invullen. 
# Deze functie retourneert een dictionary met de properties 'name' en 'age'.
# Maak een lege lijst genaamd "people" aan.
# Gebruik een while-lus om de gebruiker te vragen om de naam en leeftijd te invullen, of om te stoppen. 
# Binnen de while-lus, voer de functie "naam_leeftijd" uit en voeg het resultaat toe aan de "people" lijst.
# Als de gebruiker "stop" invoert, gebruik een for-lus om door de "people" lijst te gaan en print de naam en leeftijd van elke persoon.