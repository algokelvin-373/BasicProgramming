import turtle

# Sierpinski Triangle

def sierpinski(length, depth):
    if depth == 0:
        # Draw a filled triangle
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recurse on 3 corners
        sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

# Setup
turtle.setup(500, 500)
turtle.bgcolor('black')
turtle.color('aqua')
turtle.speed(0)
turtle.penup()
turtle.goto(-150, -100)  # Bottom-left start
turtle.pendown()

# Draw
sierpinski(300, 3)

turtle.hideturtle()
turtle.done()