def addition(number1:int, number2 = 1):
    return number1 + number2

def subtraction(number1:int, number2 = 1):
    return number1 - number2

def multiplication(number1:int, number2 = 2):
    return number1 * number2 

def division(number1:int, number2 = 2):
    return number1 / number2



print("""
    wat wilt u doen?
    (A) getallen optellen,
    (B) getallen aftrekken,
    (C) getallen vermenigvuldigen,
    (D) getallen delen,
    (E) getal ophogen,
    (F) getal verlagen,
    (G) getal verdubbelen,
    (H) getal halveren.
    """)

geen = ["e", "f", "g", "h"]
wel = ["a", "b", "c", "d"]
repeat = True

number1 = int(input("voer een getal in: "))

while repeat == True:
    
    keuze = input("taak: ").lower()


    if keuze in wel :
        number2 = int(input("voer een tweede getal in: "))


        if keuze == "a":
            number3 = (addition(number1,number2))
            print(number3)

        if keuze == "b":
            number3 = (subtraction(number1,number2))
            print(number3)

        if keuze == "c":
            number3 = (multiplication(number1,number2))
            print(number3)

        if keuze == "d":
            number3 = (division(number1,number2))
            print(number3)
    
    
    elif keuze in geen:

        if keuze == "e":
            number3 =(addition(number1))
            print(number3)

        if keuze == "f":
            number3 =(subtraction(number1))
            print(number3)

        if keuze == "g":
            number3 =(multiplication(number1))
            print(number3)

        if keuze == "h":
            number3 =(division(number1))
            print(number3)

    if keuze == "stop":
        quit()

    
    number1 = number3