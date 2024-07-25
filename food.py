from turtle import Turtle
import time
import random

class Food(Turtle):  # our Food class inherits from the Turtle class

    def __init__(self):
        super().__init__() # Ensures that it inherits the attributes from the super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_y, new_y)




