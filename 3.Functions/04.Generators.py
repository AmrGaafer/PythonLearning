# -------------------------------------------------------------------------------------------------------------
# Iterable:
#   Object that contains data that can be iterated upon (e.g. string, list, tuple, set, and dictionary)
#   - it can return one of its elements at a time
#
# Iterator:
#   Object that represents a stream of data,
#   it can be used to iterate over an iterable using next() method and returns one element at a time
#   - iter(iterable): generates an iterator from the given iterable (), returns a pointer
#   - next(iterator): returns the next item (iterator) of the iterated upon iterable
#                   returns 'StopIteration' if there is no next element
#   Hint: for-loop already calls iter() and next() methods
#
# Generators:
#   Function with "yield" keyword instead of "return", it creates an iterator
#   - supports iteration an returns an iterator by calling "yield"
#   - generator function can have more than one "yield"
#   - by using next(), it resumes from the last "yield" call not from the begining
#   - function call does not loop over the iterator, it gives only the control using "next()" method
#   NOTE: Generators are a lazy way to build iterables. 
#         They are useful when the fully realized list would not fit in memory, 
#         or when the cost to calculate each list element is high and you want to do it as late as possible. 
#         But they can only be iterated over once.
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

def myGenerator(name):
    for chr in name:
        yield chr

print(myGenerator('unknown'))
print(type(myGenerator('unknown')))
myIterator = myGenerator('Amr')
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# print(next(myIterator))


def my_enumerate(iterable, start=0):
    for item in iterable:
        yield (start, item)
        start += 1

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# Chunker
def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

# Generator expressions
sq_list = [x**2 for x in range(10)]         # this produces a list of squares
print(type(sq_list))
print(sq_list)

sq_iterator = (x**2 for x in range(10))     # this produces an iterator of squares (saves time)
print(type(sq_iterator))
print(sq_iterator)
