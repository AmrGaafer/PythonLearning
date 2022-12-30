# --------------------------------------------------------------------------------------------------
# Exercise #21: Error Handling & Debugging
# Developer:    Amr Gaafer
# Date:         24.12.2022
# --------------------------------------------------------------------------------------------------
'''
Exercise #21 solutions
'''

import os
os.system('cls')        # cls command

print("Task#1: exceptions raise:")
NUM = input("Add Your Number ")

if len(NUM) > 1:
    raise IndexError('Only One Character Allowed')
if NUM.isalpha():
    raise Exception('Only Numbers Allowed')
if int(NUM) <=0:
    raise ValueError('Number Must Be Larger Than 0')
print('####################')
print(f'the number is {NUM}')
print('####################')

print("Task#2: try-except-else:")
LETTER = input("Add Letter From A to Z: ")

try:
    if len(LETTER)>1:
        raise IndexError
    if LETTER == LETTER.lower():
        raise Exception
except IndexError:
    print("You Must Write One Character Only")
except Exception:
    print("The Letter Not In A - Z")
else:
    print(f"You Typed {LETTER}")

print("Task#3: type hinting:")
def calculate(num1, num2) -> int:
    '''two integers sum'''
    return num1 + num2

print(calculate(20, 30))
