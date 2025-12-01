import turtle

def koch(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch(length, depth - 1)
        turtle.left(60)
        koch(length, depth - 1)
        turtle.right(120)
        koch(length, depth - 1)
        turtle.left(60)
        koch(length, depth - 1)

def snowflake(length, depth):
    for _ in range(3):
        koch(length, depth)
        turtle.right(120)

# Simple setup
turtle.setup(500, 500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.pensize(2)
turtle.speed(0)
turtle.penup()
turtle.goto(-150, 100)  # Center it a bit
turtle.pendown()

# Draw
snowflake(300, 4)

turtle.hideturtle()
turtle.done()