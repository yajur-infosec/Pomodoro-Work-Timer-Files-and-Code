from tkinter import *
import math
from typing import Final

# ------------- CONSTANTS ----------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#85f4ff"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT = "Courier"
WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
reps = 0
timer = None

# TIMER RESET MECHANISM

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# TIMER MECHANISM

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_TIME * 60
    short_break_sec = SHORT_BREAK_TIME * 60
    long_break_sec = LONG_BREAK_TIME * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title.config(text="Long Break", fg=RED)
    if reps % 2 == 0:
        countdown(short_break_sec)
        title.config(text="Short Break", fg=PINK)
    else:
        title.config(text="Work", fg=BLACK)
        countdown(work_sec)

# COUNtDOWN MECHANISM

def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# UI SETUP


window = Tk()
window.title("Pomodoro Work Timer")
window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=BLUE)

title = Label(text="Timer", fg=BLACK, bg=BLUE, font=(FONT, 35, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

button1 = Button(text="Reset", command=reset_timer)
button1.grid(column=2, row=2)

check_marks = Label(fg=YELLOW, bg=BLUE, font=(FONT, 20, "normal"))
check_marks.grid(column=1, row=3)

window.mainloop()

window.mainloop
