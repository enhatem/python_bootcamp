import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
# Generating random int number between 1 and 100 both included
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
# For debugging
print(f"Pssst, the correct number is: {number}")

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if chosen_difficulty == 'hard':
    lives = 5
else:
    lives = 10
print(f"You have {lives} attempts remaining to guess the number.")

keep_repeating = True
while keep_repeating:
    guess = int(input("Make a guess: "))
    if guess == number:
        keep_repeating = False
        print(f"You got it! The answer was {number}.")
    elif guess < number:
        lives -= 1
        print("Too low.")
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        lives -= 1
        print("Too high.")
        print(f"You have {lives} attempts remaining to guess the number.")

    if lives == 0:
        keep_repeating = False
        print("You've run out of guesses, you lose.")
    elif guess != number:
        print("Guess again.")
