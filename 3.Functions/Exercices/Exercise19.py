# -------------------------------------------------------------------------------------------------------------
# Exercise #19: Generators & Decorators
# Developer:    Amr Gaafer
# Date:         29.09.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Generators:")

def reverse_string(my_string):
    for character in my_string[::-1]:
        yield character

for c in reverse_string("Elzero"):
    print(c)

print("Task#2: Decorators:")

def myDecorator(fn):
    def nested_fn():
        print('Sugar Added From Decorators')
        fn()
        print('#'*20)
    return nested_fn

@myDecorator
def make_tea():
    print("Tea Created")

@myDecorator
def make_coffe():
    print("Coffe Created")

make_tea()
make_coffe()