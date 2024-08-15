from turtle import Turtle
# aquivo da cobra

posicoes_inicias = [(0,0),(-20,0),(-40,0)]

class Cobra:
    def __init__(self):
        self.segmentos = []
        self.criar_cobra()
        self.head = self.segmentos[0]

    def criar_cobra(self):
        for posicao in posicoes_inicias:
            self.adicionar_cobra(posicao)

    def adicionar_cobra(self,posicao):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(posicao)
        self.segmentos.append(t)
    def crescer(self):
        self.adicionar_cobra(self.segmentos[-1].position())

    def mover(self):
        for i in range(len(self.segmentos) -1, 0, -1):
            new_x = self.segmentos[i - 1].xcor()
            new_y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(new_x, new_y)
        self.segmentos[0].forward(20)

    def virar_para_cima(self):
        if self.segmentos[0].heading() != 270:
            self.segmentos[0].setheading(90)
    def virar_para_baixo(self):
        if self.segmentos[0].heading() != 90:
            self.segmentos[0].setheading(270)
    def virar_para_esquerda(self):
        if self.segmentos[0].heading() != 0:
            self.segmentos[0].setheading(180)
    def virar_para_direita(self):
        if self.segmentos[0].heading() != 180:
            self.segmentos[0].setheading(0)

