from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(0.5, 0.5, 0.25)
        self.color("gold")
        self.new_location()

    def new_location(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.setposition(x_position, y_position)
