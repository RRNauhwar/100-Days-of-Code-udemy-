from turtle import Turtle 

class ScoreBoard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.pos = position
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto (self.pos)
        self.write(self.score,font=("Arial", 30, "normal"))

    def update_score(self):
        self.clear()
        self.score +=1
        self.write(self.score,font=("Arial", 30, "normal"))