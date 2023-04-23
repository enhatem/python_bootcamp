from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)



    # coffee_machine.report()
    # print(coffee_machine.is_resource_sufficient(drink))
    # money_machine.make_payment(drink.cost)
    # coffee_machine.make_coffee(drink)
    # coffee_machine.report()
    # money_machine.report()