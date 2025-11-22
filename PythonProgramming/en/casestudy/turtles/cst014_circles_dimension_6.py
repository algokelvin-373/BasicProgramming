import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(3)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

turtle.circle(400, 90)
turtle.right(270)
turtle.circle(400, 90)

turtle.hideturtle()
turtle.done()