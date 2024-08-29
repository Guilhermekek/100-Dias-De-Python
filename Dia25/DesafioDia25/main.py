import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('Dia25 - U.S States Games')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pd.read_csv("50_states.csv")

todos_os_estados = []

def funaçao(x,y,estado):
    p = turtle.Turtle()
    p.penup()
    p.hideturtle()
    p.goto(x, y)
    p.write(estado, align="center", font=("Courier", 4, "normal"))

# print("California" in data["state"].values)
# print(data["state"])
contador = 0
acertos = []
while contador < 50:
    answer_state = screen.textinput(title=f'{contador}/50Advinhe o estado', prompt='Qual o nome do estado?')
    if answer_state.title() in acertos:
        print("Voce ja forneceu esse estado")
    else:
        if answer_state.title() in data["state"].values:
            estado_data = data[data.state == answer_state.title()]
            x = int(estado_data["x"])
            y = int(estado_data["y"])
            funaçao(x,y,answer_state.title())
            acertos.append(answer_state.title())
            contador +=1
        else:
            print("Voce errou!")

turtle.mainloop()

# como a professora fez :

# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)
