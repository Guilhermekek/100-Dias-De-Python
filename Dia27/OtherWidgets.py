from tkinter import *


window = Tk()

#cria a tela mas como nao tem nenhum comando, a tela é fechada
#entao é necessario um loop para que se mantenha a tela aberta
# para isso suamos o codigo abaixo

window.title('Dia27')
# cria um titulo para a janela

window.minsize(width=500, height=300)
# define o tamanho da janela

#Label

my_label = Label(text='Sou uma label', font=('Arial', 15, "bold"))
my_label.pack()

my_label["text"] = "New text"
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button.pack()


input = Entry(width=30)
input.insert(END, string="Some text to begin with")
input.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-libe text entry")

print(text.get("1.0", END))

text.pack()

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5,command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state,command=radio_used)

radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear","Orange","Banana"]

for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()