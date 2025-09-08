import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(2)
turtle.speed(0)

colors = ['red', 'green', 'blue']
index_color = 0
radius = 100
step = 6

turtle.penup()
turtle.goto(0, -radius)
turtle.pendown()
for angle in range(0, 360, step):
    if angle % 120 == 0 and angle > 0:
        index_color = (index_color + 1) % len(colors)
        turtle.color(colors[index_color])

    arc_length = 2 * 3.14159 * radius * step / 360
    turtle.forward(arc_length)
    turtle.left(step)


turtle.hideturtle()
turtle.done()