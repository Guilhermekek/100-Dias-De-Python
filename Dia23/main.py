import time
from turtle import Screen
from player import Player
from carro_controle import CarManager
from placar import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carro_controle = CarManager()
placar = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    carro_controle.criar_carro()
    time.sleep(0.1)
    screen.update()
    carro_controle.move()

    for carro in carro_controle.all_cars:
        if player.distance(carro) < 10:
            print(player.distance(carro))
            game_is_on = False
            placar.game_over()

    if player.is_at_finish_line():
        placar.increase_level()
        carro_controle.increase_speed()


