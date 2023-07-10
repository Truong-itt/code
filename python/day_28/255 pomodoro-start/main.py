from tkinter import *
import math
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
# --------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer")
    label_2.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+=1

    worked = WORK_MIN * 60
    break_short = SHORT_BREAK_MIN * 60
    break_long = LONG_BREAK_MIN * 60
    if reps % 8==0:
        count_down(break_long)
        label_1.config(text='Break long',fg=RED)
    elif reps % 2 ==0:
        count_down(break_short)
        label_1.config(text='Break short',fg=PINK)
    else:
        count_down(worked)
        label_1.config(text='work',fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec != 0:
        canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count_sec < 10:
        canvas.itemconfig(timer_text,text = f"{count_min}:0{count_sec}")
    if count_sec == 0:
        canvas.itemconfig(timer_text, text=f"{count_min}p")
    if (count>0):
        window.after(1000, count_down, count-1)
    else:
        start_time()
        marks = ''
        bien_lam_viec = math.floor(reps / 2)
        for i in range(bien_lam_viec):
            marks += '✔'
        label_2.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- ##
window = Tk()
window.title('Promodoro')
window.config(padx=100,pady=50,bg=YELLOW)
tomato = PhotoImage(file='tomato.png ')
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(102,129,text='00:00',fill='white',font=(FONT_NAME,30,'bold'))
canvas.grid(column=1,row=1)
#cài đặt các label cho ứng dụng
label_1 = Label(text='Timer',font=(FONT_NAME,40,'normal'),fg=GREEN,bg=YELLOW)
label_1.grid(column=1,row=0)
label_2 = Label(font=(FONT_NAME,20,'italic'),fg=GREEN,bg=YELLOW)
label_2.grid(column=1,row=3)




#button
nut =  Button(text='Start',bg='white',highlightthickness=0,command=start_time)
nut.grid(column=0,row=2)
nut_2 =  Button(text='Reset',bg='white',highlightthickness=0,command=reset_timer)

nut_2.grid(column=2,row=2)





window.mainloop()