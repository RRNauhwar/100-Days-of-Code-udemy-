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
        self.get_highest_score()
        self.write_score()
    def write_score(self):
        self.clear()  # Clear previous score before writing the new one
        self.write(f"Score: {self.score} Highest score:{self.highest_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset_highest_score(self):
        if self.score>self.highest_score:
            self.highest_score = self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
        self.goto(0, -40)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.reset_highest_score()
        self.score = 0
        with open("highest_score.txt",mode = "w") as file:
            file.write(str(self.highest_score))

    def get_highest_score(self):
        with open("highest_score.txt",mode="r") as file:
            self.highest_score = int(file.read())
