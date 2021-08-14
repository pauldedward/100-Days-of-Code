from os import TMP_MAX
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = "0" + str(secs)
    
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global CHECK
        CHECK += "✔"
        pomodoro_label.config(text=CHECK)

def start_timer():
    global TIMER
    if TIMER is None:
        global REPS
        REPS += 1
        
        work_secs = (60 * WORK_MIN)
        short_break_secs = (60 * SHORT_BREAK_MIN)
        long_break_secs = (60 * LONG_BREAK_MIN)
        
        if REPS % 8 == 0:
            count_down(long_break_secs)
            title_label.config(text="Long Break", fg=RED)
        elif REPS % 2 == 0:
            count_down(short_break_secs)
            title_label.config(text="Short Break", fg=PINK)
        else:
            count_down(work_secs)
            title_label.config(text="Work", fg=GREEN)


def stop_timer():
    global TIMER
    window.after_cancel(TIMER)
    TIMER = None
    global REPS
    REPS = 0
    global CHECK
    CHECK = ""
    title_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    pomodoro_label.config(text=CHECK)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Day-28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(window, text="Start", font=(FONT_NAME, 14), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 14), bg=YELLOW,  highlightthickness=0, command=stop_timer)
reset_button.grid(row=2, column=2)

pomodoro_label = Label(window, font=("Courier", 20), fg=GREEN, bg=YELLOW)
pomodoro_label.grid(row=3, column=1)

window.mainloop()
