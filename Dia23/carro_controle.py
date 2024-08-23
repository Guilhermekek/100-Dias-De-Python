COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
        super ().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.criar_carro()


    def criar_carro(self):
        carro = Turtle('square')
        carro.color(random.choice(COLORS))
        carro.penup()
        carro.shapesize(stretch_wid=1, stretch_len=2)
        carro.goto(300, random.randint(-250, 250))
        self.all_cars.append(carro)
    def move(self):
        for i in self.all_cars:
            i.goto(i.xcor() - self.move_speed, i.ycor())

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE


