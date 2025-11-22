import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)
turtle.speed(0)

count = 0
side = 200
angle = 5
colors = ['red', 'green', 'blue']
j = 0
while count <= 360:
    if 120 <= count < 240:
        j = 1
    elif count >= 240:
        j = 2
    turtle.penup()
    turtle.pendown()
    turtle.color(colors[j])
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.left(angle)
    count += angle

turtle.hideturtle()
turtle.done()