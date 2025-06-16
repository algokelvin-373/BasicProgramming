# GUI Turtle Higher Order Functions

from turtle import Turtle, Screen

gui = Turtle()
screen = Screen()

def move_forwards():
    gui.forward(10)

def move_backwards():
    gui.backward(10)

def turn_left():
    new_heading = gui.heading() + 10
    gui.setheading(new_heading)

def turn_right():
    new_heading = gui.heading() - 10
    gui.setheading(new_heading)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()
