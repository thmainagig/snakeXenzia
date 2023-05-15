import time
from turtle import Screen, Turtle
import random
from snake import XenziaShape

my_screen = Screen()
snake = XenziaShape()

my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Xenzia Game!")
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on=True
while is_game_on:
    my_screen.update()
    time.sleep(0.25)
    snake.move()


my_screen.exitonclick()