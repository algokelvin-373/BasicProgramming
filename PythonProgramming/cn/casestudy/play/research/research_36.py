import turtle
import random

# ====== Setup ======
screen = turtle.Screen()
screen.title("Background - Natal & Tahun Baru")
screen.bgcolor("#0b1b2b")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def jump(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def snow(count=140):
    t.penup()
    for _ in range(count):
        t.goto(random.randint(-330, 330), random.randint(-220, 280))
        t.dot(random.randint(2, 4), "white")
    t.pendown()

def ground():
    t.color("#e8f1ff")
    jump(-400, -240)
    t.begin_fill()
    t.goto(400, -240)
    t.goto(400, -170)
    t.goto(-400, -170)
    t.goto(-400, -240)
    t.end_fill()

def draw_background():
    snow(150)
    ground()

draw_background()
turtle.done()
