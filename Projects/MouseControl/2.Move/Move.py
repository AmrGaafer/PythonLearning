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
import mouse
import termcolor
import pyfiglet
#print(dir(pygetwindow))
#print(pygetwindow.getAllTitles())   # get all the open windows
try:
    scope = pygetwindow.getWindowsWithTitle('Scope')[0]
    #print(scope)
    scope.minimize()
    scope.maximize()
    
    # move mouse and click
    
    xMin, xMax = 10, 1910
    yMin, yMax = 10, 1070

    xCollabseAll, yCollabseAll = 165, 145
    xExpand, yExpand = 20, 210
    xProject, yProject = 110, 230
    xStartRecord, yStartRecord = 1305, 65

    # dummy mouse motion 
    mouse.move(xMin, yMin, absolute= True, duration= 1)
    mouse.move(xMax, yMin, absolute= True, duration= 1)
    mouse.move(xMax, yMax, absolute= True, duration= 1)
    mouse.move(xMin, yMax, absolute= True, duration= 1)

    # scope project recort start
    mouse.move(xCollabseAll, yCollabseAll, absolute= True, duration= 1)
    mouse.click()
    mouse.move(xExpand, yExpand, absolute= True, duration= 1)
    mouse.click()
    mouse.move(xProject, yProject, absolute= True, duration= 1)
    mouse.click()
    time.sleep(2)
    mouse.move(xStartRecord, yStartRecord, absolute= True, duration= 1)
    mouse.click()
    time.sleep(5)
    scope.minimize()
    
except:
    print('zum Beenden Strg-C drücken.')
    print(termcolor.colored(pyfiglet.figlet_format('ScopeView Projekt ist nicht offen'), color='red'))
    time.sleep(10)
    #while True:
    #    time.sleep(2)
    #    continue
