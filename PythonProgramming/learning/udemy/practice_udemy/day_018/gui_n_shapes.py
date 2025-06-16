import random
import turtle as t

gui = t.Turtle()

def draw_n_shapes(n):
    time = 1
    while time <= n:
        gui.forward(25)
        gui.right(360/n)
        time += 1

for s in range (3, 20):
    draw_n_shapes(s)

screen = t.Screen()
screen.exitonclick()