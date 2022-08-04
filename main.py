import tkinter as t

#############################  CONSTANTS  #############################
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2B7A0B"
YELLOW = "#F5F0BB"
FONT_NAME = "Times New Roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#############################  Global Variables  #######################
lap = 0
check_text = '✔'
timer = None

#############################  TIMER RESET  ############################# 
def reset_timer():
    global check_text, lap, timer
    # Cancel/Stop timer countdown.
    if(timer != None):
        window.after_cancel(timer)
        # Reset values being displayed.
        l_session.config(text='Idle')
        tomato.itemconfig(timer_text, text='00:00')
        l_check.config(text='')
        check_text = '✔'
        lap = 0
        timer = None


#############################  TIMER MECHANISM  #############################

def start_timer():
    global lap
    lap += 1
    if(lap%8 == 0):
        countdown(LONG_BREAK_MIN*60)
        l_session.config(text='Long Break')
    elif(lap%2 == 0):
        countdown(SHORT_BREAK_MIN*60)
        l_session.config(text='Short Break')
    else:
        countdown(WORK_MIN*60)
        l_session.config(text='Work')

#############################  COUNTDOWN MECHANISM  ############################# 
def countdown(count):
    global lap, check_text
    if(count > 0):
        global timer
        # print(count)
        tomato.itemconfig(timer_text, text="0"*(2 - len(str(count//60))) + str(count//60) + ":" + "0"*(2 - len(str(count%60))) + str(count%60))
        timer = window.after(1000, countdown, count-1)
    # To maintain looping between timers when count reaches 00:00,
    # and checking if work is completed.
    elif(count == 0):
        tomato.itemconfig(timer_text, text="00:00")
        l_check.config(text=check_text*((lap + 1)//2))
        start_timer()


#############################  UI SETUP  #############################
window = t.Tk()
window.title('PomoDoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

#########  Example Code  ##########
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

# Label for session.
l_session = t.Label(text='Idle', font=(FONT_NAME, 30, 'italic'), fg=GREEN, bg=YELLOW)
l_session.grid(column=2, row=4)


# Label for checkmark (To count number of work sessions completed).
l_check = t.Label(text='', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
l_check.grid(column=2, row=5)

# Buttons for start and reset.
b_start = t.Button(text='Start', highlightthickness=0, command=start_timer)
b_reset = t.Button(text='Reset', highlightthickness=0, command=reset_timer)
b_start.config(width=10)
b_reset.config(width=10)
b_start.grid(column=1, row=3)
b_reset.grid(column=3, row=3)

# Keep the window displayed.
window.mainloop()

# TODO: Fix issue of multiple clicks of start button, gives glitch on countdown timer.
#       use a variable (1/-1) to keep state if start pressed once already, disable it accordingly.
