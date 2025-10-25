#Fazer uma interface que faça a conversao de Mile para Km
#Fazer igual na foto que esta na pasta do dia 27


from tkinter import *

window = Tk()
window.title('Mile to km Converter')
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)



my_label = Label(text='is equal to', font=('Arial', 15, "bold"))
my_label.grid(column=0,row=1)

input = Entry(width=10)
input.grid(column=1,row=0,padx=20)

my_label_km = Label(text="0", font=('Arial', 15, "bold"))
my_label_km.grid(column=1,row=1,padx=20)

my_label_km_holder = Label(text="Km", font=('Arial', 15, "bold"))
my_label_km_holder.grid(column=2,row=1)

my_label_Miles = Label(text="Miles", font=('Arial', 15, "bold"))
my_label_Miles.grid(column=2,row=0)

def calcular():
    miles = int(input.get())
    km = miles * 1.60934
    my_label_km["text"] = km

my_button_calculate = Button(text="Calculate", command=calcular)
my_button_calculate.grid(column=1,row=2,padx=20)

window.mainloop()