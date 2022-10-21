# -------------------------------------------------------------------------------------------------------------
# Boolean:
# logical variable: True or False
# Type Casting:
#   bool(var):     to boolean, True if not empty or has a numirical value other than 0
# Boolean Operators:
#   and, or, not
# Bitwise Operators:
#   <<(left shift), >>(right shift), &, |, ^(XOR), and ~(-x-1)
# Membership Operators:
#   in, not in
#   Syntax: x in y | x not in y
#           returns True if x is found in y
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

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

print('Bitwise Operators:')
print("binary value: {0:b}".format(int('100',2)))
print("right shift:  {0:b}".format(int('100',2)>>1))
print("left shift:   {0:b}".format(int('100',2)<<1))
print("bitwise and:  {0:b}".format(int('11111111', 2) & int('10101010', 2)))
print("bitwise or:   {0:b}".format(int('11111111', 2) | int('10101010', 2)))
print("bitwise xor:  {0:b}".format(int('11111111', 2) ^ int('10101010', 2)))
print("-value-a:     {0:b}".format(~ int('10101010', 2)))

print('Membership Operators:')
mySet = ['doctor', 'engineer', 'farmer', 'worker']
myJob = 'singer'
print(f'Is my job found in thr list? {myJob in mySet}')
myJob = 'engineer'
print(f'Is my job found in thr list? {myJob in mySet}')
