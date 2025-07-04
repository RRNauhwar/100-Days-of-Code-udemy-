from turtle import Turtle
import random

class Race:
    def __init__(self, turtle_list, user_bet):
        self.turtles_list = turtle_list
        self.user_bet = user_bet

    def race(self):
        self.color_turtle()
        self.positions()
        self.start_race()

    def positions(self):
        curr_y = -180
        curr_x = -230
        a = 360 / len(self.turtles_list)
        for turtle in self.turtles_list:
            turtle.shape("turtle")
            turtle.penup()
            turtle.goto(x=curr_x, y=curr_y)
            curr_y += a

    def color_turtle(self):
        colors = ["red", "blue", "violet", "green", "pink", "yellow"]
        for turtle, color in zip(self.turtles_list, colors):
            turtle.color(color)

    def start_race(self):
        is_race_on = bool(self.user_bet)  # starts only if user bet

        while is_race_on:
            for turtle in self.turtles_list:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)
                if turtle.xcor() >= 240:
                    is_race_on = False
                    winning_color = turtle.color()[0]
                    self.show_result(winning_color)

    def show_result(self, winning_color):
        announcer = Turtle()
        announcer.hideturtle()
        announcer.penup()
        announcer.goto(0, 0)

        if self.user_bet.lower() == winning_color.lower():
            message = f"You've WON! 🏆 The {winning_color} turtle won!"
        else:
            message = f"You've LOST. ❌ The {winning_color} turtle won."

        announcer.write(message, align="center", font=("Arial", 16, "bold"))