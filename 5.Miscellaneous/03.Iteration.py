# -------------------------------------------------------------------------------------------------------------
# Iterable:
#   Object that contains data that can be iterated upon (e.g. string, list, set, tuple, dictionary)
#
# Iterator:
#   Object used to iterate over an iterable using next() method and returns one element at a time
#   - iter(iterable): generates an iterator from the given iterable (), returns a pointer
#   - next(iterator): returns the next item (iterator) of the iterated upon iterable
#                   returns 'StopIteration' if there is no next element
#   Hint: for-loop already calls iter() and next() methods
#
# Generators:
#   Function with "yield" keyword instead of "return"
#   - supports iteration an returns an iterator by calling "yield"
#   - generator function can have more than one "yield"
#   - by using next(), it resumes from the last "yield" call not from the begining
#   - function call does not loop over the iterator, it gives only the control using "next()" method
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('iterable vs. iterator:')
iterable1 = 'Amr'
iterable2 = ['python', 'C++', 'PLC']

for iterator in iterable1:
    print(iterator)

for iterator in iter(iterable2):
    print(iterator)

myIterator = iter(iterable1)

print(myIterator)           # returns an address of the saved iterator

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# print(next(myIterator))   # returns 'StopIteration'

print('\n# ********************************************* #')
print('Generators:')

def myGenerator():
    yield 'A'
    yield 'm'
    yield 'r'


print(myGenerator())
print(type(myGenerator()))
myIterator = myGenerator()
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# print(next(myIterator))
