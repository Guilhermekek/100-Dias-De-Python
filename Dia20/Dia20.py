from turtle import Screen
from cobra import Cobra
import time

#arquivo principal
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Dia 20 - Jogo da Cobra")
screen.tracer(0)

game_is_on = True


cobra = Cobra()

screen.listen()
screen.onkey(cobra.virar_para_cima, "Up")
screen.onkey(cobra.virar_para_baixo, "Down")
screen.onkey(cobra.virar_para_esquerda, "Left")
screen.onkey(cobra.virar_para_direita, "Right")
def comer():
    pass


while game_is_on:
    screen.update()
    time.sleep(0.1)
    cobra.mover()

screen.exitonclick()