import random
from os import system
import art
from game_data import data



def higher_lower():

    print(art.logo)

    # Get data list size
    data_size = len(data)

    # TODO: Generate 2 random numbers
    random_number_1 = random.randint(0, data_size-1)
    random_number_2 = random.randint(0, data_size-1)

    while random_number_1 == random_number_2:
        random_number_2 = random.randint(0, data_size-1)

    # TODO: Create score for user
    score = 0

    # TODO: Output options on the screen and ask user to pick between them
    option_a = data[random_number_1]
    option_b = data[random_number_2]

    should_continue = True
    while should_continue:
        # TODO: Create while loop to repeat the program until the user chooses wrong

        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
        print(art.vs)
        print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")


        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        # debugging
        print(f"{option_a['name']}'s follower count: {option_a['follower_count']}")
        print(f"{option_b['name']}'s follower count: {option_b['follower_count']}")

        # TODO: Compare value based on the required key, if their correct, increase score, if not, game over
        if option_a['follower_count'] > option_b['follower_count']:
            if user_choice == 'a':
                score += 1
                # To keep last option in option a
                option_a = option_b
                system('cls')
                print(art.logo)
                print(f"You're right! Current score: {score}.")
            else:
                system('cls')
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}.")
                return
        else:
            if user_choice == 'b':
                score += 1
                # To keep last option in option a
                option_a = option_b
                system('cls')
                print(art.logo)
                print(f"You're right! Current score: {score}.")
            else:
                system('cls')
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}.")
                return


        # TODO: If correct, keep second option, make it the first option and pick a new option B using a new random number
        random_number_n = random.randint(0, data_size-1)
        while random_number_n == data.index(option_a):
            random_number_n = random.randint(0, data_size-1)

        option_b = data[random_number_n]


higher_lower()






















