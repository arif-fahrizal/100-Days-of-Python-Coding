import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break  = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

        if reps % 2:
            checkmark_label.config(text="")
        else:
            checkmark_label.config(text="✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady= 50, padx=100, bg=YELLOW)

# Background
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))

# Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))

# Button
start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
reset_btn = Button(text="Reset", command=reset, highlightthickness=0)

# Positions
timer_label.grid(row=0,column=1)
canvas.grid(row=1,column=1)
start_btn.grid(row=2,column=0)
reset_btn.grid(row=2,column=2)
checkmark_label.grid(row=3,column=1)









window.mainloop()