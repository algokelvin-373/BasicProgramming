import turtle

turtle.setup(width=500, height=500)
turtle.bgcolor('black')
turtle.color('lightblue')
turtle.pensize(1)
# turtle.speed(0)

# 100 left top
x1 = 0
y1 = 0
turtle.goto(x1,y1)
turtle.forward(100)
turtle.goto(x1,y1)
turtle.backward(100)
x2 = turtle.xcor()
y2 = turtle.ycor()
turtle.left(90)
turtle.forward(100)
# Execute for 50


# 50 left top
turtle.right(90)
x = turtle.xcor()
y = turtle.ycor()
turtle.goto(x,y)
turtle.forward(50)
turtle.goto(x,y)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)

# 50 left bottom
turtle.right(180)
turtle.forward(100) # 2 * 50

# 50 right top
turtle.penup()
turtle.goto(x,y)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# 50 right bottom
turtle.right(180)
turtle.forward(100) # 2 * 50

# 100 left bottom
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.forward(100)
# Execute for 50

# 50 left top
turtle.right(90)
x = turtle.xcor()
y = turtle.ycor()
turtle.goto(x,y)
turtle.forward(50)
turtle.goto(x,y)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)

# 50 left bottom
turtle.right(180)
turtle.forward(100) # 2 * 50

# 50 right top
turtle.penup()
turtle.goto(x,y)
turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# 50 right bottom
turtle.right(180)
turtle.forward(100) # 2 * 50

# 100 right top
turtle.right(90)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.hideturtle()
turtle.done()