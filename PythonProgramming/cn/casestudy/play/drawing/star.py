import turtle

def draw_star(size):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(5)
    star.color("yellow")
    star.pensize(3)

    star.penup()
    star.goto(-(size / 2), 50)
    star.pendown()

    # Make object star
    for _ in range(5):
        star.forward(size)
        star.right(144)

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("#0b1b2b")  # night sky

draw_star(400)

turtle.done()
