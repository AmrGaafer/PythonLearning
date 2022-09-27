# -------------------------------------------------------------------------------------------------------------
# Decorators (Meta programming):
#   Higher order function (Function that accepts another function as a parameter)
#   - wrap other functions and enhance their behaviour (take a function argument and returns it with added functionality)
#   Syntax: Sugar Syntax Method:
#           @Decorator_function
#           def function_ToBeDocarated():...
#
# NOTE: Everything in Python is an object, even functions
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

def myDecorator(fn):    # Decorator accepts fn()
    def nested_fn():
        print('before')
        fn()
        print('after')
    return nested_fn     # returns nested_fn

def SayHello():
    print('Hello from function!')

# Intuative decoration method:
afterDecoration = myDecorator(SayHello)
afterDecoration()

# Sugar Syntax method:
@myDecorator
def SayHelloSugarSyntax():
    print('Hello from function with sugar syntax!')

SayHelloSugarSyntax()
