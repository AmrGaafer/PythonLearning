# -------------------------------------------------------------------------------------------------------------
# TKinter
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

from tkinter import *

root = Tk()

# creating a label widget
myLabel = Label(root, text = 'Hello World!')
# putting the label on the screen
myLabel.pack()

root.mainloop()
