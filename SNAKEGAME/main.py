from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(800, 600)  # Wider to fit large turtles
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # detect collisions with wall
    if (snake.head.xcor()>=400 or snake.head.xcor()<=-400 or snake.head.ycor()>=300 or snake.head.ycor()<=-300):
        is_game_on = False
        scoreboard.game_over()
    # detect collisions with wall 
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()