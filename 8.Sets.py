# -------------------------------------------------------------------------------------------------------------
# Sets:
# 1. sets are enclosed in curly braces
# 2. sets items are not ordered and not indexed -> no indexing and no slicing
# 3. sets items can be only mutable data types (numbers, strings or tuples)
#      lists and dictionaries are unhashable data type
# 4. sets items are unique
# -------------------------------------------------------------------------------------------------------------

print('\n# *********************************S************ #')
print('SETS:\n')

myAwesomeSet = {'Amr', 'Wael', 'Ali', 110388, 120419, 110388, "Ali", (1 , 2)}
print(myAwesomeSet)

#print(myAwesomeSet[0])       # Error
#print(myAwesomeSet[0:2])     # Error

myAwesomeSet = {'Amr', 'Wael', 'Ali', (110388, 120419)}
print(myAwesomeSet)
#myAwesomeSet = {'Amr', 'Wael', 'Ali', [110388, 120419]}

# -------------------------------------------------------------------------------------------------------------
# Sets Methods:
# 1.  clear()
#   clears the set, the clear set is inticated with set()
# 2. setA.union(setB, setC,...)
#   returns the union of all the required sets, the sets don't change
# 3. set.add(element)
#   adds an element to the set, this element can be a number ,a string or a tuple (standard set element)
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('SETS METHODS:\n')
print('clear method:')
myAwesomeSet = {1 , 2, 3}
print(myAwesomeSet)
myAwesomeSet.clear()
print(myAwesomeSet)     # set()
print('# --------------------------------------------- #')

print('union method:')
myAwesomeSetA = {1 , 2, 3}
myAwesomeSetB = {4 , 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
(myAwesomeSetA.union(myAwesomeSetB))
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
