# -------------------------------------------------------------------------------------------------------------
# Exercise #17: Modules & Packages 
# Developer:    Amr Gaafer
# Date:         27.09.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Random Module Application:")
import random

print(f'Random Number Between 10 And 50 => {random.randrange(10, 50)}')
print(f'Random Even Number Between 2 And 10 => {random.randrange(2,10,2)}')
print(f'Random Odd Number Between 1 And 9 => {random.randrange(1,9,2)}')
print('Module Methods Content Here:', f'{dir(random)}', sep='\n')

print("Task#2: User-defined Modules:")
import my_mod
my_mod.say_hello('Amr')
my_mod.say_welcome('Amr')
print('Module Methods Content Here:', f'{dir(my_mod)}', sep='\n')

print("Task#3: Single functions import:")
from my_mod import say_welcome
say_welcome('Amr')

print("Task#4: Single functions import with alias:")
from my_mod import say_welcome as new_welcome
new_welcome('Amr')
