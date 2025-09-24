import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('salmon')
turtle.pensize(2)
turtle.speed(50)

# square center
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.begin_fill()
for _ in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

# side 1
x1 = -200
y1 = 200
while x1 < -100:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    x1 += 10
while y1 > 100:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    y1 -= 10

turtle.right(180)

# Side 2
x1 = 200
y1 = -200

while x1 > 100:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    x1 -= 10
while y1 < -100:
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    y1 += 10

turtle.hideturtle()
turtle.done()