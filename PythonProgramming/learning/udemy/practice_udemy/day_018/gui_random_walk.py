import random
from turtle import Turtle, Screen

gui = Turtle()

color = ['Red', 'Blue', 'Green']
direction = [0, 90, 180, 270]

gui.pensize(10)
gui.speed('fastest')
for _ in range(300):
    gui.color(random.choice(color))
    gui.forward(20)
    gui.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()