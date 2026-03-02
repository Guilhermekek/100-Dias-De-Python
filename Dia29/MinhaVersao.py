
# Decidi criar uma versao sem ver os videos dela explicando como ela faz
# So olhei o primeiro video para ter uma ideia da aplicaçao que vou tentar reproduzir

from tkinter import *
from tkinter import messagebox
import random
import os
window = Tk()
window.title("Minha Senha")
window.minsize(500,400)
window.config(padx=40,pady=40,bg="white")

canvas = Canvas(width=200, height=224,bg="white", highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=mypass_img)
canvas.grid(column=1,row=0)


my_label_site = Label(text="Website:",bg="white")
my_label_site.grid(column=0,row=1)

my_entry_site = Entry(width=30)
my_entry_site.grid(column=1,row=1)

my_label_username = Label(text="Email/Username:",bg="white")
my_label_username.grid(column=0,row=2)

my_entry_username = Entry(width=30)
my_entry_username.grid(column=1,row=2)

my_label_password = Label(text="Password:", bg="white")
my_label_password.grid(column=0, row=3)

my_entry_password = Entry(width=10)
my_entry_password.grid(column=1,row=3,sticky="w")


def regras_senha():
    # qual é o maximo de caracter?
    # pode ter caracter repetido?
    # é obrigatorio algum caracter?
    # pode ter numero em sequencia?
    pass
# funçao para criar senha
def gerar_senha():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    senha = "".join(random.choice(chars) for _ in range(14))
    my_entry_password.delete(0, END)
    my_entry_password.insert(0, senha)

def guardar_senha(site,user,pwd):
    res = messagebox.askquestion("AppSenha",f"\nSite:     {site}\n"
                    f"User:     {user}\n"
                    f"Password: {pwd}\n"
                    "Esta Ok?")
    if res == "yes":
        if os.path.exists("senhas.txt"):
            with open("senhas.txt", "a", encoding="utf-8") as f:
                f.write(f"\nSite:     {site}\n"
                        f"User:     {user}\n"
                        f"Password: {pwd}")
            apagar_informacoes()

        else:
            with open("senhas.txt", "w", encoding="utf-8") as f:
                f.write("Aqui ficam salvos as informaçoes das suas senhas\n"
                        "Criado Por Guilherme Carvalho\n")
    else:
        print("Voltando")
def apagar_informacoes():
    my_entry_site.delete(0, END)
    my_entry_username.delete(0, END)
    my_entry_password.delete(0, END)
def pegar_informacoes():
    site = my_entry_site.get()
    user = my_entry_username.get()
    pwd = my_entry_password.get()
    if site == "" or user == "" or pwd == "":
        alerta = messagebox.showerror(title="Oops", message="Voce deixou um campo em branco")
    else:
        print(site, user, pwd)
        guardar_senha(site,user,pwd)

my_button_password = Button(text="Generate Password", command=gerar_senha)
my_button_password.grid(column=1, row=3,sticky="e")


my_button_guardar = Button(text="Add",justify="center",command=pegar_informacoes,width=30)
my_button_guardar.grid(column=1,row=4)

# funçao para pegar as informaçoes



# funçao para validar se ja nao existem tais informaçoes

window.mainloop()