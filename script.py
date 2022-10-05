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
    print("\n")

def render(word, tries_left, letters_already_taken, message):
    "renders the hangman game"
    os.system('cls' if os.name == 'nt' else 'clear')
    print("tries left: ", tries_left)
    print_chosen_word(word, letters_already_taken)
    print_taken_letters(letters_already_taken)
    print(message)

# logic methods
def validate_input(usr_input, letters_already_taken):
    """checks that the input is only 1 letter from the VALID_CHARS constant, also checks if the letter is already taken

    returns an error message if the input is invalid, and returns None if it is valid"""
    if len(usr_input) > 1:
        print_taken_letters(letters_already_taken)
        return "You can only input 1 letter at a time!"
    elif usr_input in letters_already_taken:
        print_taken_letters(letters_already_taken)
        return "This letter has already been taken!"
    elif usr_input not in VALID_CHARS:
        print_taken_letters(letters_already_taken)
        return "Invalid input, Please input a letter from the latin alphabet"
    return None

def take_user_input(letters_already_taken):
    "takes user input and validates it to ensure it's a valid latin character and not already taken"
    usr_input = input("Choose a letter: ").upper()
    error = validate_input(usr_input, letters_already_taken)
    if error != None:
        usr_input = None
    return (usr_input, error)

def chosen_word():
    "selects a random word from the words file"
    with open('words.txt', 'r') as f:
        allText = f.read()
        words = list(map(str, allText.split()))
  
        # print random string
        random_word = random.choice(words)
        return random_word

def is_guess_mistake(word, letter):
    "returns true is the guess was incorrect, false otherwise"
    return letter not in word

def has_won(letters_already_taken, word):
    "checks if the player has won"
    for letter in word:
        if letter not in letters_already_taken:
            return False
    return True

# main loop and state
def main():
    # state
    letters_already_taken = []
    word = chosen_word().upper()
    tries_left = 10
    message = ""

    # game loop
    while True:
        # rendering
        render(word, tries_left, letters_already_taken, message)

        # logic
        letter, error = take_user_input(letters_already_taken)
        if error != None:
            message = error
            continue

        if is_guess_mistake(word, letter):
            message = "oops, that wasn't right"
            tries_left -= 1
            if tries_left <= 0:
                print("Unlucky, you lose")
                break
        else:
            message = "correct!"
        
        letters_already_taken.append(letter)

        if has_won(letters_already_taken, word):
            print("Congratulations, you've won!")
            break

    print("GAME OVER! Thanks for playing! ")
        

if __name__ == "__main__":
    main()