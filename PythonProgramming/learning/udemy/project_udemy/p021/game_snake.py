from turtle import Turtle, Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake eat food
    if snake.head.distance(food) < 15:
        print("Nyam nyam")
        food.refresh()
        scoreboard.increase_score()

    # Detect Wall
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < - 230:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()