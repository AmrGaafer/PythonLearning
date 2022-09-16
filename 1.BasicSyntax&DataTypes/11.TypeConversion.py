# -------------------------------------------------------------------------------------------------------------
# Type Conversion:
# str()         converts to string
# list()        converts to list (string, set, tuple, or dictionary), needs iterable elements
# tuple()       converts to tuple (string, list, set, or dictionary), needs iterable elements
# set()         converts to set (string, list, tuple, or dictionary), needs iterable elements
# dict()        converts to dictionary (list or tuple), needs iterable and hashable elements
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Type Conversion:\n')
print('str()')
a = 10                      # int
print(str(a))
a = 10.52                   # float
print(str(a))
a = 15 + 20j                # complex
print(str(a))
a = [1, 2, 3]               # list
print(str(a))
a = (1, 2, 3)               # tuple
print(str(a))
a = {1, 2, 3}               # set
print(str(a))
a = {"a":1, "b":2, "c":3}   # dictionary
print(str(a))
print('# --------------------------------------------- #')

print('list()')
# a = 10                    # int
# print(list(a))
# a = 10.52                 # float
# print(list(a))
# a = 15 + 20j              # complex
# print(list(a))
a = "Amooor"                # string
print(list(a))
a = (1, 2, 3)               # tuple
print(list(a))
a = {1, 2, 3}               # set
print(list(a))
a = {"a":1, "b":2, "c":3}   # dictionary (only keys)
print(list(a))
print('# --------------------------------------------- #')

print('tuple()')
# a = 10                    # int -> Error
# print(tuple(a))
# a = 10.52                 # float
# print(tuple(a))
# a = 15 + 20j              # complex
# print(tuple(a))
a = "Amooor"                # string
print(tuple(a))
a = [1, 2, 3]               # list
print(tuple(a))
a = {1, 2, 3}               # set
print(tuple(a))
a = {"a":1, "b":2, "c":3}   # dictionary (only keys)
print(tuple(a))
print('# --------------------------------------------- #')

print('set()')
# a = 10                    # int
# print(set(a))
# a = 10.52                 # float
# print(set(a))
# a = 15 + 20j              # complex
# print(set(a))
a = "Amooor"                # string
print(set(a))
a = [1, 2, 3]               # list
print(set(a))
a = (1, 2, 3)               # tuple
print(set(a))
a = {"a":1, "b":2, "c":3}   # dictionary (only keys)
print(set(a))
print('# --------------------------------------------- #')

print('dict()')
# a = 10                    # int
# print(dict(a))
# a = 10.52                 # float
# print(dict(a))
# a = 15 + 20j              # complex
# print(dict(a))
# a = "Amooor"              # string
# print(dict(a))
a = [["a",1], ["b",2], ["c",3]]               # list
print(dict(a))
a = (("a",1), ("b",2), ("c",3))               # tuple
print(dict(a))
# a = {{"a",1}, {"b",2}, {"c",3}}             # set (not hashable variable)
# print(dict(a))
print('# --------------------------------------------- #')
