# -------------------------------------------------------------------------------------------------------------
# TKinter:
#   The concept is to have a GUI environment and create widgets within that environment
#
# TK()      returns a GUI environment   (creating a GUI)
#
# Label()   creates a GUI label element (creating a GUI element)
#   labelElement.pack()                 packs that element on the GUI
#   labelElement.grid(row= , column=)   puts that element on the GUI at the given grid positions
#                                       (The zero position is the upper left position,
#                                       the given positions are relative)
#   NOTE: The two previous methods could not be called on the same GUI environment
#
# Button()  creates a GUI button element
#           - padx, pady: width and height
#           - command: the funciton to be called on click (name is given without paranthesis)
#           - fg, bg: text and background color
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

from tkinter import *

# creating a GUI object
root = Tk()

# creating a label widget (step#1)
myLabell = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = 'My name is Amr')
myLabel3 = Label(root, text = 'I love Python')

# putting the label on the screen (step#2)
myLabell.grid(row= 0, column=0)
myLabel2.grid(row= 1, column=1)
myLabel3.grid(row= 2, column=0)


def myClick():
    myLabel = Label(root, text = 'Horraaaa!').grid(row=5, column=0)

# creating a button widget (step#1)
myButton = Button(root, text='Click me!', padx= 50, pady= 50, command=myClick, fg= 'blue', bg= 'white')
# putting the button on the screen (step#2)
myButton.grid(row= 4, column=4)

root.mainloop()
