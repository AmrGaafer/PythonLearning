# Resources:
#   win32gui install [not implemented]:
#       https://stackoverflow.com/questions/2790825/how-can-i-maximize-a-specific-window-with-python
#   pygetwindow module explaination:
#       https://pygetwindow.readthedocs.io/en/latest/
#   mouse module:
#       https://github.com/boppreh/mouse
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
#print(dir(pygetwindow))
print(pygetwindow.getAllTitles())   # get all the open windows
scope = pygetwindow.getWindowsWithTitle('ScopeTest')[0]
print(scope)
scope.minimize()
scope.maximize()


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
