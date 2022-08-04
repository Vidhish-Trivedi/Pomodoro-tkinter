import tkinter as t

#############################  CONSTANTS  #############################
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#############################  TIMER RESET  ############################# 

#############################  TIMER MECHANISM  ############################# 
def start_timer():
    countdown(5*60)

#############################  COUNTDOWN MECHANISM  ############################# 
def countdown(count):
    if(count >= 0):
        # print(count)
        tomato.itemconfig(timer_text, text="0"*(2 - len(str(count//60))) + str(count//60) + ":" + "0"*(2 - len(str(count%60))) + str(count%60))
        window.after(1000, countdown, count-1)

#############################  UI SETUP  #############################
window = t.Tk()
window.title('PomoDoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

# def fun(var1, var2):
#     print(var1)
#     print(var2)
# window.after(1000*(2), fun, 'hello', 'bye')

######################################################################################
###########  Canvas component, to add images/layers  ##########
tomato = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = t.PhotoImage(file='./tomato.png')
tomato.create_image(100, 112, image=img)

# 'fill=' argument is for text color.
timer_text = tomato.create_text(100, 120, text='00:00', font=(FONT_NAME, 30, "bold"), fill='white')

# Grid --> (3 columns X 5 rows).
tomato.grid(column=2, row=2)

######################################################################################

# Label for timer.

l_timer = t.Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
l_timer.grid(column=2, row=1)

# Label for checkmark.
l_check = t.Label(text='✔', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
l_check.grid(column=2, row=4)

# Buttons for start and reset.
b_start = t.Button(text='Start', highlightthickness=0, command=start_timer)
b_reset = t.Button(text='Reset', highlightthickness=0)
b_start.config(width=10)
b_reset.config(width=10)
b_start.grid(column=1, row=3)
b_reset.grid(column=3, row=3)

# Keep the window displayed.
window.mainloop()
