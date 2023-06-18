from turtle import Turtle, Screen

# W = Forwards
# S = Backwards
# A = Counter-clockwise
# D = Clockwise
# C = Clear drawing and put turtle back in the center

my_turtle = Turtle()
screen = Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def move_left():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)

def move_right():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)

def clear_screen():
    my_turtle.reset()

screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=clear_screen, key='c')


screen.exitonclick()


