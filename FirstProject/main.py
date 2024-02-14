# importando tkinter
from tkinter import *
from tkinter import ttk

#colors
color1 = "#3b3b3b" # black
color2 = "#feffff" # white
color3 = "#38576b" # blue
color4 = "#ECEFF1" # gray
color5 = '#FFAB40' # orange



janela =Tk()
janela.title("Calculator")
janela.geometry("235x310")
janela.config(bg=color1)

#Create frames
frame_tela = Frame(janela,width=235, height=50,bg=color3)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela,width=235, height=260)
frame_corpo.grid(row=1,column=0)

# all_values variable

all_values = ''

# create function
def enter_values(event):

    global all_values

    all_values = all_values + str(event)
    
    #screen
    value_text.set(all_values)

#function for calculator
def calc():
    global all_values
    
    result = eval(all_values)
    value_text.set(str(result))

#function to clean screen
def clean_screen():
    global all_values
    all_values = ''
    value_text.set("")


# create Label
value_text = StringVar()

app_label = Label(frame_tela, textvariable= value_text, width=16, height=2,padx=7,relief=FLAT, anchor="e",justify=RIGHT,font=('Ivy 18'),bg=color3,fg=color2)
app_label.place(x=0,y=0)

# create Buttons
b_1 = Button(frame_corpo, command= lambda: clean_screen() ,text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo, command= lambda: enter_values('%'),text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_2.place(x=119, y=0) 
b_3 = Button(frame_corpo, command= lambda: enter_values('/'),text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_3.place(x=178, y=0) 

b_4 = Button(frame_corpo, command= lambda: enter_values('7'),text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_4.place(x=1, y=52)
b_5 = Button(frame_corpo, command= lambda: enter_values('8'),text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command= lambda: enter_values('9'),text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_6.place(x=119, y=52)
b_7 = Button(frame_corpo, command= lambda: enter_values('*'),text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_7.place(x=178, y=52)

b_8 = Button(frame_corpo, command= lambda: enter_values('4'),text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_8.place(x=1, y=104)
b_9 = Button(frame_corpo, command= lambda: enter_values('5'),text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, command= lambda: enter_values('6'),text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_10.place(x=119, y=104)
b_11 = Button(frame_corpo, command= lambda: enter_values('-'),text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_11.place(x=178, y=104)

b_12 = Button(frame_corpo, command= lambda: enter_values('1'),text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_12.place(x=1, y=156)
b_13 = Button(frame_corpo, command= lambda: enter_values('2'),text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, command= lambda: enter_values('3'),text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_14.place(x=119, y=156)
b_15 = Button(frame_corpo, command= lambda: enter_values('+'),text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_15.place(x=178, y=156)

b_16 = Button(frame_corpo, command= lambda: enter_values('0'),text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_16.place(x=0,y=208)
b_17 = Button(frame_corpo, command= lambda: enter_values('.'),text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_17.place(x=119, y=208) 
b_18 = Button(frame_corpo, command= lambda: calc(), text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_18.place(x=178, y=208) 

janela.mainloop()