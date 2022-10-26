# -------------------------------------------------------------------------------------------------------------
# Built-in Functions:
#  Numeric Functions:
#   sum(iterable, start)    returns the sum of the elements, (optionally) summation start can be provided
#   eval(expression)        returns the value of the expression given as a string (this could be class type)
#   round(float, accuracy)  returns the round (integer) of a float with (optionally) certain accuracy (float)
#   abs(number)             returns the distance between the number and zero
#   pow(base, exp, mod)     returns the base^exp and (optionally) the modulus
#   min(iterator or items)  returns the minimum value element (numerical or strings)
#   max(iterator or items)  returns the maximum value element (numerical or strings)
#   bin(integer)            returns the binary string value of the argument
#   hex(integer)            returns the hex string value of the argument
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
#   zip(list1, list2)       returns an iterator that combines multiple iterables into one sequence of tuples
#                           each tuple contains the elements in that position from all iterables
#                           - list(zip(list1, list2)) produces list of tuples (iterable)
#                           - the zipped list length is equal to the shortest input list
#   zip(*lst_of_tpl)        returns tuples from the unzipped list
#   enumerate(iterable, st) returns an ierator holds an enumarated version of the iterable
#                           with (optionally) given start (st) counter
#   slice(start, end, step) returns sliced version of that variable (end is mandatory)
#   reversed(iterable)      returns a reversed version of the iterable (e.g. string or list)
#                           correspoding to iterable[::-1]
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

print('Numeric Functions')
print('eval():')
print(eval('5*6'))
x= 24
print(eval('x/6'))
print(eval('int'))
print(eval('float'))
print(eval('str'))
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
print(list(range(4)))
print(*range(4))
print([*range(0)])
print(list(range(10)))
print(list(range(0, 20, 2)))
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('Boolean Functions')
print('all():')
name = "Amr"
print(all(name))

lst = [True, True, True]
print(all(lst))
lst = [True, True, False]
print(all(lst))            # False

lst = [1 , 2, 3]
print(all(lst))
lst = [1 , 2, []]
print(all(lst))            # False

lst = [1, 2, 3]
print(all(lst))
lst = [1, 0, 3]
print(all(lst))            # False

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
lst = [1 , 2, 3]
print(any(lst))
lst = [1 , 2, []]
print(any(lst))             # False
lst = [0]
print(any(lst))             # False
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
print('zip():')
lst1 = ['A', 'B', 'C', 'D', 'E']
lst2 = list(range(10))
zipped = zip(lst1, lst2)        # iterator 
print(zipped)
zipped = list(zipped)           # iterable (list)
print(zipped)
tpl1, tpl2 = zip(*zipped)
print(tpl1)
print(tpl2)
print('# --------------------------------------------- #')

print('enumerate():')
mySkills = ["C++", "Python", "PLC"]
print(type(enumerate(mySkills, 1)))
mySkillsEnum = enumerate(mySkills, 1)   # iterator
print(mySkillsEnum)
mySkillsEnum = list(mySkillsEnum)       # iterable (list)
print(mySkillsEnum)
for mySkill in mySkillsEnum:
    print(mySkill)
for count,skill in mySkillsEnum:
    print(count, skill)
print('# --------------------------------------------- #')

print('slice():')
myString = '0123456789'
print(myString[5:8])
print(myString[:8])                     # till a given end
print(myString[5:])                     # starting from a given start
print(myString[slice(5)])               # end is mandatory
print(myString[slice(5,8)])
print('# --------------------------------------------- #')

print('reversed():')
name = "Amr"
print(reversed(name))
print(name[::-1])
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
