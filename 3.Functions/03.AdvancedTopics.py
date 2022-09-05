# -------------------------------------------------------------------------------------------------------------
# Advanced Topics in Functions:
#   1. map(function, iterator): returns the address of the map object
#       - accepts a function + iterator
#       - runs the function on every element of the iterator
#       - the function can be either a pre-defined function or a lambda function
#
#   2. filter(function, iterator): returns the address of the filter object
#       - accepts a function + iterator
#       - runs the function on every element of the iterator
#       - the function can be either a pre-defined function or a lambda function
#       - expects a boolean return from the function
#       - filters out all iterable elements for which the function returns True
#
#   3. reduce(function, iterator): returns the result of the reduce object
#       - accepts a function + iterator
#       - runs the function on the first two elements of the iterator
#       - then, runs the functin on the result and the third element of the iterator, and so on...
#       - the function can be either a pre-defined function or a lambda function
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('map:\n')
print('Pre-defined function:')
def formatText(name):
    return f"- {name.strip().capitalize()} -"
myText = ['Amr', 'Gaafer']
myFormatedText = map(formatText, myText)
print(myFormatedText)
for name in myFormatedText:
    print(name)

print('lambda function:')
myText = ['  amr', 'gaafer   ']
for name in map(lambda name: f"- {name.strip().capitalize()} -", myText):
    print(name)
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('filter:\n')
print('Pre-defined function:')
def checkNumber(num):
    return num > 10
myNums = [0, 1, 19, 10, 20, 100, 5]
myResult = filter(checkNumber, myNums)

for num in myResult:
    print(num)

print('lambda function:')
myNames = ["Amr", "Osama", "osOO", "Othman"]
for name in filter(lambda name: name.startswith('O'), myNames):
    print(name)
print('# --------------------------------------------- #')

print('\n# ********************************************* #')
print('reduce:\n')
from functools import reduce
myNums = [1, 8, 2, 9, 12]
myResult = reduce(lambda num1, num2: num1+num2, myNums)
print(myResult)
print('# --------------------------------------------- #')
