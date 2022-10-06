import os

import hangman
import render

# rendering
def render_game(word, tries_left, letters_already_taken, message):
    "renders the hangman game"
    os.system('cls' if os.name == 'nt' else 'clear')
    print("tries left: ", tries_left)
    render.print_chosen_word(word, letters_already_taken)
    render.print_taken_letters(letters_already_taken)
    print(message)

# logic method
def take_user_input(letters_already_taken):
    "takes user input and validates it to ensure it's a valid latin character and not already taken"
    usr_input = input("Choose a letter: ").upper()
    error = hangman.validate_input(usr_input, letters_already_taken)
    if error != None:
        usr_input = None
    return (usr_input, error)


# main loop and state
def main():
    # state
    letters_already_taken = []
    word = hangman.chosen_word().upper()
    tries_left = 10
    message = ""

    # game loop
    while True:
        # rendering
        render_game(word, tries_left, letters_already_taken, message)

        # logic
        letter, error = take_user_input(letters_already_taken)
        if error != None:
            message = error
            continue

        if hangman.is_guess_mistake(word, letter):
            message = "oops, that wasn't right"
            tries_left -= 1
            if tries_left <= 0:
                print("Unlucky, you lose")
                break
        else:
            message = "correct!"
        
        letters_already_taken.append(letter)

        if hangman.has_won(letters_already_taken, word):
            print("Congratulations, you've won!")
            break

    print("GAME OVER! Thanks for playing! ")
        

if __name__ == "__main__":
    main()