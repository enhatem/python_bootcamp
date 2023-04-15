def turn_right():
    turn_left()
    turn_left()
    turn_left()

right_turns = 0
while not at_goal():
    if right_is_clear() and right_turns < 4:
        turn_right()
        move()
        right_turns += 1
    elif right_is_clear and right_turns >=4:
        if front_is_clear():
            move()
            right_turns = 0
        else:
            turn_right()
            right_turns = 0
    elif front_is_clear():
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0