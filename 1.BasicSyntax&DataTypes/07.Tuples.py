# -------------------------------------------------------------------------------------------------------------
# Tuples:
# 1. tuples are enclosed in parantheses, but parantheses can be removed
# 2. tuples items are ordered with zero-inddex base
# 3. tuples items can be different data types
# 4. tuples are immutable (cannot be modified)
# 5. tuples items are not unique
# 6. operators used in strings and lists are available in tuples
# 
# Notes:
# tuples with one element: (element,)
# the operator * repeat is valid for strings, lists and tuples
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# *********************************S************ #')
print('TUPLES:\n')
myAwesomeTuple = ("Amr", "Wael")
myAwesomeTuple2 = "Amr", "Wael"

print(myAwesomeTuple)
print(type(myAwesomeTuple))
print(myAwesomeTuple2)
print(type(myAwesomeTuple2))

print('\n# ********************************************* #')
print('TUPLES INDEXING:\n')
print('len function:')
print(len(myAwesomeTuple))

# Indexing
print('Indexing:')
myAwesomeTuple = 1, "Amr" , 3, 4+0j, False, 6.25
print(myAwesomeTuple[0])
print(myAwesomeTuple[1])
print(myAwesomeTuple[2])
print(myAwesomeTuple[3])
print(myAwesomeTuple[4])
print(myAwesomeTuple[-1])

# Tuples are immutable
#myAwesomeTuple[0] = 1      # Error 

print('\n# ********************************************* #')
print('TUPLES WITH ONE ELEMENT:\n')
myAwesomeTuple = (1)
print(type(myAwesomeTuple))
myAwesomeTuple = (1,)
print(type(myAwesomeTuple))

print('\n# ********************************************* #')
print('TUPLES CONCATENATION:\n')
myAwesomeTuple = 1, 2, 3, 4
myAwesomeTuple2 = "Amr", "Wael"
print(myAwesomeTuple + myAwesomeTuple2)

print('\n# ********************************************* #')
print('REPEAT *:\n')
myString = "Amr"
myList = ["Amr", "Wael"]
myTuple = ("Amr", "Wael")

print(myString * 6)
print(6 * myList)
print(6 * myTuple)

# -------------------------------------------------------------------------------------------------------------
# Tuples Methods:
# 1. count(element)
#   returns how many occurancies of the element are found in the tuple
# 2. index(element)
#   returns the first index of the element found in the tuple
# NOTE: tuples could be destructed!
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('LISTS METHODS:\n')
print('count method:')
myNumbers = (-100, 15.7, 26, 0, -2.31, -1024 , 650000)
print(myNumbers.count(15.7))
print(myNumbers.count(0.0))
print(myNumbers.count(0))
print('# --------------------------------------------- #')

print('index method:')
myNames = ('Amr', 'Wael', 'Ali', 'Awad')
print(myNames.index("Awad"))
myNumbers = (-100, 15.7, 26, 0, -2.31, -1024 , 650000)
print(myNumbers.index(0.0))
print('# --------------------------------------------- #')

print("Tuple Destruct:")
myNames = ('Amr', 'Wael', 'Ali', 'Awad')
a, b, c, d = myNames
print(a); print(b); print(c); print(d)

myNames = ('Amr', 'Wael', 15, 'Ali', 'Awad')
a, b, _, c, d = myNames                 # ignore the 3rd element
print(a); print(b); print(c); print(d)
