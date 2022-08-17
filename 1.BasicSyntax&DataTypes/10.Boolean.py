# -------------------------------------------------------------------------------------------------------------
# Boolean:
# logical variable: True or False
# Type Casting:
#   bool(var):     to boolean, True if not empty or has a numirical value other than 0
# Boolean Operators:
#   and, or, not
# Membership Operators:
#   in, not in
#   Syntax: x in y | x not in y
#           returns True if x is found in y
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('BOOLEAN:\n')

print(bool(True))
print(bool(False))

print(bool(100))
print(bool(0))

print(bool(1))
print(bool(None))

print(bool(100.0))
print(bool(0.0))

print(bool(100.0+5j))
print(bool(0.0+0.0j))

print(bool("Amr"))
print(bool(""))

print(bool([1,0]))
print(bool([]))

print('Membership Operators:')
mySet = ['doctor', 'engineer', 'farmer', 'worker']
myJob = 'singer'
print(f'Is my job found in thr list? {myJob in mySet}')
myJob = 'engineer'
print(f'Is my job found in thr list? {myJob in mySet}')
