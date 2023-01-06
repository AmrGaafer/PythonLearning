# -------------------------------------------------------------------------------------------------------------
# Decorators (Meta programming):
#   Higher order function (Function that accepts another function as a parameter)
#   - wrap other functions and enhance their behaviour (take a function argument and returns it with added functionality)
#   Syntax:
#           def function_DecoratingFunction():...
#               def function_nested(...):          # has to have the same blueprint of nested function
#                   ...
#                   function_ToBeDocarated(...)
#                   ...
#               return function_nested
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
        fn()            # wrapped function execution
        print('after')
    return nested_fn    # returns nested_fn

def SayHello():
    print('Hello from function!')

# Intuative decoration method:
afterDecoration = myDecorator(SayHello)
afterDecoration()
print('-----------------------')

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
        print('before_2')
        fn(n1, n2)          # has to have matching blueprint to to wrapped function
        print('after_2')
    return nested_fn

@myDecorator        # outter decorator
@myDecorator2       # inner decorator
def calculate(n1, n2):
    print(n1 + n2)

calculate(1, 2)
print('-----------------------')
calculate(-1, 2)

print('-----------------------'*2)
@myDecorator2
@myDecorator
def calculate(n1, n2):
    print(n1 + n2)

calculate(1, 2)
print('-----------------------')
calculate(-1, 2)

print('\n# ********************************************* #')
print('Example (Execution time):')
from time import time

def executionTime(fn):
    def wrapper(i):
        start = time()
        fn(i)
        end = time()
        print(f'The function execution time is {end - start} sec')
    return wrapper

@executionTime
def rangePrinter(i):
    for n in range(0, i+1):
        print(n)

rangePrinter(10000)
