# turtle event listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
# When we use a function as an argument to another function, we don't add the parentheses.
# Using the parenthesis in the argument will run the function right then and there.
screen.onkey(fun=move_forward, key="space")

screen.exitonclick()


def add(n1, n2):
    return n1+n2

def divide(n1, n2):
    return n1/n2

# Higher order function (it's a function that can work with other functions
# ==> not applicable in all programming languages. But it's commonly used in pythons)
def calculate(n1, n2, func):
    return func(n1, n2)

result = calculate(2, 3, divide)
print(result)
