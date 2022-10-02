# -------------------------------------------------------------------------------------------------------------
# Built-in Functions:
#  Numeric Functions:
#   sum(iterable, start)    returns the sum of the elements, (optionally) summation start can be provided
#   round(float, accuracy)  returns the round (integer) of a float with (optionally) certain accuracy (float)
#   abs(number)             returns the distance between the number and zero
#   pow(base, exp, mod)     returns the base^exp and (optionally) the modulus
#   min(iterator or items)  returns the minimum value element (numerical or strings)
#   max(iterator or items)  returns the maximum value element (numerical or strings)
#   bin(integer)            returns the binary value of the argument
#   range(start, end, step) returns a <class 'range'> with (optionally) start other than 0
#                                                      and (optionally) certain step
#                               - the range doesn't include the end
#                               - the range can be unpacked by the asterisk operator *
#
#  Boolean Functions:
#   all(iterable)           returns True if all the iterable arguments (string, list, tuple or dictionary) are True
#   any(iterable)           returns True if any of the iterable arguments (string, list, tuple or dictionary) is True
#
#  String Functions:
#   print(string)           prints the given string on the console
#                               - the seperator is by default " " and can be modified
#                               - the line end is by default "\n" and can be modified
#
#  General Purpose Functions:
#   slice(start, end, step) returns sliced version of that variable (end is mandatory)
#   enumerate(iterable, start)
#                           returns enumarated version of the iterable with (optionally) given start counter
#   reversed(iterable)      returns a reversed version of the iterable (e.g. string or list)
#   id(variable)            returns the memory id of that variable
#   help()                  returns a help manual for the given text
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Numeric Functions')
print('sum():')
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 12))
print(sum([1, 2, 3], -12))
print('# --------------------------------------------- #')

print('round():')
print(round(1.99))
print(round(1.99, 1))
print('# --------------------------------------------- #')

print('abs():')
print(abs(1.99))
print(abs(3+4j))
print('# --------------------------------------------- #')

print('pow():')
print(pow(1.99,2))
print(pow(3+4j, 5))
print(pow(3, 5))
print(pow(3, 5, 10))
print('# --------------------------------------------- #')

print('min():')
print(min((37, 6, 7, 100)))
print(min(['A', 'a', 'Amor']))
print('# --------------------------------------------- #')

print('max():')
print(max((37, 6, 7, 100)))
print(max(['A', 'a', 'Amor']))
print('# --------------------------------------------- #')

print('bin():')
num = 65535
print(bin(num))
print('# --------------------------------------------- #')

print('range():')
print(type(range(4)))
print(range(4))
print(*range(4))
myList = [*range(0)]
print(myList)
myList = [*range(10)]
print(myList)
myList = [*range(0, 20, 2)]
print(myList)
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('Boolean Functions')
print('all():')
name = "Amr"
print(all(name))

list = [True, True, True]
print(all(list))
list = [True, True, False]
print(all(list))            # False

list = [1 , 2, 3]
print(all(list))
list = [1 , 2, []]
print(all(list))            # False

list = [1, 2, 3]
print(all(list))
list = [1, 0, 3]
print(all(list))            # False

set = {1, 2, 3}
print(all(set))
set = {1, 0, 3}
print(all(set))             # False

dict = {5 : "Apple", 1 : "Orange"}
print(all(dict))
dict = {0 : "Apple", 1 : "Orange"}
print(all(dict))            # False
print('# --------------------------------------------- #')

print('any():')
list = [1 , 2, 3]
print(any(list))
list = [1 , 2, []]
print(any(list))            # False
list = [0]
print(any(list))            # False
set = {0}
print(any(set))             # False
dict = {0 : "Apple"}
print(all(dict))            # False
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('String Functions')
print('print():')
print("Amr", "Awad")                    # Default seperator is space
print("Amr", "Awad", sep = " @ ")       # Seperator can be modified
print("First line")                     # Default line ending is "\n"
print("Second line", end = " ")         # Line ending can be modified
print("Third line")
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('General Purpose Functions')
print('slice():')
myString = '0123456789'
print(myString[5:8])
print(myString[:8])                     # till a given end
print(myString[5:])                     # starting from a given start
print(myString[slice(5)])               # end is mandatory
print(myString[slice(5,8)])
print('# --------------------------------------------- #')

print('enumerate():')
mySkills = ["C++", "Python", "PLC"]
mySkillsEnum = enumerate(mySkills, 1)
print(mySkillsEnum)
for mySkill in mySkillsEnum:
    print(mySkill)
for count,skill in mySkillsEnum:
    print(count, skill)
print('# --------------------------------------------- #')

print('reversed():')
name = "Amr"
print(reversed(name))
for char in reversed(name):
    print(char)
names = ["Adam", "Amr", "Gaafer"]
print(reversed(names))
for name in reversed(names):
    print(name)
print('# --------------------------------------------- #')

print('id():')
num = 12
print(id(12))
print(id(num))
num = 14
print(id(12))
print(id(num))              # id changes here as the value changed
print('# --------------------------------------------- #')

print('help():')
help("len")
print('# --------------------------------------------- #')
