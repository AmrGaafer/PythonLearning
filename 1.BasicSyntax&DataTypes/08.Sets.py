# -------------------------------------------------------------------------------------------------------------
# Sets:
# 1. sets are enclosed in curly braces
# 2. sets items are not ordered and not indexed -> no indexing and no slicing
# 3. sets items can be only mutable data types (numbers, strings or tuples)
#      lists and dictionaries are unhashable data type
# 4. sets items are unique
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('SETS:\n')

myAwesomeSet = {'Amr', 'Adam', 'Yousuf', 110388, 120419, 110388, "Yousuf", (1 , 2)}
print(myAwesomeSet)

#print(myAwesomeSet[0])       # Error
#print(myAwesomeSet[0:2])     # Error
#myAwesomeSet = {'Amr', 'Adam', 'Yousuf', [110388, 120419]}    # Error as list is a hashable data type

# -------------------------------------------------------------------------------------------------------------
# Sets Methods:
# 01. clear()
#   clears the set, the clear set is inticated with set()
# 02. copy()
#   returns a shallow copy of the set
#
# 03. set.add(element)
#   adds an element to the set, this element can be a number ,a string or a tuple (standard set element)
# 04.setA.union(setB, setC,...) OR setA | setB | ...
#   returns the union of all the required sets, the sets don't change
# 05. update(set argument)
#   updated the set by the union of it with the given set argument
#
# 06. remove()
#   removes the given element content from the whole set
#   if the element doesn't exist, it produces an error
# 07. discards()
#   discards the given element content from the whole set
#   if the element doesn't exist, it produces an error
# 08. pop()
#   removes an element randomly
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('SETS METHODS:\n')
print('clear method:')
myAwesomeSet = {1 , 2, 3}
print(myAwesomeSet)
myAwesomeSet.clear()
print(myAwesomeSet)     # set()
print('# --------------------------------------------- #')

print('copy method:')
myAwesomeSet = {1 , 2, 3}
print(f"myAwesomeSet: {myAwesomeSet}")
myAwesomeSet2 = myAwesomeSet.copy()
print(f"myAwesomeSet2: {myAwesomeSet2}")
myAwesomeSet.add(4)
print(f"myAwesomeSet: {myAwesomeSet}")
print(f"myAwesomeSet2: {myAwesomeSet2}")
print('# --------------------------------------------- #')

print('add method:')
myAwesomeSet = {1 , 2, 3}
print(myAwesomeSet)
myAwesomeSet.add(-5.6+3j)
print(myAwesomeSet)
myAwesomeSet.add('5')
print(myAwesomeSet)
myAwesomeSet.add((15,14))
print(myAwesomeSet)
print('# --------------------------------------------- #')

print('union method:')
myAwesomeSetA = {1 , 2, 3}
myAwesomeSetB = {4 , 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.union(myAwesomeSetB))
print('# --------------------------------------------- #')

print('update method:')
myAwesomeSetA = {1 , 2, 3}
myAwesomeSetB = {4 , 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
myAwesomeSetA.update(myAwesomeSetB)
print(myAwesomeSetA)
myAwesomeSetA.update(['Amr', 'Adam'])
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('remove method:')
myAwesomeSet = {1 , 2, 3}
print(myAwesomeSet)
myAwesomeSet.remove(1)
print(myAwesomeSet)
myAwesomeSet.remove(2)
print(myAwesomeSet)
myAwesomeSet.remove(3)
print(myAwesomeSet)     # set()
print('# --------------------------------------------- #')

print('discard method:')
myAwesomeSet = {1 , 2, 3}
print(myAwesomeSet)
myAwesomeSet.discard(1)
print(myAwesomeSet)
myAwesomeSet.discard(2)
print(myAwesomeSet)
myAwesomeSet.discard(4)
print(myAwesomeSet)
print('# --------------------------------------------- #')

print('pop method:')
myAwesomeSet = {0 , 2, 3, 100, -15.5}
print(myAwesomeSet.pop())
print(myAwesomeSet)
print('# --------------------------------------------- #')
