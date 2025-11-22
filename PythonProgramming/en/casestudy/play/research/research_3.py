import turtle

turtle.setup(width=500, height=500)
turtle.color('black')
turtle.pensize(1)

r = 200

turtle.penup()
turtle.goto(0, -r)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

r -= 10

turtle.penup()
turtle.goto(0, -r)
turtle.pendown()
turtle.color('white')
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

turtle.hideturtle()
turtle.done()