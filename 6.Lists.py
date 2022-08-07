# -------------------------------------------------------------------------------------------------------------
# Lists:
# 1. list items are enclosed in square brackets
# 2. list items are ordered with zero-inddex base'
# 3. list items can be different data types
# 4. list items are mutable (editable) -> edit, delete and add
# -------------------------------------------------------------------------------------------------------------

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

# Edit
print('Edit:')
myAwesomeList = ['one', 'two', 'three', 15, 100.5, False]
print(myAwesomeList)
myAwesomeList[0:3] = [1, 2 , 3 , 4] # edit
print(myAwesomeList)
myAwesomeList[0:4] = []             # delete
print(myAwesomeList)
#myAwesomeList[4] = 5               # add is not possible this way
#print(myAwesomeList)
