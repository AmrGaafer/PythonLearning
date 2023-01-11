# -------------------------------------------------------------------------------------------------------------
# Module: .py File that contains a set of functions
# Packages: a module that contains sub-modules. A sub-module is specified with the usual dot notation.
#   1. can be either built-in or user defined
#   2. can be imported in the application (one or multiple)
#
#   NOTE: Built-in modules and packages are saved here:
#           C:\Users\user\AppData\Local\Programs\Python\Python**\Lib
#                                                            (**) is the Python version
#         Built-in Modules list: https://docs.python.org/3/py-modindex.html
#
#   Important built-in packages:
#       csv:            very convenient for reading and writing csv files
#       collections:    useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
#       random:         generates pseudo-random numbers, shuffles sequences randomly and chooses random items
#       string:         more functions on strings.
#       re:             pattern-matching in strings via regular expressions
#       math:           some standard mathematical functions
#       os:             interacting with operating systems
#       os.path:        submodule of os for manipulating path names
#       sys:            work directly with the Python interpreter
#       json:           good for reading and writing json files (good for web work)
#
#   Syntax:
#     1. Module import:
#       import moduleName1, moduleName2         imports the whole module(s)
#       Hint #1: if the whole module is imported, the function can be called only using the dot notation (.)
#                (e.g. random.random(), functools.reduce())
#       import moduleName as moduleAlias        imports the module as an alias
#       [bad practice] from modulName import *  imports the whole module and all its functions are callable 
#                                               without the need to hint #1 above
#                                               - This might be confusing and the imported objects (e.g. functions)
#                                                 may overwrite (or even overwritten) by the developer's objects
#
#     2. Function import:
#       from moduleName import fn1, fn2,...     imports certain function(s) from the module
#       Hint #2: if certain function(s) of module is/are imported, 
#                the function can be called without using the dot notation (.)(e.g. random(), reduce())
#       from moduleName import fn1 as fnAlias   imports certain function as an alias from the module
#
#       dir(moduleName)                         returns all the available functions in that module
#                                               !! The module has to be previously imported !!
#   Install external packages:
#       1. Module is a single file, Package is group of Modules
#       2. downloadable from the internet
#       3. Python Package Manager PIP is the tool to install Packages and their dependencies
#       pip documentation: https://pip.pypa.io/en/stable/
#       External Packages list: https://pypi.org/
#       NOTE: requirements.txt: list of projects dependencies in one file, each line is PackageName==VersionNumber
#             VersionNumber is technically optional
#             Example:
#               beutifulsoup4==4.5.1
#               bs4==0.0.1
#
#   Important external packages:
#       IPython:        better interactive Python interpreter
#       requests:       Provides easy to use methods to make web requests. Useful for accessing web APIs.
#       Flask:          lightweight framework for making web applications and APIs.
#       Django:         more featureful framework for making web applications. Django is particularly good for designing complex, 
#                       content heavy, web applications.
#       Beautiful Soup: used to parse HTML and extract information from it. Great for web scraping.
#       pytest:         extends Python's builtin assertions and unittest module.
#       PyYAML:         for reading and writing YAML files.
#       NumPy:          fundamental package for scientific computing with Python. 
#                       It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
#       pandas:         library containing high-performance, data structures and data analysis tools. 
#                       In particular, pandas provides dataframes!
#       matplotlib:     2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
#       ggplot:         another 2D plotting library, based on R's ggplot2 library.
#       Pillow:         Python Imaging Library adds image processing capabilities to your Python interpreter.
#       pyglet:         cross-platform application framework intended for game development.
#       Pygame:         set of Python modules designed for writing games.
#       pytz:           World Timezone Definitions for Python
#
#   Syntax (on Terminal):
#       pip --version                           returns the version of the installed pip
#       pip install pip --upgrade pip           upgrades pip
#       pip list                                returns a list of all installed pip
#       pip install PackageName                 installs the given Package(s)
#       pip uninstall PackageName               uninstalls the given Package(s)
#       pip install PackageName==x.x.x          installs the given Package version x.x.x
#       pip install PackageName>=x.x.x          installs the given Package version x.x.x or newer
#       pip install -r requirements.txt         installs the project dependencies all at once
# -------------------------------------------------------------------------------------------------------------

import os
import sys
import random, functools    # built-in modules    
import MyModule             # user-defined module
import termcolor            # exernal module - (on Terminal) pip install termcolor
import pyfiglet             # exernal module - (on Terminal) pip install pyfiglet
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Built-in Modules:\n')
print(f'print a random number {random.random()}')
print(f'try a second module {functools.reduce(lambda a, b: a+b, [1 , 2, 3])}')

from random import randint
print(f'print a random integer number {randint(-10,100)}')

print(f'\nprint random module content:\n\r{dir(random)}')

import abc
print(f'\nprint abc module content:\n\r{dir(abc)}')

print('\n# ********************************************* #')
print('User-defined Modules:\n')
print(sys.path)
print(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))    # NOTE: one time call
#print(sys.path)
print(dir(MyModule))
MyModule.sayHello('Amr')
MyModule.sayHowAreYou('Amr')

print('\n# ********************************************* #')
print('Import External Modules:\n')
print(termcolor.colored(pyfiglet.figlet_format('Amr'), color='magenta'))
