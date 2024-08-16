# Criar o jogo de ping pong do zero ou seguir os passos da professora

# decidi criar uma versao do zero e depois irei comparar com a versao seguindo os passos da professora

from turtle import Turtle,Screen
from remo import Remo
from remoInimigo import RemoInimigo
from placar import Placar
from bola import Bola
import random
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Dia 20 - Jogo do Ping Pong")
screen.tracer(0)



game_is_on = True
remo = Remo()
remoInimigo = RemoInimigo()
placar = Placar()
bola = Bola()
screen.listen()
screen.onkey(remo.ir_para_cima, "Up")
screen.onkey(remo.ir_para_baixo, "Down")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    remoInimigo.mover()
    bola.mover()
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.ricochetear_y()
    if bola.distance(remo) < 50 and bola.xcor() > 320 or bola.distance(remoInimigo) < 50 and bola.xcor() < -320:
        bola.ricochetear_x()

    if bola.xcor() > 380:
        bola.resetar()

screen.exitonclick()