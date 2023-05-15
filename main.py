import time
from turtle import Screen, Turtle
import random

my_screen = Screen()

my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Xenzia Game!")
my_screen.tracer(0)

snake_body = []
class XenziaShape():
    y_coord = random.randint(-260,260)
    x_coord= random.randint(-260, 260)
    starting_position=[(x_coord,y_coord), (x_coord-20, y_coord), (x_coord-40, y_coord)]
    for _ in range(0,3):
        mr_cobra = Turtle(shape="turtle")
        mr_cobra.color("white")
        mr_cobra.penup()
        mr_cobra.goto(starting_position[_])
        snake_body.append(mr_cobra)


is_game_on=True
while is_game_on:
    my_screen.update()
    time.sleep(0.025)
    for body in snake_body:
        body.forward(10)

        # if body.xcors >590:
        #     is_game_on=False
        #     print("Game Over!")



XenziaShape()


my_screen.exitonclick()