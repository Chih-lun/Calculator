from tkinter import *
import math

ENTER = '0'
CALCULATE = ''
RESULT = 0

def clear():
    global ENTER
    global CALCULATE
    global RESULT
    ENTER = '0'
    CALCULATE = ''
    RESULT = 0
    screen['text'] = ENTER

def equal():
    global ENTER
    global CALCULATE
    global RESULT
    try:
        RESULT = eval(CALCULATE + ENTER)
        CALCULATE = str(RESULT)
    except:
        pass
    if math.modf(RESULT)[0] == 0.0:
        RESULT = int(RESULT)
    ENTER = '0'
    screen['text'] = RESULT

def plus():
    global ENTER
    global CALCULATE
    global RESULT
    try:
        CALCULATE = CALCULATE + ENTER
        RESULT = eval(CALCULATE)
        CALCULATE = str(RESULT)
    except:
        pass
    ENTER = '0'
    CALCULATE = CALCULATE + '+'
    screen['text'] = RESULT


def substract():
    global ENTER
    global CALCULATE
    global RESULT
    try:
        CALCULATE = CALCULATE + ENTER
        RESULT = eval(CALCULATE)
        CALCULATE = str(RESULT)
    except:
        pass
    ENTER = '0'
    CALCULATE = CALCULATE + '-'
    screen['text'] = RESULT

def multiple():
    global ENTER
    global CALCULATE
    global RESULT
    try:
        CALCULATE = CALCULATE + ENTER
        RESULT = eval(CALCULATE)
        CALCULATE = str(RESULT)
    except:
        pass
    ENTER = '0'
    CALCULATE = CALCULATE + '*'
    screen['text'] = RESULT


def divide():
    global ENTER
    global CALCULATE
    global RESULT
    try:
        CALCULATE = CALCULATE + ENTER
        RESULT = eval(CALCULATE)
        CALCULATE = str(RESULT)
    except:
        pass
    ENTER = '0'
    CALCULATE = CALCULATE + '/'
    screen['text'] = RESULT


def add_dot():
    global ENTER
    global DOT
    if '.' in ENTER:
        pass
    else:
        ENTER = ENTER + '.'
        screen['text'] = ENTER

def add_zero():
    global ENTER
    if ENTER == '0':
        pass
    else:
        ENTER = ENTER + '0'
    screen['text'] = ENTER

def add_one():
    global ENTER
    if ENTER == '0':
        ENTER = '1'
    else:
        ENTER = ENTER + '1'
    screen['text'] = ENTER

def add_two():
    global ENTER
    if ENTER == '0':
        ENTER = '2'
    else:
        ENTER = ENTER + '2'
    screen['text'] = ENTER

def add_three():
    global ENTER
    if ENTER == '0':
        ENTER = '3'
    else:
        ENTER = ENTER + '3'
    screen['text'] = ENTER

def add_four():
    global ENTER
    if ENTER == '0':
        ENTER = '4'
    else:
        ENTER = ENTER + '4'
    screen['text'] = ENTER

def add_five():
    global ENTER
    if ENTER == '0':
        ENTER = '5'
    else:
        ENTER = ENTER + '5'
    screen['text'] = ENTER

def add_six():
    global ENTER
    if ENTER == '0':
        ENTER = '6'
    else:
        ENTER = ENTER + '6'
    screen['text'] = ENTER

def add_seven():
    global ENTER
    if ENTER == '0':
        ENTER = '7'
    else:
        ENTER = ENTER + '7'
    screen['text'] = ENTER

def add_eight():
    global ENTER
    if ENTER == '0':
        ENTER = '8'
    else:
        ENTER = ENTER + '8'
    screen['text'] = ENTER

def add_nine():
    global ENTER
    if ENTER == '0':
        ENTER = '9'
    else:
        ENTER = ENTER + '9'
    screen['text'] = ENTER

window = Tk()
window.config(padx=25,pady=25)

screen = Label(text=0,bg='black',fg='white',width=24,height=3,anchor='w')
screen.grid(column=0,row=0,columnspan=4)

c_button = Button(text='C',bg='white',fg='black',width=17,command=clear)
c_button.grid(column=0,row=1,columnspan=3)
plus_button = Button(text='+',bg='white',fg='black',width=5,command=plus)
plus_button.grid(column=3,row=1)
subtract_button = Button(text='-',bg='white',fg='black',width=5,command=substract)
subtract_button.grid(column=3,row=2)
multiply_button = Button(text='×',bg='white',fg='black',width=5,command=multiple)
multiply_button.grid(column=3,row=3)
divide_button = Button(text='÷',bg='white',fg='black',width=5,command=divide)
divide_button.grid(column=3,row=4)
equal_button = Button(text='=',bg='white',fg='black',width=5,command=equal)
equal_button.grid(column=3,row=5)
dot_button = Button(text='.',bg='white',fg='black',width=5,command=add_dot)
dot_button.grid(column=2,row=5)
one_button = Button(text='1',bg='white',fg='black',width=5,command=add_one)
one_button.grid(column=0,row=4)
two_button = Button(text='2',bg='white',fg='black',width=5,command=add_two)
two_button.grid(column=1,row=4)
three_button = Button(text='3',bg='white',fg='black',width=5,command=add_three)
three_button.grid(column=2,row=4)
four_button = Button(text='4',bg='white',fg='black',width=5,command=add_four)
four_button.grid(column=0,row=3)
five_button = Button(text='5',bg='white',fg='black',width=5,command=add_five)
five_button.grid(column=1,row=3)
six_button = Button(text='6',bg='white',fg='black',width=5,command=add_six)
six_button.grid(column=2,row=3)
seven_button = Button(text='7',bg='white',fg='black',width=5,command=add_seven)
seven_button.grid(column=0,row=2)
eight_button = Button(text='8',bg='white',fg='black',width=5,command=add_eight)
eight_button.grid(column=1,row=2)
nine_button = Button(text='9',bg='white',fg='black',width=5,command=add_nine)
nine_button.grid(column=2,row=2)
zero_button = Button(text='0',bg='white',fg='black',width=11,command=add_zero)
zero_button.grid(column=0,row=5,columnspan=2)

window.mainloop()