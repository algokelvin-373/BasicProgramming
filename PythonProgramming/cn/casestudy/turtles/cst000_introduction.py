import turtle

turtle.setup(width=400, height=200)
turtle.color('black')
turtle.pensize(0)

turtle.penup()  # Not make draw line

turtle.goto(0, 0)
turtle.write(
    'Python 代码 - Turtle',
    align='center',
    font=("Arial", 18, "bold")
)

turtle.hideturtle()
turtle.done()