from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo


def find_highest_bidder(bidding_record):
    # bidding_record = {"Angela": 123, "James": 321}
    highest_bid = 0
    bid_winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bid_winner = bidder
    print(f"The winner is {bid_winner} with a bid of ${highest_bid}")


print(logo)

bidding_dictionary = {}
repeat_process = True
while repeat_process:
    name_input = input("What is your name?: ")
    bid_input = int(input("What is your bid?: $"))
    bidding_dictionary[name_input] = bid_input
    result = input("Are there other bidders? type 'yes' or 'no'.\n")
    clear()
    if result == 'no':
        repeat_process = False
        find_highest_bidder(bidding_dictionary)
