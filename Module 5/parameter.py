def groet(aantal:int):
    antwoord = " "
    for x in range(1, aantal + 1):
        antwoord += f"hello from funtion town {x} \n"
    return antwoord

print(groet(3))
print("-----")
print(groet(7))