import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
p1 = Paddle()
p2 = Paddle(-350, 0)
b = Ball()
s = Scoreboard()

screen.listen()
screen.onkeypress(
    key= "Up",
    fun=p1.go_up
)
screen.onkeypress(
    key= "Down",
    fun=p1.go_down
)
screen.onkeypress(
    key= "w",
    fun=p2.go_up
)
screen.onkeypress(
    key= "s",
    fun=p2.go_down
)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if b.turtle.ycor() >= 280 or b.turtle.ycor() <= -280:
        b.change_y_direction()
    elif (b.turtle.distance(p1.turtle) < 50 and b.turtle.xcor() > 320) or\
            (b.turtle.distance(p2.turtle) < 50 and b.turtle.xcor() < -320):
        b.change_x_direction()
        b.add_speed()
    elif b.turtle.xcor() >= 380:
        s.update_scoreboard_left()
        b.reset_position()
    elif b.turtle.xcor() <= -380:
        s.update_scoreboard_right()
        b.reset_position()
    b.move_ball()










screen.exitonclick()