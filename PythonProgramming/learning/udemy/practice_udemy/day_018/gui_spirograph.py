import random
import turtle as t

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        gui.color(random_color())
        gui.circle(100)
        gui.setheading(gui.heading() + size_of_graph)

gui = t.Turtle()
t.colormode(255)

gui.speed('fastest')

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()