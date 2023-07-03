## All imports
from termcolor import *
from lingowords import *
from random import *
## All Constants
KLEURGOED = "red"
KLEURSLECHT = "white"
KLEURHALF = "yellow"
NUMMERGOED = 1
NUMMERHALF = 2
NUMMERSLECHT = 3
MAX_POGINGEN = 5
## Shows the rules
def showrules():
    print("De regels van Lingo zijn als volgt:")
    print("1. er is 1 woord in het spel")
    print("2. je mag 5 keer raden")
    print("3. je mag alleen de letters van het woord raden")
    print("De Kleuren zijn als volgt:")
    print(f"1. goed: {KLEURGOED}")
    print(f"2. in het woord maar niet de juiste plek: {KLEURHALF}")
    print(f"3. Fout: {KLEURSLECHT}")
## Show the intro
def showintro():
    print("Welkom bij Lingo!")
    print("Dit spel is gemaakt door:")
    print("- Remco Mol")
## Shows the outro
def showoutro():
    print("Bedankt voor het spelen van Lingo!")
    print("Dit spel is gemaakt door:")
    print("- Remco Mol")
## Gets a word out off the wordlist  
def GetWord():
    word = choice(words)
    return word
## Gets the length of the word
def GetWordLength(word):
    return len(word)
## Asks the user for a word of the lenght off the wordtoguess and checks it
def wordcheck(lenword:int):
    repeat = True
    while repeat == True:
        wordinput = input("Geef een woord van " + str(lenword) + " letters:").lower()
        if int(len(wordinput)) == lenword and wordinput.isalpha() == True:
            repeat = False
            return wordinput
        else:
            repeat = True
## Returns the words in letters
def wordinletters(wordtoguess:str):
    wordlist = []
    for letter in wordtoguess:
        wordlist.append(letter)
    return wordlist
## Gives the words a number bound to a color
def checkwords(word:str,wordinput:str,wordlist:list,wordtoguesslist:list):
    checkwordlist = []
    checkworddict = {}
    wordtoguesslist2 = wordtoguesslist.copy()
    if word == wordinput:
        checkworddict["geraden"]=True
    else:
        checkworddict["geraden"]=False
    for i in range(len(word)):
        if wordlist[i]==wordtoguesslist[i]:
            checkwordlist.append(1)
            wordtoguesslist2[i] = "+"
        else:
            checkwordlist.append("+")
    for i in range(len(word)):
        if wordlist[i] in wordtoguesslist2 and checkwordlist[i] == "+":
            wordtoguesslist2[wordtoguesslist2.index(wordlist[i])] = "+"
            checkwordlist[i] = 2
        else:
            wordtoguesslist2[i] = "+"
    for i in range(len(word)):
        if wordlist[i] not in wordtoguesslist2 and checkwordlist[i] == "+":
            checkwordlist[i] = 3
    checkworddict["checkwordlist"]=checkwordlist
    return checkworddict
## Puts the letters with the correct color in an string
def getletterswithcolor(checkworddict:dict,wordlist:list):
    listtoprint = []
    wordnumber = 0
    totaltext = ""
    for i in checkworddict["checkwordlist"]:
        if i == NUMMERGOED:
            listtoprint.append(colored(wordlist[wordnumber],KLEURGOED))
        elif i == NUMMERHALF:
            listtoprint.append(colored(wordlist[wordnumber],KLEURHALF))
        else:
            listtoprint.append(colored(wordlist[wordnumber],KLEURSLECHT))
        wordnumber+=1
    for j in range(len(listtoprint)):
        totaltext = totaltext + listtoprint[j]
    return totaltext
    
## Prints the lingo board
def printlingoboard(wordstoprint:list,wordlenght:int):
    if len(wordstoprint) <= MAX_POGINGEN:
        for i in range(len(wordstoprint)):
            print(wordstoprint[i])
        for i in range(MAX_POGINGEN-len(wordstoprint)):
            print("*"*wordlenght)

## Asks the user to play again
def keepplaying():
    repeat = True
    while repeat == True:
        try:
            keepplaying=input("Wil je nog een keer spelen? Ja/Nee").lower()
            if keepplaying == "ja":
                return True
            elif keepplaying == "nee":
                return False
            else:
                print("Je hebt geen geldige invoer gegeven")
        except:
            print("Je hebt geen geldige invoer gegeven")
            repeat = True
## Prints the first letter of the word to guess
def printfirtslingoletter(wordtoguesslist:list):
    print("De eerste letter van het woord is:")
    print(colored(wordtoguesslist[0],KLEURGOED))


    
    



        

