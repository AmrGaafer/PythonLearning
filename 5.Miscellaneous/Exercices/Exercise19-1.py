# -------------------------------------------------------------------------------------------------------------
# Exercise #19-1:   Generators & Decorators
# Developer:        Amr Gaafer
# Date:             29.09.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Generators:")

def reverse_string(my_string):
    for character in my_string[::-1]:
        yield character

# Test
for c in reverse_string("Elzero"):
    print(c)
