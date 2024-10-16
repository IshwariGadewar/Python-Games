import tkinter
import math

PATH = r'D:\PYTHON\PYTHON - Udemy\Game\POMODORA APP\tomato.png'
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
TIME = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(TIME)
    timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if REPS%8==0:
        count_down(long_break_sec)
        timer.config(text="Break",fg=RED)
    elif REPS%2==0:
        timer.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global TIME
        TIME = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if REPS%2==1:
            global marks
            marks += "✔"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("POMODORA")
window.config(padx=100,pady=50,bg=YELLOW)

#heading
timer = tkinter.Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0)
timer.grid(row=0,column=1)

#bg as tomato
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file=PATH)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


#start button
start = tkinter.Button(text="Start",width=3,height=1,highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

#checkMark
check_mark = tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
check_mark.grid(row=3,column=1)

#reset button
reset = tkinter.Button(text="Reset",width=4,height=1,highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

window.mainloop()