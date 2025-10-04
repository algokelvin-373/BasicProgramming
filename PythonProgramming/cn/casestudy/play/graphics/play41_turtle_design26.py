import turtle

def draw_pattern_left(x, y, side, step, y_ratio, y_targets):
    y_side = int(y_ratio * y)
    x_side = x
    turtle.goto(-x, y_side)
    turtle.goto(x, y_side)
    for _ in range(int(side / step)):
        for y_ratio_target in y_targets:
            target_y = int(y_ratio_target * y)
            turtle.goto(x, target_y)
            turtle.goto(x_side, y_side)
        x_side -= step

def draw_pattern_right(x, y, side, step, y_ratio, y_targets):
    y_side = int(y_ratio * y)
    x_side = -x
    turtle.goto(-x, y_side)
    turtle.goto(x, y_side)
    for _ in range(int(side / step)):
        for y_ratio_target in y_targets:
            target_y = int(y_ratio_target * y)
            turtle.goto(-x, target_y)
            turtle.goto(x_side, y_side)
        x_side += step

def design26(x, y):
    side = x + y

    turtle.penup()
    turtle.goto(-x, -y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    step = 10

    r = 0.75; targets = [1, 0.5]
    draw_pattern_left(x, y, side, step, r, targets)

    r = 0.5; targets = [0.75, 0.25]
    draw_pattern_right(x, y, side, step, r, targets)

    r = 0.25; targets = [0.5, 0]
    draw_pattern_left(x, y, side, step, r, targets)

    r = 0; targets = [0.25, -0.25]
    draw_pattern_right(x, y, side, step, r, targets)

    r = -0.25; targets = [0, -0.5]
    draw_pattern_left(x, y, side, step, r, targets)

    r = -0.5; targets = [-0.25, -0.75]
    draw_pattern_right(x, y, side, step, r, targets)

    r = -0.75; targets = [-0.5, -1]
    draw_pattern_left(x, y, side, step, r, targets)

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(1)
turtle.speed(0)

design26(200, 200)

turtle.hideturtle()
turtle.done()