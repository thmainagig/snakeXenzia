from turtle import Screen
from snake import XenziaShape
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Xenzia Game!")
my_screen.tracer(0)

snake = XenziaShape()
foodie = Food()
scoreboard = ScoreBoard()

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

    # Detect if snake ate food and add score and snake body

    if snake.head.distance(foodie) < 14:
        foodie.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scoreboard.game_over()
        is_game_on=False

    #Detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body)<10:
            scoreboard.game_over()
            is_game_on=False


my_screen.exitonclick()