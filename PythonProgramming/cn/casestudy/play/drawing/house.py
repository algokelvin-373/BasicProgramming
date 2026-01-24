import turtle

def draw_house(size):
    house = turtle.Turtle()
    house.hideturtle()
    house.speed(10)
    house.pensize(3)

    body_height = 0.5 * size
    roof_height = 0.3 * size

    house.penup()
    house.goto(-(size / 2), -size / 2)
    house.pendown()

    # Draw body house
    house.color("#f5c16c")  # warm wall color
    house.penup()
    house.goto(-size / 2, -body_height / 2)
    house.pendown()
    house.begin_fill()
    for _ in range(2):
        house.forward(size)
        house.left(90)
        house.forward(body_height)
        house.left(90)
    house.end_fill()

    # Draw roof
    house.color("#c0392b")  # roof color
    house.penup()
    house.goto(-size / 2, body_height / 2)
    house.pendown()
    house.begin_fill()
    house.goto(0, body_height / 2 + roof_height)
    house.goto(size / 2, body_height / 2)
    house.goto(-size / 2, body_height / 2)
    house.end_fill()

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("#0b1b2b")  # night sky

draw_house(400)

turtle.done()
