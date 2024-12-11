import random  # Allows use of random function to select random word from word list

from hangman_art import (
    logo,  # Imports logo to display when run
    stages,  # Imports pre-build ascii art of hangman stages in hangman_art.py
)
from hangman_words import (
    word_list,  # Imports pre-built word list in the hangman_words.py file
)

print(logo)

lives = 6 # Fixed number of lives allowed in hangman

chosen_word = random.choice(word_list)  # Assigns random word from list
# print(chosen_word)  # prints out this word - This should be disabled once testing is complete.

# Print placeholder to show blanks based on length of chars in chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("\n" + placeholder + "\n\n")  # Adds new line for readability

game_over = False  # sets whether game is over yet to use in loop below.
correct_letters = []  # Create list to store previously guessed letters

# Loop until game is over
while not game_over:

    # Ask user to guess a letter - assign to guess variable
    guess = input("Guess a letter: ").lower()

    # Check if letter guessed is in word and if so, replace corresponding blank
    display = ""

    for letter in chosen_word:  # Loop through letters in chosen_word
        if letter == guess:  # if good guess
            display += letter  # show letter
            correct_letters.append(guess)  # add chosen letter 

        elif letter in correct_letters:
            display += letter  # show letter if already added
        else:
            display += "_"  # shows blank still left to guess


    print("\n" + display + "\n")

    if guess not in chosen_word:
        lives -= 1  # decrements lives left
        if lives > 1:
            print(f"You have {lives} lives left.")
        else:
            print(f"You have {lives} life left!")
        print(stages[lives] + "\n")  # Displays the corresponding ascii art based on lives left
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was {chosen_word}.")

    if "_" not in display:  #Checks to see if the entire word has been guessed
        game_over = True
        print("You win!")
