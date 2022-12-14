# Resources:
#   win32gui install [not implemented]:
#       https://stackoverflow.com/questions/70725054/how-to-get-the-directory-location-of-the-window-in-focus-in-python
#       https://stackoverflow.com/questions/2790825/how-can-i-maximize-a-specific-window-with-python
#       https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
#       https://stackoverflow.com/questions/2090464/python-window-activation
#   pygetwindow module explaination:
#       https://pygetwindow.readthedocs.io/en/latest/
#   mouse module:
#       https://github.com/boppreh/mouse
#       https://www.youtube.com/watch?v=W9wIiLDMiWU
#   keyboard:
#       https://github.com/boppreh/keyboard

import os
os.system('cls')        # cls command
import time

# maximize screen and focus:
# solution #1:
#import win32gui, win32com
#hwnd = pywin32_system32.GetForegroundWindow()
#pywin32_system32.ShowWindow(hwnd, win32com.SW_MAXIMIZE)

# solution #2:
#import ctypes
#
#time.sleep(5)
#user32 = ctypes.WinDLL('user32')
#SW_MAXIMISE = 3
#hWnd = user32.GetForegroundWindow()
#user32.ShowWindow(hWnd, SW_MAXIMISE)
#print('Hello world!')
#time.sleep(3)

# solution #3:
import pygetwindow
import termcolor
import pyfiglet
#print(dir(pygetwindow))
#print(pygetwindow.getAllTitles())   # get all the open windows
try:
    scope = pygetwindow.getWindowsWithTitle('Scope')[0]
    print(scope)
    scope.minimize()
    scope.maximize()
except:
    print('Press Ctrl-C to quit.')
    print(termcolor.colored(pyfiglet.figlet_format('ScopeView Projekt ist nicht offen'), color='red'))
    while True:
        continue


# move mouse and click:
import mouse

mouse.move(10, 10, absolute= True, duration= 1)
time.sleep(1)
mouse.move(1910, 10, absolute= True, duration= 1)
time.sleep(1)
mouse.move(1910, 1000, absolute= True, duration= 1)
mouse.right_click()
time.sleep(1)
mouse.move(10, 1070, absolute= True, duration= 1)
