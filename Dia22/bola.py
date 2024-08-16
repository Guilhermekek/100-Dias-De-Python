from turtle import Turtle
import random
class Bola(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_mover = 10
        self.y_mover = 10

    def mover(self):
        novo_x = self.xcor() + self.x_mover
        novo_y = self.ycor() + self.y_mover
        self.goto(novo_x, novo_y)

    def ricochetear_y(self):
        self.y_mover *= -1

    def ricochetear_x(self):
        self.x_mover *= -1

    def resetar(self):
        self.goto(0, 0)