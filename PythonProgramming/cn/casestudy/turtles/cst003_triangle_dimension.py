import turtle

def draw_triangles(count, side, step):
    for i in range(count):
        turtle.penup()
        turtle.goto(-side/2, -side/2)
        turtle.pendown()
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)
        side += step


turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(0)

draw_triangles(count=20, side=40, step=20)

turtle.hideturtle()
turtle.done()