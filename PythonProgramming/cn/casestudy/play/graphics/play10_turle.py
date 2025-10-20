import turtle

turtle.setup(width=600, height=600)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

colors = [
    'red',
    'green',
    'blue',
    'brown',
    'purple'
]

x_position = 250
y_position = 250
side = 500
for i in range(25):
    color = colors[i % len(colors)]
    turtle.penup()
    turtle.goto(-x_position, -y_position)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()
    side -= 20
    x_position -= 10
    y_position -= 10

turtle.hideturtle()
turtle.done()