# -------------------------------------------------------------------------------------------------------------
# Exercise #19-2:   Generators & Decorators
# Developer:        Amr Gaafer
# Date:             29.09.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#2: Decorators:")

def myDecorator(fn):
    def nested_fn():
        print('Sugar Added From Decorators')
        fn()
        print('#'*20)
    return nested_fn

# Test
@myDecorator
def make_tea():
    print("Tea Created")

@myDecorator
def make_coffe():
    print("Coffe Created")

make_tea()
make_coffe()
