# Resources:
#   win32gui install [not implemented]:
#       https://stackoverflow.com/questions/70725054/how-to-get-the-directory-location-of-the-window-in-focus-in-python
#       https://stackoverflow.com/questions/2790825/how-can-i-maximize-a-specific-window-with-python
#       https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
#       https://stackoverflow.com/questions/2090464/python-window-activation
#   pygetwindow module explaination:
#       https://pygetwindow.readthedocs.io/en/latest/
#   subprocess:
#       https://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-arguments
#   mouse module:
#       https://github.com/boppreh/mouse
#       https://www.youtube.com/watch?v=W9wIiLDMiWU
#   keyboard:
#       https://github.com/boppreh/keyboard

import os, subprocess, time
os.system('cls')        # cls command

# maximize screen and focus:

# solution #1:
#import win32gui, win32com
#
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
#print(pygetwindow.getAllTitles())   # get all the open windows
try:
    print('ScopeView Project bringing to front!')
    scope = pygetwindow.getWindowsWithTitle('EOL_Scope')[0]
    print('ScopeView Project found!')
    print(scope)
    print('ScopeView Project bringing to front!')
    scope.minimize()
    scope.maximize()
except:
    print('ScopeView Project not found!')
    #os.system(r'C:/Users/Gerd1/Desktop/EOL_Scope/EOL_Scope.sln')                       # hangs execution
    #subprocess.call('C:/Users/Gerd1/Desktop/EOL_Scope/EOL_Scope.sln', shell= False)    # hangs execution
    subprocess.Popen('C:/Users/Gerd1/Desktop/EOL_Scope/EOL_Scope.sln', stdout = subprocess.PIPE, shell = True)
    #subprocess.Popen('D:/Arbeitsverzeichnis/Beckhoff/scope/Au41x_EOL_Scope_Project.sln', stdout = subprocess.PIPE, shell = True)
    print('ScopeView Project opening!')
    time.sleep(30)
    print('ScopeView Project bringing to front!')
    scope = pygetwindow.getWindowsWithTitle('EOL_Scope')[0]
    print('ScopeView Project found!')
    print(scope)
    print('ScopeView Project bringing to front!')
    scope.minimize()
    scope.maximize()

# move mouse and click
import mouse

xMin, xMax = 10, 1910
yMin, yMax = 10, 1070

xCollabseAll, yCollabseAll = 165, 145
xExpand, yExpand = 20, 210
xProject, yProject = 110, 230
xStartRecord, yStartRecord = 1305, 65

# dummy mouse motion
print('Mouse dummy motion')
mouse.move(xMin, yMin, absolute= True, duration= 1)
mouse.move(xMax, yMin, absolute= True, duration= 1)
mouse.move(xMax, yMax, absolute= True, duration= 1)
mouse.move(xMin, yMax, absolute= True, duration= 1)

# scope project recort start
print('ScopeView Project start')
mouse.move(xCollabseAll, yCollabseAll, absolute= True, duration= 1)
mouse.click()
mouse.move(xExpand, yExpand, absolute= True, duration= 1)
mouse.click()
mouse.move(xProject, yProject, absolute= True, duration= 1)
mouse.click()
time.sleep(1)
mouse.move(xStartRecord, yStartRecord, absolute= True, duration= 1)
mouse.click()
time.sleep(4)
scope.minimize()

# declare PRG_ScopeView.boScopeReady flag
#print('Declaring PRG_ScopeView.boScopeReady flag on True')
#import pyads
#
#class AdsCom():
#    #is_connected = False
#    def __init__(self):
#        adsNetID = '192.168.100.10.1.1'
#        self.plc = pyads.Connection(adsNetID, pyads.PORT_TC3PLC1)
#        # connect to plc and open connection
#        #self.plc.close()
#        self.plc.open()
#        print(self.plc.is_open)
#
#PlcCom = AdsCom()
#PlcCom.plc.write_by_name("PRG_ScopeView.boScopeReady", True, pyads.PLCTYPE_BOOL)
