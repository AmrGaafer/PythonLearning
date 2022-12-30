from cgitb import text
import os
os.system('cls')        # cls command

varLatch = 0
varTemp = 0

def latch(n):
    global varLatch
    global varTemp
    if str(n) in '0123456789':
        myEntry.insert(0, n)
    elif n == 'c':
        myEntry.delete(0, END)
    elif n == '+':
        varLatch = varTemp + varLatch
    elif n == '=':
        varLatch = varLatch + varTemp

from tkinter import *

root = Tk()
root.title("My Calculator")

buttonWidth = 40
buttonHeight = 20

myEntry = Entry(root, width = buttonWidth, bg= 'white', fg= 'black')
myEntry.grid(row= 0, column=0, columnspan=3)

myButton7 = Button(root, text='7', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(7))
myButton7.grid(row= 1, column=0)

myButton8 = Button(root, text='8', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(8))
myButton8.grid(row= 1, column=1)

myButton9 = Button(root, text='9', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(9))
myButton9.grid(row= 1, column=2)

myButton4 = Button(root, text='4', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(4))
myButton4.grid(row= 2, column=0)

myButton5 = Button(root, text='5', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(5))
myButton5.grid(row= 2, column=1)

myButton6 = Button(root, text='6', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(6))
myButton6.grid(row= 2, column=2)

myButton1 = Button(root, text='1', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(1))
myButton1.grid(row= 3, column=0)

myButton2 = Button(root, text='2', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(2))
myButton2.grid(row= 3, column=1)

myButton3 = Button(root, text='3', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(3))
myButton3.grid(row= 3, column=2)

myButton0 = Button(root, text='0', padx= buttonWidth, pady= buttonHeight, command=lambda: latch(0))
myButton0.grid(row= 4, column=0)

myButtonClear = Button(root, text='Clear', padx= buttonWidth*2-3, pady= buttonHeight, command= lambda: latch('c'))
myButtonClear.grid(row= 4, column=1, columnspan=2)

myButtonPlus = Button(root, text='+', padx= buttonWidth-1, pady= buttonHeight, command= lambda: latch('+'))
myButtonPlus.grid(row= 5, column=0)

myButtonEqual = Button(root, text='=', padx= buttonWidth*2+6, pady= buttonHeight, command= lambda: latch('='))
myButtonEqual.grid(row= 5, column=1, columnspan=2)

root.mainloop()
