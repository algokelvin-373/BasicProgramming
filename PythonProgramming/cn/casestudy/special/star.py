import turtle

def draw_star(size):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color("yellow")
    star.pensize(3)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

screen = turtle.Screen()
screen.bgcolor("#0b1b2b")  # night sky

draw_star(150)

turtle.done()
