from random import randint
from sre_constants import REPEAT
from timeit import repeat
from tkinter import TRUE


play = True
ronde = 1
bomb = randint(1,10)
score = 0
while play == True:
    guess = input("Ronde "+str(ronde)+": Op welk getal denkt u dat de bom ligt")
   
    if int(guess) == bomb:
        play = False
        print("Boem!, Game over")
    else:
        score = score + (ronde * ronde)
        ronde = ronde + 1 
        nextRound = input("Wilt u naar ronde "+str(ronde)+ " (Y/N)?").lower()

        if nextRound == "n":
            play = False

print("Uw score is", score)
