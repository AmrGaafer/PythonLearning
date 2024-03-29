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
#
# Entry()   creates a GUI entry element
#           - width: width
#           - borderwidth: border width
#           - fg, bg: text and background color
#   entryElement.get()                  returns the entered text in the entryElement
#   entryElement.insert(0, 'Txt')       intializes the entryElement with default text 'Txt'
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
    Label(root, text = e.get()).grid(row=5, column=0)

# creating a button widget (step#1)
myButton = Button(root, text='Click me!', padx= 50, pady= 20, command=myClick, fg= 'blue', bg= 'white')
# putting the button on the screen (step#2)
myButton.grid(row= 4, column=4)

# creating an entry widget (step#1)
e = Entry(root, width= 20, fg= 'purple', bg= 'yellow', borderwidth= 5)
# putting the entry widget on the screen (step#2)
e.grid(row= 6, column= 0)
e.insert(0, 'I expect your name :)')

# calling the GUI in loop
root.mainloop()
