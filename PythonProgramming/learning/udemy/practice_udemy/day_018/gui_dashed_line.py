import random
import turtle as t

gui = t.Turtle()

for _ in range(15):
    gui.forward(10)
    gui.penup()
    gui.forward(10)
    gui.pendown()

screen = t.Screen()
screen.exitonclick()