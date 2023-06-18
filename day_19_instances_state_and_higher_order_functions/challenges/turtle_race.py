import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles_list=[]
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70 + i * 30)
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
            else:
                print(f"You lost! The {winning_color} turtle won!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
