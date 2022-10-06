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