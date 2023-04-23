from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def evaluate_machine_resources(user_input):
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    menu_water = MENU[user_input]["ingredients"]["water"]
    if "milk" in MENU[user_input]["ingredients"]:
        menu_milk = MENU[user_input]["ingredients"]["milk"]
    else:
        menu_milk = 0
    menu_coffee = MENU[user_input]["ingredients"]["coffee"]
    if machine_water >= menu_water:
        if machine_milk >= menu_milk:
            if machine_coffee >= menu_coffee:
                return True
            else:
                print("Not enough coffee in the machine.")
                return False
        else:
            print("Not enough milk in the machine.")
            return False
    else:
        print("Not enough water in the machine.")
        return False

def coffee_machine():
    system('cls')
    global resources
    is_running = True
    available_choices = ["espresso", "latte", "cappuccino", "off", "report"]
    while is_running:

        # Resting resource check
        enough_resources = False
        # Asking user what they want (“What would you like? (espresso/latte/cappuccino): ”)

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        while user_input not in available_choices:
            print("Your choice is not valid.")
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Including option to turn off coffee machine if the user enters "off" to the prompt.

        if user_input == "off":
            print("Turning off machine")
            is_running = False
        # Printing report if user enters "report" to the prompt.
        elif user_input == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")

        # Checking if resources are sufficient when the user orders a drink
        else:
            enough_resources = evaluate_machine_resources(user_input)

        # Processing coins. If there are enough ingredients to make the drink, we prompt the user to insert coins
        ## Calcualte the monetary value of the coins inserted
        # Coin operated: penny: 1cent($0.01), nickel: 5cents($0.05), dime: 10cents($0.1), quarter: 25cents($0.25)
        if enough_resources:
            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: "))
            dimes_inserted = int(input("How many dimes?: "))
            nickels_inserted = int(input("How many nickels?: "))
            pennies_inserted = int(input("How many pennies?: "))

            # Calculating the total amount of money inserted
            inserted_amount = quarters_inserted*0.25 + dimes_inserted*0.1 + nickels_inserted*0.05 + pennies_inserted*0.01

            # Checking if the inserted amount is enough to make the drink:
            if inserted_amount >= MENU[user_input]["cost"]:
                # Check transaction successful and add money to the machine and return change, if any.
                money_to_return = round(inserted_amount - MENU[user_input]["cost"], 2)
                resources["money"] += MENU[user_input]["cost"]
                if money_to_return > 0.0:
                    print(f"Here is ${money_to_return} in change.")
                # Deducting resources
                resources["water"] -= MENU[user_input]["ingredients"]["water"]
                if "milk" in MENU[user_input]["ingredients"]:
                    resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
                print(f"Here's your {user_input}☕️. Enjoy!")

            else:
                print(f"Sorry that's not enough money. Money refunded.")

coffee_machine()
