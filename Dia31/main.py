from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
window = Tk()
window.title("Flash Card")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


palavra_sorteada = {}


canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_imagem = canvas.create_image(400, 263, image=card_front_img)

titulo = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
palavra = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

def load_data():
    try:
        df = pd.read_csv("data/palavras_para_aprender.csv")
    except FileNotFoundError:
        original_data = pd.read_csv("data/french_words.csv")
        print(original_data)
        palavras_para_aprender = original_data.to_dict(orient="records")
    else:
        palavras_para_aprender = df.to_dict(orient="records")
    return palavras_para_aprender
palavras_frances_dict = load_data()
def update_csv():
    palavras_frances_dict.remove(palavra_sorteada)
    df = pd.DataFrame(palavras_frances_dict)
    df.to_csv("data/palavras_para_aprender.csv")

def certo():
    global palavra_sorteada, rodar_card_tempo
    window.after_cancel(rodar_card_tempo)
    palavra_sorteada = random.choice(palavras_frances_dict)
    canvas.itemconfig(titulo,text="French",fill="black")
    canvas.itemconfig(palavra, text=palavra_sorteada["French"], fill="green")
    canvas.itemconfig(canvas_imagem, image=card_front_img)
    update_csv()
    rodar_card_tempo = window.after(3000, func=rodar_card)

def errado():
    global palavra_sorteada, rodar_card_tempo
    palavra_sorteada = random.choice(palavras_frances_dict)
    canvas.itemconfig(titulo, text="French", fill="black")
    canvas.itemconfig(palavra, text=palavra_sorteada["French"], fill="red")
    canvas.itemconfig(canvas_imagem, image=card_front_img)
    rodar_card_tempo = window.after(3000, func=rodar_card)

def rodar_card():
    canvas.itemconfig(titulo,text="English",fill="white")
    canvas.itemconfig(palavra, text=palavra_sorteada["English"], fill="white")
    canvas.itemconfig(canvas_imagem,image=card_back_img)

rodar_card_tempo = window.after(3000, func=rodar_card)
errado_img = PhotoImage(file="images/wrong.png")
errado_button = Button(image=errado_img,command=errado, highlightthickness=0)
errado_button.grid(column=0,row=1)

certo_img = PhotoImage(file="images/right.png")
certo_button = Button(image=certo_img,command=certo, highlightthickness=0)
certo_button.grid(column=1,row=1)

window.mainloop()