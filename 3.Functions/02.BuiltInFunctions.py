# -------------------------------------------------------------------------------------------------------------
# Built-in Functions:
#   all(iterable)           returns True if all the iterable arguments (string, list, tuple or dictionary) are True
#   any(iterable)           returns True if any of the iterable arguments (string, list, tuple or dictionary) is True
#   bin(integer)            returns the binary code of the argument
#   id(variable)            returns the memory id of that variable
#   sum(iterable, start)    returns the sum of the elements
#   round(digit, accuracy)  returns the round of a digit with (optionally) certain accuracy
#   range(start, end, step) returns a <class 'range'> with (optionally) start other than 0
#                                                      and (optionally) certain step
#   print(string)           prints the given string on the console
#                               the seperator is by default " " and can be modified
#                               the line end is by default "\n" and can be modified
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
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

print('bin():')
num = 65535
print(bin(num))
print('# --------------------------------------------- #')

print('id():')
num = 12
print(id(12))
print(id(num))
num = 14
print(id(12))
print(id(num))              # id changes here as the value changed
print('# --------------------------------------------- #')

print('sum():')
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 12))
print('# --------------------------------------------- #')

print('round():')
print(round(1.99))
print(round(1.99, 1))
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

print('print():')
print("Amr", "Awad")                    # Default seperator is space
print("Amr", "Awad", sep = " @ ")       # Seperator can be modified
print("First line")                     # Default line ending is "\n"
print("Second line", end = " ")         # Line ending can be modified
print("Third line")
print('# --------------------------------------------- #')
