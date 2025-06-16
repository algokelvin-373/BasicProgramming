import random
from turtle import Turtle, Screen


def position_turtle(all_turtle, color, position):
    gui = Turtle(shape="turtle")
    gui.color(color)
    gui.penup()
    gui.goto(x=-230, y=position)
    all_turtle.append(gui)

def display_message(text):
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.color("white")
    writer.goto(0, 160)
    writer.write(text, align="center", font=("Arial", 16, "bold"))

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color:"
)

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    position_turtle(
        all_turtles,
        colors[turtle_index],
        y_positions[turtle_index]
    )

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                message = f"You win! The {winning_color} turtle is the winner"
            else:
                message = f"You lose! The {winning_color} turtle is the winner"
            display_message(message)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()