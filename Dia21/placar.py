from turtle import Turtle


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.n = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"placar: {self.n}", align="center", font=("Arial", 16, "bold"))


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "bold"))

    def update_placar(self):
        self.n +=1
        self.clear()
        self.write(f"placar: {self.n}", align="center", font=("Arial", 16, "bold"))