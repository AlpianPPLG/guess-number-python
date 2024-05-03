import random
import time
import sys

# this is the game's title
print("Welcome to Number Guessing Game!")

# setting up the number range for the user to guess
print()
number_range = int(input("Please enter the maximum number you want to guess: "))
secret_number = random.randint(1, number_range)

# allow the user to make guesses
print()
guess_limit = str(input("You have 10 attempts to guess the number. type 'yes' to continue: "))

for attempt in range(10):
    print()
    guess = int(input("Please enter your guess: "))

    if guess < secret_number:
        print()
        print("Your guess is too low.")
    elif guess > secret_number:
        print()
        print("Your guess is too high.")
    else:
        print()
        print(f"Congratulations! You've guessed the secret number {secret_number} correctly in {attempt+1} attempts.")
        break

# if all attempts are used
if attempt == 9:
    print()
    print(f"Sorry, you've exhausted all your attempts. The secret number was {secret_number}.")

# end of the game
print()
input("Press Enter to exit...")
sys.exit()