
# Decidi criar uma versao sem ver os videos dela explicando como ela faz
# Copiei o que ja tinha feito no dia 29 da minha versao
# na nova versao dela, ela usa json ao inves de arquivo txt

from tkinter import *
from tkinter import messagebox
import random
import os
import json
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

my_entry_password = Entry(width=30)
my_entry_password.grid(column=1,row=3)


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
        if os.path.exists("senhas.json"):
            with open("senhas.json", "r", encoding="utf-8") as f:
                # le os dados antigos
                data = json.load(f)
                # atualiza o arquibo antigo
                data.update({site:{"user":user,"password":pwd}})

            with open("senhas.json", "w", encoding="utf-8") as f:
                # salva o arquivo
                json.dump(data,f, indent=4)
            apagar_informacoes()

        else:
            with open("senhas.json", "w", encoding="utf-8") as f:
                json.dump({site:{"user":user,"password":pwd}},f, indent=4)
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

def procurar_informaçoes():
    site = my_entry_site.get()
    if os.path.exists("senhas.json"):
        with open("senhas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if site in data:
                messagebox.showinfo(title=f"{site}", message=data[site])
            else:
                messagebox.showerror(title = "Erro", message="Nao existe")

    else:
        messagebox.showerror(title = "Erro", message="Nao tem o arquivo senhas.json")

my_button_password = Button(text="Generate Password", command=gerar_senha,width=13)
my_button_password.grid(column=2, row=3,sticky="e")


my_button_guardar = Button(text="Add",justify="center",command=pegar_informacoes,width=30)
my_button_guardar.grid(column=1,row=4)

my_button_search = Button(text="Search",command=procurar_informaçoes,width=13)
my_button_search.grid(column=2,row=1)

# funçao para pegar as informaçoes



# funçao para validar se ja nao existem tais informaçoes

window.mainloop()