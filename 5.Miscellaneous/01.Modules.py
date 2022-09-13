# -------------------------------------------------------------------------------------------------------------
# Modules: File that contains a set of funcitons
#   1. can be either built-in or user defined
#   2. can be imported in the application (one or multiple)
#
#   NOTE: Built-in modules are saved here:
#           C:\Users\user\AppData\Local\Programs\Python\Python39\Lib
#   Syntax:
#       import moduleName1, moduleName2         imports the whole module(s)
#       Hint: if the whole module is called, the function can be called using the resolution operator (.)
#             e.g. random.random(), functools.reduce()
#       from moduleName import fn1, fn2,...     imports certain function(s) from the module
#       dir(moduleName)                         returns all the available functions in that module
#                                               !! The module has to be previously imported !!
# -------------------------------------------------------------------------------------------------------------

import random, functools
print(f'print a random number {random.random()}')
print(f'try a second module {functools.reduce(lambda a, b: a+b, [1 , 2, 3])}')

from random import randint
print(f'print a random integer number {randint(-10,100)}')

print(dir(random))
