# from data_handler import DataHandler
#
# if __name__ == '__main__':
#     file_dir_name = 'data/20230405_152908_4.csv'
#
#     data_handle = DataHandler(file_dir_name)
#     data_handle.read_data()
#
#     if data_handle.data is not None:
#         #print(f"DatAVG.xa =  {data_handle.data['ns=6;s=::AsGlobalPV:comm_metrologie.o_datums_B1112.DatAVG.X',]}")
#         datAVG_x = data_handle.data['ns=6;s=::AsGlobalPV:comm_metrologie.o_datums_B1112.DatAVG.X'].to_numpy()
#         print(datAVG_x.shape)

import random

import art
from game_data import data



def higher_lower():

    # TODO: Create welcome screen


    # TODO: Generate 2 random numbers
    random_number_1 = random.randint(0, len(data))
    random_number_2 = random.randint(0, len(data))

    while random_number_1 == random_number_2:
        random_number_2 = random.randint(0, len(data))

    # TODO: Create score for user
    score = 0


    # TODO: Output options on the screen and ask user to pick between them
    option_a = data[random_number_1]
    option_b = data[random_number_2]

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print("VS")
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")


    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # debugging
    print(f"{option_a['name']}'s follower count: {option_a['follower_count']}")
    print(f"{option_b['name']}'s follower count: {option_b['follower_count']}")

    # TODO: Compare value based on the required key, if their correct, increase score, if not, game over
    if option_a['follower_count'] > option_b['follower_count']:
        if user_choice == 'a':
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            return
    else:
        if user_choice == 'b':
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            return


    # TODO: If correct, keep second option, make it the first option and pick a new option B using new random number


higher_lower()






















