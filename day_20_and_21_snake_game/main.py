from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

game_is_on = True
screen.listen()
screen.onkey(key="Up", fun=snake.rotate_up)
screen.onkey(key="Down", fun=snake.rotate_down)
screen.onkey(key="Left", fun=snake.rotate_left)
screen.onkey(key="Right", fun=snake.rotate_right)

while game_is_on:
    screen.update()
    time.sleep(1 / 10)

    snake.move_forward()

    if food.distance(snake.head) <= 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    for segment in snake.snake_body[1::]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
            
screen.exitonclick()