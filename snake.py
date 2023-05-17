from turtle import Turtle, Screen
import random
import time


my_screen = Screen()

y_coord = random.randint(-260, 260)
x_coord = random.randint(-260, 260)

STARTING_CORDS = [(x_coord, y_coord), (x_coord - 20, y_coord), (x_coord - 40, y_coord)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class XenziaShape:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in range(0, len(STARTING_CORDS)):
            self.add_body(STARTING_CORDS[position])

    def add_body(self, position):
        mr_cobra = Turtle(shape="square")
        mr_cobra.color("white")
        mr_cobra.penup()
        mr_cobra.goto(position)
        self.snake_body.append(mr_cobra)

    #Add a new body to the snake
    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        # is_game_on = True
        # while is_game_on:
        #     my_screen.update()
        #     time.sleep(0.25)
        for body_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_num-1].xcor()
            new_y = self.snake_body[body_num-1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]