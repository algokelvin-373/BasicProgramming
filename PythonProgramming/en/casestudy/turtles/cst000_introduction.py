import turtle

turtle.setup(width=400, height=200)
turtle.color('black')
turtle.pensize(0)

turtle.penup()      # Not make draw line

turtle.goto(0, 0)
turtle.write(
    "Python Code - Turtle",
        align="center",
        font=("Arial", 20, "bold")
)
turtle.hideturtle()
turtle.done()