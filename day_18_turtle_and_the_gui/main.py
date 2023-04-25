from turtle import Turtle, Screen, forward, backward, right, left
import random

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("darkgreen")
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# import heroes
# print(heroes.gen())

# Challenge 2
# for i in range(20):
#     if i % 2 == 0:
#         tim.pendown()
#     else:
#         tim.penup()
#     tim.forward(10)

# Challenge 3 (draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon)
# from random import  randint
# screen = Screen()
# screen.colormode(255)
# sides = 3
# while sides < 11:
#     angle = 360 / sides
#     tim.color((randint(0, 255), randint(0, 255), randint(0, 255)))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

# Challenge 4 (generate a random walk with the turtle) ---- increase thickness and velocity of turtle
# movement = [tim.forward, tim.backward, tim.right, tim.left]
# direction = [0, 90, 180, 270]
# screen = Screen()
# tim.pensize(15)
# tim.speed(10)
# screen.colormode(255)
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# i = 0
# while i < 200:
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
#     # index = random.choice(range(len(movement)))
#     # if index == 0 or index == 1:
#     #     movement[index](20)
#     # else:
#     #     movement[index](90)
#     i += 1

# my_tuple = (1, 3, 8)
# print(my_tuple[2])

# Challenge 5 (Drawing a spyrograph)
screen = Screen()
screen.colormode(255)
tim.speed(11)

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



screen.exitonclick()
