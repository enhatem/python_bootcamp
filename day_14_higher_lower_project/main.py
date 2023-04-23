import random
from os import system
import art
from game_data import data

def clear_screen():
    system('cls')
    print(art.logo)

def check_answer(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == 'a'
    else:
        return guess == 'b'

def higher_lower():

    # Printing art logo
    print(art.logo)

    # Get data list size
    data_size = len(data)

    # Generate 2 random numbers
    random_number_1 = random.randint(0, data_size-1)
    random_number_2 = random.randint(0, data_size-1)

    while random_number_1 == random_number_2:
        random_number_2 = random.randint(0, data_size-1)

    # Create score for user
    score = 0

    # Output options on the screen and ask user to pick between them
    option_a = data[random_number_1]
    option_b = data[random_number_2]

    should_continue = True
    # Create while loop to repeat the program until the user chooses wrong
    while should_continue:
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
        print(art.vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Clearing screen
        clear_screen()

        # Comparing value based on the required key, if their correct, increase score, if not, game over
        is_correct = check_answer(user_choice, option_a['follower_count'], option_b['follower_count'])

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

        # Store dictionary of option_b in option_a
        option_a = option_b

        # TODO: If correct, keep second option, make it the first option and pick a new option B using a new random number
        random_number_n = random.randint(0, data_size-1)
        while random_number_n == data.index(option_a):
            random_number_n = random.randint(0, data_size-1)

        option_b = data[random_number_n]


higher_lower()

















