# -------------------------------------------------------------------------------------------------------------
# Module Test:  Dummy 
# Developer:    Amr Gaafer
# Date          01.01.2023
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('print from MyModule2')
print('this file is running from: ', __name__) #__main__

def Hello():
    print('print function from MyModule2')

if __name__ == '__main__':
    print('MyModule2 is running directly')
else:
    print('MyModule2 is NOT running directly')

