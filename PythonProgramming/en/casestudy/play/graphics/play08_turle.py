import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

side = 20
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink']
dimension = len(colors)
for i in range(dimension):
    s = side
    for _ in range(20):
        turtle.penup()
        turtle.pendown()
        turtle.color(colors[i])
        turtle.circle(s)
        s += 5
    turtle.left(360/dimension)

turtle.hideturtle()
turtle.done()