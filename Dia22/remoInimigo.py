from turtle import Turtle

posicoes_inicias_inimigo= [(350,0),(350,20),(350,40),(350,60),(350,80)]
class RemoInimigo(Turtle):

    def __init__(self):
        super().__init__()
        self.segmentos = []
        self.criar_remo_inimigo()
        self.head = self.segmentos[0]
        self.tail = self.segmentos[-1]
        self.direcao = 270

    def criar_remo_inimigo(self):
        for posicao in posicoes_inicias_inimigo:
            self.adicionar_remo(posicao)

    def adicionar_remo(self, posicao):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(posicao)
        self.segmentos.append(t)

    def detectar_parede(self):
        if self.head.ycor() <= -280:
            self.direcao = 90
        elif self.head.ycor() >= 280:
            self.direcao = 270

    def mover(self):
        self.detectar_parede()
        for i in range(len(self.segmentos) - 1, 0, -1):
            new_x = self.segmentos[i - 1].xcor()
            new_y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(new_x, new_y)
        self.head.setheading(self.direcao)
        self.head.forward(20)
