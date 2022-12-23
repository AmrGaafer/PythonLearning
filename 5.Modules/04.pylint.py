# --------------------------------------------------------------------------------------------------
# pylint Module: code evaluation module to check if the code is satisfying the coding guidlines
#   Testing on terminal:
#       pylint.exe file_directory to be evaluated
# --------------------------------------------------------------------------------------------------
'''This is my test module'''

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('pylint module:\n')

def say_hello(name):
    '''This is my test function'''
    msg = 'Hi'
    return msg + ' ' + name.strip().capitalize() + '!'

print(say_hello('  AmR'))
