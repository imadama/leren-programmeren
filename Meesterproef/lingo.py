import random
from lingowords import words

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def check_guess(guess, target_word, guessed_letters):
    correct_positions = set()
    correct_letters = set()
    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            correct_positions.add(i)
            guessed_letters.add(letter)
        elif letter in target_word:
            correct_letters.add(letter)
    return correct_positions, correct_letters

def lingo_game():
    target_word = random.choice(words)
    guessed_letters = {target_word[0]}
    attempts = 5

    print("Lingo - Raad het woord!")
    print("Je krijgt 5 pogingen om het woord te raden.")
    print("Het woord begint met:", target_word[0])

    while attempts > 0:
        print("\nPogingen over:", attempts)
        guess = input("Voer een woord in: ").lower()

        if len(guess) != len(target_word) or guess[0] != target_word[0]:
            print("Ongeldig woord. Zorg ervoor dat het woord begint met de gegeven letter en dezelfde lengte heeft.")
            continue

        if guess == target_word:
            print("Gefeliciteerd! Je hebt het woord geraden:", target_word)
            break

        correct_positions, correct_letters = check_guess(guess, target_word, guessed_letters)
        display = display_word(target_word, guessed_letters)
        print("Correcte letters op de juiste positie (groen):", len(correct_positions))
        print("Correcte letters op de verkeerde positie (geel):", len(correct_letters))
        print("Huidige gok:", display)
        attempts -= 1

    if attempts == 0:
        print("\nHelaas! Je hebt geen pogingen meer. Het woord was:", target_word)

if __name__ == "__main__":
    lingo_game()
