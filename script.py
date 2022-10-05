import random
import os

# constants
VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# rendering methods
def print_chosen_word(word, letters_already_taken):
    "for every letter in the chosen word, prints an underscore"
    print("\n")
    for letter in word:
        if letter in letters_already_taken:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")

def print_taken_letters(letters):
    "prints letter's that have already been taken"
    print("\n" + "Letters already taken: ")
    for i in letters:
        print(i.upper(), end=", ")

# logic methods
def take_user_input():
    "takes user input and stores it"
    letter = input("\n" + "\n" + "Choose a letter: ")
    return letter.upper()

def chosen_word():
    "selects a random word from the words file"
    with open('words.txt', 'r') as f:
        allText = f.read()
        words = list(map(str, allText.split()))
  
        # print random string
        random_word = random.choice(words)
        return random_word

# main loop and state
def main():
    # state
    letters_already_taken = []
    word = chosen_word().upper()

    # game loop
    while True:
        # rendering
        os.system('cls' if os.name == 'nt' else 'clear')
        print_chosen_word(word, letters_already_taken)
        print_taken_letters(letters_already_taken)

        # logic
        letter = take_user_input()
        letters_already_taken.append(letter)

if __name__ == "__main__":    
    main()