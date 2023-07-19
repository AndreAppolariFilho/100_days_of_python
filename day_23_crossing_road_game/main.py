import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
t = Player()
cm = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=t.move_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cm.generate_cars()
    cm.move_cars()
    if cm.check_collision_with_player(t):
        game_is_on = False
        sb.draw_game_over()
    if t.check_objective():
        sb.update_level()
        t.reset_position()
        cm.update_cars_speed()


screen.exitonclick()