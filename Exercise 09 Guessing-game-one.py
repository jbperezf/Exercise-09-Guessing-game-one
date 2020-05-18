# Exercise 9. Guessing game one
#
# - Generate a random number between 1 and 9 (including 1 and 9).
# - Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#   (Hint: remember to use the user input lessons from the very first exercise)
# - Keep the game going until the user types “exit”
# - Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

random_num = random.randint(0, 10)
guessing_times = 0
user_num = int(input("Guess a number between 1 and 10: "))

while True:
    if user_num < random_num:
        user_num = int(input("Too low, guess again: "))
        guessing_times += 1
        continue
    elif user_num > random_num:
        user_num = int(input("Too high, guess again: "))
        guessing_times += 1
        continue
    elif user_num == random_num:
        guessing_times += 1
        print("That's it! it took you " + str(guessing_times) + " guesses.\nWant to go again or exit the game?")
        if str(input("'exit' or 'again'?: ")) == "again":
            random_num = random.randint(0, 10)
            guessing_times = 0
            user_num = int(input("Guess a number between 1 and 10: "))
            continue
        else:
            break
