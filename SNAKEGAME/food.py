from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")

        self.refresh()
     
    def refresh(self):
        rand_x = random.randint(-380,380)
        rand_y = random.randint(-250,250)
        self.goto(rand_x,rand_y)