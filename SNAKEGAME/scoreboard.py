from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260) 
        self.score = 0
        self.highest_score = 0
        self.write_score()
    def write_score(self):
        self.clear()  # Clear previous score before writing the new one
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
        self.goto(0, -40)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.score = 0