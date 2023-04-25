import random
import turtle
# import colorgram
#
# colors = colorgram.extract("C:\\Users\\Elie\\Documents\\Development\\python_bootcamp\\day_18_turtle_and_the_gui\\the_hirst_painting_project\\image\\image.jpeg", 30)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)

# 10x10 spots. Size of dot 20, spaced by 50
color_list = [(188, 18, 44), (243, 231, 66), (252, 236, 241), (210, 236, 242), (196, 74, 33), (218, 66, 107), (17, 125, 173), (196, 175, 17), (107, 182, 209), (12, 142, 88), (12, 167, 214), (241, 231, 2), (210, 152, 94), (186, 41, 61), (24, 39, 76), (77, 174, 95), (35, 44, 111), (214, 68, 50), (219, 129, 156), (124, 185, 119), (236, 164, 184), (6, 59, 39), (147, 208, 221), (7, 94, 54), (4, 85, 110), (160, 29, 28), (236, 171, 164), (162, 212, 178)]
michael_angelo = turtle.Turtle()
turtle.colormode(255)
michael_angelo.speed(11)
x = -5*50
y = -5*50
michael_angelo.penup()
michael_angelo.hideturtle()
michael_angelo.setposition(x, y)
number_of_dots = 10

for i in range(number_of_dots):
    if i > 0:
        y += 50
        michael_angelo.goto(x, y)
    for j in range(number_of_dots):
        michael_angelo.dot(20, random.choice(color_list))
        michael_angelo.forward(50)


screen = turtle.Screen()
screen.exitonclick()

