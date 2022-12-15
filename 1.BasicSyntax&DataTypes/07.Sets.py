# -------------------------------------------------------------------------------------------------------------
# Sets: Mutable unordered sequence of elements
# 1. sets are enclosed in curly braces {}
# 2. sets items are unordered and not indexed -> no indexing and no slicing
# 3. sets items are unique
# 4. sets items can be only hashable data types (numbers, strings or tuples)
#      lists and dictionaries are unhashable data type
#
#   NOTE: Mutability: whether an object can change its values after it has been created
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('SETS:\n')

myAwesomeSet = {'Amr', 'Adam', 'Yousuf', 110388, 120419, 110388, "Yousuf", (1 , 2)}
print(myAwesomeSet)
myAwesomeSet2 = {1, 2, 3, 1}
print(myAwesomeSet2)
#print(myAwesomeSet + myAwesomeSet2)    	# concatenate is not supported

#print(myAwesomeSet[0])       # Error
#print(myAwesomeSet[0:2])     # Error
#myAwesomeSet = {'Amr', 'Adam', 'Yousuf', [110388, 120419]}    # Error as list is a hashable data type

# -------------------------------------------------------------------------------------------------------------
# Sets Methods:
# 01. set.add(element)
#   adds an element to the set, this element can be a number ,a string or a tuple (standard set element)
# 02. update(set argument)
#   updates the set by adding the given argument (it could be unhaschable data type, e.g list)
# 03. remove()
#   removes the given element content from the whole set
#   if the element doesn't exist, it produces an error
# 04. discards()
#   discards the given element content from the whole set
#   if the element doesn't exist, it does not produce an error
# 05. pop()
#   removes an element randomly
# 06. clear()
#   clears the set, the clear set is inticated with set()
#
# 07. copy()
#   returns a shallow copy of the set
#
# 08. setA.union(setB, setC,...) OR setA | setB | ...
#   returns the union of all the required sets, the sets don't change
# 09. setA.difference(setB) OR setA - setB
#   returns the differnce between setA and setB, setA doesn't update
# 10. setA.difference_update(setB) OR setA - setB
#   returns the differnce between setA and setB, setA updates
# 11. setA.intersection(setB) OR setA & setB
#   returns the intersection of setA and setB, setA doesn't update
# 12. setA.intersection_update(setB)
#   returns the intersection of setA and setB, setA updates
# 09. setA.symmetric_difference(setB) OR setA ^ setB
#   returns the symetric differnce setA and setB (XOR), setA doesn't update
# 10. setA.symmetric_difference_update(setB) OR setA - setB
#   returns the symetric differnce setA and setB (XOR), setA updates
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('SETS METHODS:\n')
print('add method:')
myAwesomeSet = {1, 2, 3}
print(myAwesomeSet)
myAwesomeSet.add(-5.6+3j)
print(myAwesomeSet)
myAwesomeSet.add('5')
print(myAwesomeSet)
myAwesomeSet.add((15,14))
print(myAwesomeSet)
print('# --------------------------------------------- #')

print('update method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {4, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
myAwesomeSetA.update(myAwesomeSetB)
print(myAwesomeSetA)
myAwesomeSetA.update(['Amr', 'Lina'])
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('remove method:')
myAwesomeSet = {1, 2, 3}
print(myAwesomeSet)
myAwesomeSet.remove(1)
print(myAwesomeSet)
myAwesomeSet.remove(2)
print(myAwesomeSet)
#myAwesomeSet.remove(4) # error
myAwesomeSet.remove(3)
print(myAwesomeSet)     # set()
print('# --------------------------------------------- #')

print('discard method:')
myAwesomeSet = {1, 2, 3}
print(myAwesomeSet)
myAwesomeSet.discard(1)
print(myAwesomeSet)
myAwesomeSet.discard(2)
print(myAwesomeSet)
myAwesomeSet.discard(4)
print(myAwesomeSet)
print('# --------------------------------------------- #')

print('pop method:')
myAwesomeSet = {10, 2, 3, 100, -15.5}
print(myAwesomeSet.pop())
print(myAwesomeSet)
print('# --------------------------------------------- #')

print('clear method:')
myAwesomeSet = {1 , 2 , 3}
print(myAwesomeSet)
myAwesomeSet.clear()
print(myAwesomeSet)     # set()
print('# --------------------------------------------- #')

print('copy method:')
myAwesomeSet = {1, 2, 3}
print(f"myAwesomeSet: {myAwesomeSet}")
myAwesomeSet2 = myAwesomeSet.copy()
print(f"myAwesomeSet2: {myAwesomeSet2}")
myAwesomeSet.add(4)
print(f"myAwesomeSet: {myAwesomeSet}")
print(f"myAwesomeSet2: {myAwesomeSet2}")
print('# --------------------------------------------- #')

print('union method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {4, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.union(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('difference method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.difference(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('difference_update method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.difference_update(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('intersection method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.intersection(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('intersection_update method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.intersection_update(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('symmetric_difference method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.symmetric_difference(myAwesomeSetB))
print(myAwesomeSetA)
print('# --------------------------------------------- #')

print('symmetric_difference_update method:')
myAwesomeSetA = {1, 2, 3}
myAwesomeSetB = {3, 5, 6}
print(myAwesomeSetA)
print(myAwesomeSetB)
print(myAwesomeSetA.symmetric_difference_update(myAwesomeSetB))
print(myAwesomeSetA)

# -------------------------------------------------------------------------------------------------------------
# Sets Methods with boolean return:
# 1. setA.issuperset(setB)                          checks if setA is superset of setB
# 2. setA.issubset(setB)                            checks if setA is subset of setB
# 3. setA.isdisjoint(setB)                          checks if setA and setB have no common element(s)
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('SETS METHODS WITH BOOLEAN RETURN:\n')

print('issuperset method:')
A = {1, 2, 3}
B = {1, 2, 3, 4}
C = {1, 2, 3, 4, 5} 
print(B.issuperset(A))
print(C.issuperset(A))
print(C.issuperset(B))
print(B.issuperset(C))
print('# --------------------------------------------- #')

print('issubset method:')
A = {1, 2, 3}
B = {1, 2, 3, 4}
C = {1, 2, 3, 4, 5} 
print(A.issubset(B))
print(C.issubset(A))
print(C.issubset(B))
print(B.issubset(C))
print('# --------------------------------------------- #')

print('isdisjoint method:')
A = {1, 2}
B = {3, 4}
C = {1, 2, 3, 4, 5} 
print(A.isdisjoint(B))
print(C.isdisjoint(A))
print(C.isdisjoint(B))
print(B.isdisjoint(C))
