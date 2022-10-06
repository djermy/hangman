import random

VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# logic methods
def validate_input(usr_input, letters_already_taken):
    """checks that the input is only 1 letter from the VALID_CHARS constant, also checks if the letter is already taken

    returns an error message if the input is invalid, and returns None if it is valid"""
    if len(usr_input) > 1:
        return "You can only input 1 letter at a time!"
    elif usr_input in letters_already_taken:
        return "This letter has already been taken!"
    elif usr_input not in VALID_CHARS or usr_input == "":
        return "Invalid input, Please input a letter from the latin alphabet"
    return None


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

