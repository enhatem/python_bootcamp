from replit import clear
#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)
    
    num1 =  float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    
    
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    previous_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {previous_answer}")
    repeat_calculation = True
    while repeat_calculation:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick another operation from the line above: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        current_answer = calculation_function(previous_answer, num3)
        print(f"{previous_answer} {operation_symbol} {num3} =  {current_answer}")
        # check if user wants to continue
        user_decision = input(
            f"Type 'y' to continue calculating with {current_answer}, or type 'n' to start a new calculation.: "
        ).lower()
        if user_decision == 'y':
            # reset first_answer
            previous_answer = current_answer
        else:
            repeat_calculation = False
            clear()
            calculator()  # Recursion ==> Recalling a function within it's own definition

calculator()