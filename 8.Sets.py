# -------------------------------------------------------------------------------------------------------------
# Sets:
# 1. sets are enclosed in curly braces
# 2. sets items are not ordered and not indexed -> no indexing and no slicing
# 3. sets items can be only mutable data types (numbers, strings and tuples)
#      lists and dictionaries are unhashable data type
# 4. sets items are unique
# -------------------------------------------------------------------------------------------------------------

print('\n# *********************************S************ #')
print('SETS:\n')

myAwesomeSet = {'Amr', 'Wael', 'Ali', 110388, 120419, 110388, "Ali"}
print(myAwesomeSet)

#print(myAwesomeSet[0])       # Error
#print(myAwesomeSet[0:2])     # Error

myAwesomeSet = {'Amr', 'Wael', 'Ali', (110388, 120419)}
print(myAwesomeSet)
#myAwesomeSet = {'Amr', 'Wael', 'Ali', [110388, 120419]}