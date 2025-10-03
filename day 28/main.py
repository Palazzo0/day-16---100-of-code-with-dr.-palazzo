from idlelib.debugger_r import gui_adap_oid
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
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canva_text, text= "00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
       count_down(long_break_sec)
       timer_label.config(text="Long Break", font=(FONT_NAME, 35, "bold"),  fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", font=(FONT_NAME, 35, "bold"), fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", font=(FONT_NAME, 35, "bold"), fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canva_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Palazzo's pomodoro App")
window.config(padx=100, pady=50, bg= YELLOW)


#display my image and create text on image
canvas = Canvas(width=200, height=223, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image= tomato_img)
canva_text = canvas.create_text(103, 130, fill="white", text="00:00", font=(FONT_NAME, 45, "bold"))
canvas.grid(column=1, row=1)

#create the timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW,  fg=GREEN)
timer_label.grid(column=1, row=0)


#create the start and reset buttons
start = Button(text="Start", command=start_timer)
reset = Button(text="Reset", command=reset_timer)

start.grid(column=0, row=2)
reset.grid(column=2, row=2)

#create the check mark
check_mark = Label( font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)













window.mainloop()