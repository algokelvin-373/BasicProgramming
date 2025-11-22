import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(2)

s = 60
turtle.penup()
turtle.goto(-30, -30)
turtle.pendown()
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)

s = 80
turtle.penup()
turtle.goto(-40, -40)
turtle.pendown()
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)

s = 100
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)
turtle.forward(s)
turtle.left(120)

turtle.hideturtle()
turtle.done()