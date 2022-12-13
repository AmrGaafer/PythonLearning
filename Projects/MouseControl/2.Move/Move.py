import os
os.system('cls')        # cls command

import ctypes

user32 = ctypes.WinDLL('user32')
SW_MAXIMISE = 3
hWnd = user32.GetForegroundWindow()
user32.ShowWindow(hWnd, SW_MAXIMISE)

import mouse
import time

i = 0
while i <= 2:
    mouse.move(10, 10, absolute= True, duration= 1)
    time.sleep(1)
    mouse.move(1910, 10, absolute= True, duration= 1)
    time.sleep(1)
    mouse.move(1910, 1070, absolute= True, duration= 1)
    time.sleep(1)
    mouse.move(10, 1070, absolute= True, duration= 1)
    time.sleep(1)
    i += 1