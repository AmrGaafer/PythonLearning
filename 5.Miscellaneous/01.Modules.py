# -------------------------------------------------------------------------------------------------------------
# Module: .py File that contains a set of functions
#   1. can be either built-in or user defined
#   2. can be imported in the application (one or multiple)
#
#   NOTE: Built-in modules are saved here:
#           C:\Users\user\AppData\Local\Programs\Python\Python39\Lib
#   Syntax:
#     1. Module import:
#       import moduleName1, moduleName2         imports the whole module(s)
#       Hint #1: if the whole module is imported, the function can be called only using the resolution operator (.)
#                (e.g. random.random(), functools.reduce())
#       import moduleName as moduleAlias        imports the module as an alias
#       Built-in Modules list: https://docs.python.org/3/py-modindex.html
#
#     2. Function import:
#       from moduleName import fn1, fn2,...     imports certain function(s) from the module
#       Hint #2: if certain function(s) of module is/are imported, 
#                the function can be called without using the resolution operator (.)(e.g. random(), reduce())
#       from moduleName import fn1 as fnAlias   imports certain function as an alias from the module
#
#       dir(moduleName)                         returns all the available functions in that module
#                                               !! The module has to be previously imported !!
#   Install external packages:
#       1. Module is a single file, Package is group of Modules
#       2. downloadable from the internet
#       3. Python Package Manager PIP is the tool to install Packages and their dependencies
#       External Packages list: https://pypi.org/
#       pip documentation: https://pip.pypa.io/en/stable/
#   Syntax (on Terminal):
#       pip --version                           returns the version of the installed pip
#       pip list                                returns a list of all installed pip
#       pip install PackageName                 installs the given Package
#       pip install PackageName==x.x.x          installs the given Package version x.x.x
#       pip install PackageName>=x.x.x          installs the given Package version x.x.x or newer
#       pip install pip --upgrade pip           upgrades pip
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Built-in Modules:\n')
import random, functools

print(f'print a random number {random.random()}')
print(f'try a second module {functools.reduce(lambda a, b: a+b, [1 , 2, 3])}')

from random import randint
print(f'print a random integer number {randint(-10,100)}')

print(dir(random))

print('\n# ********************************************* #')
print('User-defined Modules:\n')
import sys
import os
print(sys.path)
print(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))    # NOTE: one time call
#print(sys.path)

import MyModule
print(dir(MyModule))
MyModule.sayHello('Amr')
MyModule.sayHowAreYou('Amr')

print('\n# ********************************************* #')
print('Import External Modules:\n')
import termcolor    #(on Terminal) pip install termcolor
import pyfiglet     #(on Terminal) pip install pyfiglet

print(termcolor.colored(pyfiglet.figlet_format('Amr'), color='magenta'))
