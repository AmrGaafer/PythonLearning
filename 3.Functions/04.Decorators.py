# -------------------------------------------------------------------------------------------------------------
# Decorators (Meta programming):
#   Higher order function (Function that accepts another function as a parameter)
#   - wrap other functions and enhance their behaviour (take a function argument and returns it with added functionality)
#   Syntax:
#           def function_DecoratingFunction():...
#               ...
#               function_ToBeDocarated()
#               ...
#
#   Implementation: Sugar Syntax Method:
#           @Decorator_function
#           def function():     # decorated function
#
#           - function_DecoratingFunction() has to pass the paramters needed to the wraped function
#           - function_ToBeDocarated()      has to have matching blueprint to to wrapped function
#
# NOTE: Everything in Python is an object, even functions
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Functions without parameters decoration:')
def myDecorator(fn):    # decorator accepts fn()
    def nested_fn():    # decorating function (wraper function)
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

print('\n# ********************************************* #')
print('Functions with parameters decoration:')
def myDecorator(fn):
    def nested_fn(n1, n2):  # has to pass the parameters needed to the wrapped function
        print('before')
        if n1 < 0 or n2 < 0:
            print('One or both numbers is less than zero')
        fn(n1, n2)          # has to have matching blueprint to to wrapped function
        print('after')
    return nested_fn

def myDecorator2(fn):
    def nested_fn(n1, n2):  # has to pass the parameters needed to the wrapped function
        print('Decorator2')
        fn(n1, n2)          # has to have matching blueprint to to wrapped function
    return nested_fn

@myDecorator
@myDecorator2
def calculate(n1, n2):
    print(n1 + n2)

calculate(1, 2),
print('-----------------------')
calculate(-1, 2)

print('\n# ********************************************* #')
print('Example (Speed Test):')
