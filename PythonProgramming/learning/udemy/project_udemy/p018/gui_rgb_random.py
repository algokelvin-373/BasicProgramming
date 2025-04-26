import turtle as t
import random

color = ['Red', 'Blue', 'Yellow', 'Green', 'Orange', 'Pink', 'Purple', 'Black', 'Grey', 'Brown']

t.colormode(255)
gui = t.Turtle()
gui.speed('fastest')
gui.penup()

gui.setheading(180)
gui.forward(300)
gui.setheading(-90)
gui.forward(300)

data = 1
while data <= 120:
    gui.dot(20, random.choice(color))
    gui.setheading(360)
    gui.forward(50)
    if data % 12 == 0:
        gui.setheading(180)
        gui.forward(12 * 50)
        gui.setheading(90)
        gui.forward(50)
    data += 1

screen = t.Screen()
screen.exitonclick()