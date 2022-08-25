# -------------------------------------------------------------------------------------------------------------
# Built-in Functions:
#   all(iterable)       returns True if all the iterable arguments (string, list, tuple or dictionary) are True
#   any(iterable)       returns True if any of the iterable arguments (string, list, tuple or dictionary) is True
#   bin(integer)        returns the binary code of the argument
#   id(variable)        returns the memory id of that variable
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
num = 5
print(bin(num))
print('# --------------------------------------------- #')

print('id():')
num = 12
print(id(12))
print(id(num))
num = 14
print(id(12))
print(id(num))
print('# --------------------------------------------- #')
