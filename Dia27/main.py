from tkinter import *


window = Tk()

#cria a tela mas como nao tem nenhum comando, a tela é fechada
#entao é necessario um loop para que se mantenha a tela aberta
# para isso suamos o codigo abaixo

window.title('Dia27')
# cria um titulo para a janela

window.minsize(width=500, height=300)
# define o tamanho da janela

window.config(padx=100, pady=200)

#Label

my_label = Label(text='Sou uma label', font=('Arial', 15, "bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "New text"
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=2,row=0)


input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


window.mainloop()