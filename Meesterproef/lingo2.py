import random
from lingowords import words

def select_word():
    """
    Deze functie selecteert een willekeurig woord uit de woordenlijst
    """
    return random.choice(words)

def check_guess(word, guess):
    """
    Deze functie controleert de geraden letters van de speler en geeft feedback
    """
    feedback = ''
    for i in range(len(word)):
        if word[i] == guess[i]:
            feedback += 'G'
        elif guess[i] in word:
            feedback += 'Y'
        else:
            feedback += 'R'
    return feedback

def play_game():
    """
    Deze functie start het Lingo spel en geeft de speler 5 pogingen
    """
    word = select_word()
    print('Welkom bij Lingo! Raad het woord met 5 letters dat begint met de letter', word[0])
    guesses = 0
    correct = False
    while guesses < 5 and not correct:
        guess = input('Poging {}: '.format(guesses+1))
        if len(guess) != len(word):
            print('Je moet een woord raden met {} letters'.format(len(word)))
            continue
        feedback = check_guess(word, guess)
        print(feedback)
        if feedback == 'GGGGG':
            correct = True
            print('Gefeliciteerd, je hebt het woord geraden in {} pogingen!'.format(guesses+1))
            break  # voeg een break statement toe om de lus te verlaten wanneer het woord is geraden
        guesses += 1
    if not correct:
        print('Helaas, je hebt het woord niet geraden. Het woord was', word)

if __name__ == '__main__':
    play_game()
