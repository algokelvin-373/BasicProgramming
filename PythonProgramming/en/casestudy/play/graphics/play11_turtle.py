import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)

# Must s1 > s2
s1 = 100
s2 = 50
for _ in range(4):
    turtle.penup()
    turtle.forward(s1)
    turtle.pendown()
    for _ in range(4):
        for _ in range(4):
            turtle.forward(s2)
            turtle.left(90)
        turtle.left(90)
    turtle.goto(0, 0)
    turtle.left(90)

turtle.hideturtle()
turtle.done()