import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

colors = [
    'red',
    'green',
    'blue',
    'orange',
    'brown',
    'gray',
    'purple',
    'yellow',
    'black'
]

side = 20
dimension = 4
count = 45
for _ in range(dimension):
    s = side
    for i in range(count):
        turtle.color(colors[i % len(colors)])
        turtle.penup()
        turtle.pendown()
        for _ in range(4):
            turtle.forward(s)
            turtle.left(90)
        s += 5
    turtle.left(360 / dimension)

turtle.hideturtle()
turtle.done()