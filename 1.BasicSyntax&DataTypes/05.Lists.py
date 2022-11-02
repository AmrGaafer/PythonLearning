# -------------------------------------------------------------------------------------------------------------
# Lists:
# 1. list items are enclosed in square brackets
# 2. list items are ordered with zero-inddex base
# 3. list items can be different data types
# 4. list items are mutable (editable) -> edit, delete and add
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('LISTS:\n')
myAwesomeList = ["string", 1, 102.5, 3+7j, True]
print(type(myAwesomeList))
print(type(myAwesomeList[0]))
print(type(myAwesomeList[1]))
print(type(myAwesomeList[2]))
print(type(myAwesomeList[3]))
print(type(myAwesomeList[4]))

print('\n# ********************************************* #')
print('LISTS INDEXING AND SLICING:\n')
print('len function:')
print(len(myAwesomeList))

# Indexing
print('Indexing:')
print(myAwesomeList[0])
print(myAwesomeList[1])
print(myAwesomeList[2])
print(myAwesomeList[3])
print(myAwesomeList[4])

# Slicing
print('Slicing:')
print(myAwesomeList[1:3])   # items 1 & 2
print(myAwesomeList[2:])    # items 2 till the end
print(myAwesomeList[:4])    # start till item 3
print(myAwesomeList[::2])   # all items with step 2
print(myAwesomeList[:])     # all list
print(myAwesomeList[::])    # all list
print(myAwesomeList[::-1])  # all list reversed

# Edit
print('Edit:')
myAwesomeList = ['one', 'two', 'three', 15, 100.5, False]
myAwesomeList2 = [1, 2, 3, 4]
print(myAwesomeList + myAwesomeList2)   # adding
print(myAwesomeList)
myAwesomeList[0:3] = [1, 2 , 3 , 4]     # edit
print(myAwesomeList)
myAwesomeList[0:4] = []                 # delete
print(myAwesomeList)
#myAwesomeList[4] = 5                   # element add is not possible this way
#print(myAwesomeList)

# -------------------------------------------------------------------------------------------------------------
# Lists Methods:
# 1.  append(element)
#   appends an element by the end of the list, the appended element is added as just one element
#   the element type can be: int, float, string, complex or list
# 2.  insert(index, object)
#   inserts the provided object before index, the inserted element is added as just one element
#   the element type can be: int, float, string, complex or list
# 3.  extend(element)
#   extends the original list with that given arguement (element)
#   the element type can be: array and each element is added individually
#                            or 
#                            string, each letter is considered as a signle element
# 4.  remove(element content)
#   removes the given element content from the whole list (int, float, complex or string)
# 5.  pop(index)
#   removes and returns item of that index
#
# 6.  sort(reverse = True/False, key = myFunction)
#   sorts numerrical or string (not both together) values in ascending or descending order
#       (default) reverse = False -> Ascending order
#       reverse = True -> Descending order
#       (Optional) key to give a sorting function (e.g. len to sort according to the length)
#
# 7.  reverse()
#   reverses the list
#
# 8.  clear()
#   clears the list
# 9.  copy()
#   returns a shallow copy of the list
#
# 10. count(element)
#   returns how many occurancies of the element are found in the list
# 11. index(element)
#   returns the first index of the element found in the list
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('LISTS METHODS:\n')
print('append method:')
myNames = ["Amr"]
print(myNames)

myNames.append("Wael")
print(myNames)

myNames.append("Ali")
print(myNames)

myNames.append(["Awad", "Gaafer"])
print(myNames)
print(myNames[1])
print(type(myNames[1]))
print(myNames[3])
print(type(myNames[3]))
print(myNames[3][0])
print(myNames[3][1])
print(type(myNames[3][1]))
print('# --------------------------------------------- #')

print('insert method:')
myNames = ['Wael', 'Gaafer']
myNames.insert(0, "Amr")
myNames.insert(2, ["Ali", "Awad"])
print(myNames)
print('# --------------------------------------------- #')

print('extend method:')
myNames = ["Amr"]
print(myNames)
myNames.extend(["Wael"])
print(myNames)
myNames.extend(["Ali"])
print(myNames)
myNames.extend(["Awad", "Gaafer"])
print(myNames)

myNumbers = [1 , 2, 3]
print(myNumbers)
myNumbers.extend([4])
print(myNumbers)
myNumbers.extend([5, 6])
print(myNumbers)
print('# --------------------------------------------- #')

print('remove method:')
myNames = ['Amr', 'Wael', 'Ali', 'Awad', 'Gaafer']
myNames.extend([110388])
print(myNames)
myNames.remove(110388)
print(myNames)
myNames.remove("Gaafer")
print(myNames)
print('# --------------------------------------------- #')

print('pop method:')
myNames = ['Amr', 'Wael', 'Ali', 'Awad', 'Gaafer']
myName = myNames.pop(0)
print(myName)
print(myNames)

print('# --------------------------------------------- #')

print('sort method:')
myNumbers = [-100, 15.7, 26, 0, -2.31, -1024 , 650000]
print(myNumbers)
myNumbers.sort()
print(myNumbers)
myNumbers.sort(reverse= False)
print(myNumbers)
myNumbers.sort(reverse= True)
print(myNumbers)

myNames.sort()
print(myNames)
myNames.sort(reverse= True)
print(myNames)
myNames.sort(key= len)
print(myNames)
print('# --------------------------------------------- #')

print('reverse method:')
myNumbers = [-100, 15.7, 26, 0, -2.31, -1024 , 650000]
print(myNumbers)
myNumbers.reverse()
print(myNumbers)

myNames = ['Amr', 'Wael', 'Ali', 'Awad']
print(myNames)
myNames.reverse()
print(myNames)
print('# --------------------------------------------- #')

print('clear method:')
myNumbers = [-100, 15.7, 26, 0, -2.31, -1024 , 650000]
print(myNumbers)
myNumbers.clear()
print(myNumbers)

myNames = ['Amr', 'Wael', 'Ali', 'Awad']
print(myNames)
myNames.clear()
print(myNames)
print('# --------------------------------------------- #')

print('copy method:')
a = [0, 1, 2 , 3, 4]
b = a.copy()
print(a)
print(b)

a.append(5)
print(a)
print(b)
print('# --------------------------------------------- #')

print('count method:')
myNumbers = [-100, 15.7, 26, 0, -2.31, -1024 , 650000]
print(myNumbers.count(15.7))
print(myNumbers.count(0.0))
print(myNumbers.count(0))
print('# --------------------------------------------- #')

print('index method:')
myNames = ['Amr', 'Wael', 'Ali', 'Awad']
print(myNames.index("Awad"))
myNumbers = [-100, 15.7, 26, 0, -2.31, -1024 , 650000]
print(myNumbers.index(0.0))
print('# --------------------------------------------- #')
