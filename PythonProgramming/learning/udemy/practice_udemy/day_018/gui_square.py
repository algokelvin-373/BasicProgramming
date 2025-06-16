import random
import turtle as t

gui = t.Turtle()

time = 1
while time <= 4:
    gui.forward(100)
    gui.right(90)
    time += 1

screen = t.Screen()
screen.exitonclick()