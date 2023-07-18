import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK = "#000000"
DARKBLUE = "#164B60"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    label_text.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps +=1
    if reps in (1,3,5,7):
        count_down(WORK_MIN*60)
        label_text.config(text= "Work",bg=DARK,fg=RED)
    elif reps in (2,4,6):
        count_down(SHORT_BREAK_MIN*60)
        label_text.config(text= "REST",bg=DARK,fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        label_text.config(text= "LONG BREAK",bg=DARK,fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec =  count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="🗸"
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
#Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=DARK)
#Label
label_text = tkinter.Label(text="Timer",bg=DARK,fg=GREEN,font=("Arial",24,"bold"))
label_text.grid(row=0,column=2)
#Image
canvas = tkinter.Canvas(width=200,height=224,bg=DARK,highlightthickness=0) 
tomato_img = tkinter.PhotoImage(file="C:\\Users\\timul\\Desktop\\python\\pomodoro\\p.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,115,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=2)
#Buttons 
button_start = tkinter.Button(text="Start",command=start_timer,bg=DARKBLUE)
button_start.grid(row=3,column=1)
check = tkinter.Label(bg=DARK,fg=GREEN,font=("Arial",12,"bold"))
check.grid(row=3,column=2)
button_end = tkinter.Button(text="Reset",command=reset_timer,bg=DARKBLUE)
button_end.grid(row=3,column=3)


window.mainloop()