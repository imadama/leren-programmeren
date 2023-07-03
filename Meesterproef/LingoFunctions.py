from termcolor import *
from lingowords import *
from random import *

KLEURGOED = "green"
KLEURSLECHT = "white"
KLEURHALF = "yellow"
NUMMERGOED = 1
NUMMERHALF = 2
NUMMERSLECHT = 3
MAX_POGINGEN = 5

def WelkomBericht():
    print("Welkom bij Lingo!")
    print("Dit spel is gemaakt door:")
    print("Imad Amazyan")

def AfsluitBericht():
    print("Bedankt voor het spelen van Lingo!")
    print("Ik ben erg blij dat u dit spel wilde spelen.")

def spelregels():
    print("De regels van Lingo zijn als volgt:")
    print("Raad 1 woord, die 5 letters bevat.")
    print("Het woord moet 5 letters lang zijn en mag alleen letters bevatten.")
    print("Je krijgt 5 pogingen om het woord te raden.")
    print("Bij elke poging worden de letters die op de juiste plaats staan groen gekleurd.")
    print("Letters die wel in het woord zitten maar op de verkeerde plaats staan worden geel getoond.")

def PrintEersteLetter(wordtoguesslist:list):
    print("De eerste letter van het woord is:")
    print(colored(wordtoguesslist[0],KLEURGOED))

def GetWord():
    word = choice(words)
    return word

def GetWordLength(word):
    return len(word)

def CheckWord(lenword:int):
    repeat = True
    while repeat == True:
        wordinput = input("Geef een woord van " + str(lenword) + " letters:").lower()
        if int(len(wordinput)) == lenword and wordinput.isalpha() == True:
            repeat = False
            return wordinput
        else:
            repeat = True

def Wordtoguessinletters(wordtoguess:str):
    wordlist = []
    for letter in wordtoguess:
        wordlist.append(letter)
    return wordlist