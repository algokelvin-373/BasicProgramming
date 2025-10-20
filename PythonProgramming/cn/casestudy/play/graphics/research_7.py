import turtle

turtle.setup(width=800, height=800)
turtle.color('black')
turtle.pensize(2)
turtle.speed(0)

# Test 1
# 50, 70, 100, 140, 200, 280, 390
#   20  30   40   60   80  110
#     10   10  20   20   30

# s = 50
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# s = 70
turtle.penup()
turtle.goto(0, -70)
turtle.pendown()
turtle.circle(70)

turtle.penup()
turtle.goto(-70, -70)
turtle.pendown()
for _ in range(4):
    turtle.forward(140)
    turtle.left(90)

# s = 100
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
for _ in range(4):
    turtle.forward(200)
    turtle.left(90)

# s = 140
turtle.penup()
turtle.goto(0, -140)
turtle.pendown()
turtle.circle(140)

turtle.penup()
turtle.goto(-140, -140)
turtle.pendown()
for _ in range(4):
    turtle.forward(280)
    turtle.left(90)

# s = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
for _ in range(4):
    turtle.forward(400)
    turtle.left(90)

# s = 280
turtle.penup()
turtle.goto(0, -280)
turtle.pendown()
turtle.circle(280)

turtle.penup()
turtle.goto(-280, -280)
turtle.pendown()
for _ in range(4):
    turtle.forward(560)
    turtle.left(90)

# s = 390
turtle.penup()
turtle.goto(0, -390)
turtle.pendown()
turtle.circle(390)

turtle.penup()
turtle.goto(-390, -390)
turtle.pendown()
for _ in range(4):
    turtle.forward(780)
    turtle.left(90)

turtle.hideturtle()
turtle.done()
