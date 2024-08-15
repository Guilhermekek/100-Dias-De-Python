from turtle import Screen
from cobra import Cobra
from comida import Comida
from placar import Placar
import time

#arquivo principal
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Dia 20 - Jogo da Cobra")
screen.tracer(0)

game_is_on = True


cobra = Cobra()
comida = Comida()
placar = Placar()


screen.listen()
screen.onkey(cobra.virar_para_cima, "Up")
screen.onkey(cobra.virar_para_baixo, "Down")
screen.onkey(cobra.virar_para_esquerda, "Left")
screen.onkey(cobra.virar_para_direita, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    cobra.mover()

    # detectar quando a comida e a cobra colidirem
    if cobra.head.distance(comida) < 15:
        comida.refresh()
        placar.update_placar()
        cobra.crescer()

    # detectar colisao com a parede
    if cobra.head.xcor()> 280 or cobra.head.xcor() < -280 or cobra.head.ycor()> 280 or cobra.head.ycor() < -280:
        game_is_on = False
        placar.game_over()

    # detectar colisao com o rabo
    for segmento in cobra.segmentos[1:]:
        if cobra.head.distance(segmento) < 10:
            game_is_on = False
            placar.game_over()

screen.exitonclick()