import turtle

# Binary Tree

def tree(branch_len, depth):
    if depth == 0:
        return
    turtle.forward(branch_len)
    turtle.left(30)
    tree(branch_len * 0.7, depth - 1)
    turtle.right(60)
    tree(branch_len * 0.7, depth - 1)
    turtle.left(30)
    turtle.backward(branch_len)

# Setup
turtle.setup(500, 500)
turtle.bgcolor('black')
turtle.color('green')
turtle.pensize(2)
turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)    # Start from bottom
turtle.pendown()

# Draw tree
tree(125, 10)

turtle.hideturtle()
turtle.done()