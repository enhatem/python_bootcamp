############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

##################### Code #####################
import os
import random
from art import logo

# NB: We can only call a function after it has been declared
# we could have used sum() to get the total sum of a list
def calculate_score(player_cards):
    player_score = 0
    number_of_cards = len(player_cards)
    for i in range(0, number_of_cards):
        player_score += player_cards[i]
    return player_score


def re_evaluate_ace(player_cards):
    for i in range(0, 2):
        if player_cards[i] == 11:
            player_cards[i] = 1
    return player_cards

def print_score(user_cards, user_score, computer_cards, computer_score):
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {computer_cards}. Computer's score: {computer_score}")

def check_blackjack(user_cards, user_score, computer_cards, computer_score):
    flag = False
    if computer_score == 21:
        flag = True
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("You lose. Computer has a blackjack.")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return flag
    elif user_score == 21:
        flag = True
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("You win. You have a blackjack!")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return flag

def blackjack():

    # Clearing console
    os.system('cls')

    # printing welcome screen
    print(logo)
    print("Welcome to Blackjack!")

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    ace_drawn_user = False
    ace_drawn_computer = False
    user_score = 0
    computer_score = 0

    # Drawing 2 random cards for the user and the computer
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        if user_cards[-1] == 11:
            ace_drawn_user = True
        computer_cards.append(random.choice(cards))
        if computer_cards[-1] == 11:
            ace_drawn_computer = True

    # Calculating scores
    user_score = calculate_score(player_cards=user_cards)
    computer_score = calculate_score(player_cards=computer_cards)

    # Checking if any of the scores are above 21 and whether an ace was drawn
    if computer_score > 21 and ace_drawn_computer is True:
        computer_cards = re_evaluate_ace(computer_cards)
    if user_score > 21 and ace_drawn_user is True:
        user_cards = re_evaluate_ace(user_cards)

    # Recalculating scores
    user_score = calculate_score(player_cards=user_cards)
    computer_score = calculate_score(player_cards=computer_cards)

    # Revealing the computer's first card to the user as well as the user's cards
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Asking the user if they want to draw another card
    should_keep_drawing = True
    while should_keep_drawing:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == 'y':
            user_cards.append(random.choice(cards))
            user_score = calculate_score(player_cards=user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            if user_score > 21:
                should_keep_drawing = False
                print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
                print("You lose. Your score is larger that 21.")
                user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
                if user_decision == 'y':
                    blackjack()
                return 0
        else:
            should_keep_drawing = False

    # Checking if computer or the player has a blackjack(The computer wins if they have a blackjack, even if the user has a blackjack too)
    flag = check_blackjack(user_cards, user_score, computer_cards, computer_score)
    if flag:
        return 0

    # Drawing cards for the computer until their score goes over 16
    if computer_score < 17:
        computer_draws = True
        while computer_draws:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)
            if computer_score > 17:
                computer_draws = False

    # Checking if the computer's score is larger than 21 after adding the cards
    if computer_score > 21:
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("You win. The computer's score is larger that 21.")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return 0

    # Checking if we have a blackjack or if we have a draw
    flag = check_blackjack(user_cards, user_score, computer_cards, computer_score)
    if flag:
        return 0

    # Checking if we have a draw
    if computer_score == user_score:
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("It's a draw!")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return 0
    elif user_score > computer_score:
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("You win! Your score is greater than the computer's score.")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return 0
    else:
        print_score(user_cards=user_cards, user_score=user_score, computer_cards=computer_cards, computer_score=computer_score)
        print("You lose. Your score is smaller than the computer's score.")
        user_decision = input("Type 'y' if you want to play again. Otherwise, type 'n'. ").lower()
        if user_decision == 'y':
            blackjack()
        return 0


user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_choice == 'y':
    blackjack()
