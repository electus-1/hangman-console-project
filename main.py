import random
from turtle import clear
from hangman_art import logo, stages
from hangman_words import word_list

# Choose a random word from the list to work with
random_word = random.choice(word_list)
lives = 6  # Assigned six lives because we have 6 stages for the hangman art
print(logo)  # greeting the user with logo
blanks = []  # we need as many blanks as the letters in the random word
for character in random_word:
    blanks += "_"

while True:
    # prompting the user for their guess and making it lowercase just in case they enter uppercase
    user_guess = input("Guess a letter: ").lower()
    if (
        user_guess in blanks
    ):  # checking the blanks to make sure the user hasn't already guessed that letter correctly
        print(f'You\'ve already guessed the letter "{user_guess}".')

    # if the random word contains the users guess, replace the blank in the correponding index of "blanks" with the user guess
    for index in range(0, len(random_word)):
        if random_word[index] == user_guess:
            blanks[index] = user_guess
    # if the random word does not contain the users guess, decrease lives by 1 to change the stage of the hangman art
    if user_guess not in random_word:
        print(f'The letter "{user_guess}" is not in the word.')
        lives -= 1
        if lives == 0:  # if there are no remaining lives, the game is lost
            print(f'The answer is "{random_word}".')
            print("You lost.")
            break
    # convert the "blanks" list to string in order to display it properly
    print(f"{' '.join(blanks)}")
    # if blanks are fully replaced, then the game is won
    if blanks == random_word:
        print("You win!")
        break
    print(stages[lives])
