import random
import os

def chosen_word():
    with open('words.txt', 'r') as f:
        allText = f.read()
        words = list(map(str, allText.split()))
  
        # print random string
        random_word = random.choice(words)
        return random_word


def print_chosen_word(word):
    print("\n")
    for i in range(len(word)):
        print("_", end=" ")

def take_user_input(letters):
    letter = input("\n" + "\n" + "Choose a letter: ")
    letters.append(letter.lower())

def print_taken_letters(letters):
    print("\n" + "Letters already taken: ")
    for i in letters:
        print(i.upper() + ",", end=" ")

def letter_in_word(word, letters):
    if letters[-1] in word:
        return True

def main():
    letters_already_taken = []
    word = chosen_word()

    while True:
        chosen_word()
        print_chosen_word(chosen_word())
        take_user_input(letters_already_taken)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_taken_letters(letters_already_taken)

if __name__ == "__main__":    
    main()