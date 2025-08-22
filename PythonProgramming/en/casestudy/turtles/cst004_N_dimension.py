import turtle

def draw_N_dimension(dimension, count, side, step):
    for i in range(count):
        turtle.penup()
        turtle.goto(-side/2, -side/2)
        turtle.pendown()
        for _ in range(dimension):
            turtle.forward(side)
            turtle.left(360/dimension)
        side += step

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_N_dimension(6, 20, 20, 10)

turtle.hideturtle()
turtle.done()