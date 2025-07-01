from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
is_game_on = True 
l_paddle_score = ScoreBoard((-80,250))
r_paddle_score = ScoreBoard((80,250))
while (is_game_on):
    time.sleep(.001)
    screen.update()
    ball.move()
    
    # detect collisions 
    if ball.ycor()>300 or ball.ycor()<-300:
        ball.y_bounce()
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.x_bounce()
        l_paddle_score.update_score()
    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.x_bounce()
        r_paddle_score.update_score()
    if ball.distance(r_paddle) <50 or ball.distance(l_paddle) <50:
        ball.x_bounce()

screen.exitonclick()