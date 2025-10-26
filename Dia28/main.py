from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def Resetar():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label_timer.config(text="Timer")
    my_label_checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
from datetime import time
SHORT_BREAK_REPS = [1,3,5,7]
LONG_BREAK_REPS = [2,4,6]
def Comecar():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in SHORT_BREAK_REPS:
        count_down(short_break_sec)
        my_label_timer.config(text="Break", fg=PINK)
    elif reps in LONG_BREAK_REPS:
        count_down(long_break_sec)
        my_label_timer.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        my_label_timer.config(text="Work", fg=GREEN)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    # como eu fiz
    #if count_sec == 0:
        #count_sec = "00"
    #elif count_sec < 10:
        #count_sec = "0"+str(count_sec)
    # como a professora fez
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        Comecar()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        my_label_checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro App")
# cria um titulo para a janela
window.config(padx=100, pady=50, bg=YELLOW)



my_label_timer = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50, "bold") )
my_label_timer.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


my_button_start = Button(text="Start",command=Comecar)
my_button_start.grid(column=0,row=2,sticky="n")

my_button_reset = Button(text="Reset", command=Resetar)
my_button_reset.grid(column=2,row=2,sticky="w")

my_label_checkmark = Label(text="", fg=GREEN, bg=YELLOW)
my_label_checkmark.grid(column=1,row=3)
window.mainloop()