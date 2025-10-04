import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(2)
turtle.speed(50)

# background
turtle.color('red', 'lightblue')
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.begin_fill()
for _ in range(4):
    turtle.forward(400)
    turtle.left(90)
turtle.end_fill()

# side 1 [left, top]
for i in range(100):
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.circle(i + 3, 90)


turtle.hideturtle()
turtle.done()