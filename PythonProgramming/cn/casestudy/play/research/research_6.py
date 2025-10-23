import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(2)


turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Left (-) or Right (+)
turtle.circle(100, -180)

# Bottom (-) or Top (+)
turtle.setheading(-90)
turtle.circle(100, 180)

turtle.hideturtle()
turtle.done()