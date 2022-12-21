# -------------------------------------------------------------------------------------------------------------
# Exercise #5:  Tuples & Methods
# Developer:    Amr Gaafer
# Date          21.12.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: tuple creation:")
name = 'Amr',
print(type(name))

print("Task#2: tuple manipulation:")
friends = ("Osama", "Ahmed", "Sayed")

friends = list(friends)
friends[0] = 'Elzero'
friends = tuple(friends)
print(friends)
print(type(friends))
print(len(friends))

print("Task#3: tuple concatenate:")
nums = (1, 2, 3)
letters = ("A", "B", "C")

my_tuple = nums + letters
print(my_tuple)
print(len(my_tuple))

print("Task#4: tuple destruction:")
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)
