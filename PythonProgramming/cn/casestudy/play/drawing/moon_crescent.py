import turtle

bg = "#0b1b2b"          # background color
moon_color = "#808080"  # moon color

def obj_circle(t, bg_color, x, radius):
    t.color(bg_color)
    t.penup()
    t.goto(x, -radius)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_crescent(radius):
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.speed(5)
    moon.pensize(0)

    # Object 1: Moon Full Circle
    obj_circle(moon, moon_color, 0, radius)
    # Object 2: Moon Crescent Cutout
    obj_circle(moon, bg, 100, radius)


screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor(bg)

draw_crescent(150)

turtle.done()
