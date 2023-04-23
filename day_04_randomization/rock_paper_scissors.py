rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_choice = random.randint(0, 2)

list = [rock, paper, scissors]
if user_choice >= 0 and user_choice <= 2:
    print(list[user_choice])
    print(f"computer chose: {list[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    else:
        print("you lose")
else:
    print("Please input a valid number.")
