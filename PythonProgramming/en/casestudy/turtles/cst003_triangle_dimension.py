import turtle


def equilateral_triangle(side_length):
    height = (side_length * (3 ** 0.5)) / 2
    x_start = -side_length / 2
    y_start = -height / 2

    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()

    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)  # Turn Left 120

def draw_triangles(count, initial_side, step):
    side = initial_side
    for _ in range(count):
        equilateral_triangle(side)
        side += 2 * step


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_triangles(count=20, initial_side=20, step=10)

turtle.hideturtle()
turtle.done()