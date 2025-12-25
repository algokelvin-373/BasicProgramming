import turtle

bg = "#0b1b2b"      # background color
moon_color = "yellow"

def draw_crescent(radius):
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.speed(5)
    moon.pensize(0)

    # Object 1
    moon.color(moon_color)
    moon.penup()
    moon.goto(0, -radius)
    moon.pendown()
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()

    # Object 2
    moon.color(bg)
    moon.penup()
    moon.goto(60, -radius)
    moon.pendown()
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()


screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor(bg)

draw_crescent(150)

turtle.done()
