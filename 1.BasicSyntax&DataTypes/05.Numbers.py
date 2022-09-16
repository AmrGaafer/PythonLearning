# -------------------------------------------------------------------------------------------------------------
# Nmubers:
# Types:
#   -> Integer (int)
#   -> floating point (float)
#   -> complex  (complex)
#       to get the real part: complexVar.real
#       to get the complex part: complexVar.imag
# Type Casting:
#   to int:     int(realVar)
#   to float:   float(intVar)
#   to complex: complex(intVar or realVar)
#
# Arithmetic Operators:
# [+]   addition
# [-]   subtraction
# [*]   multiplication
# [**]  exponent
# [/]   division
# [%]   modulus
# [//]  floor division
#
# Assignment Operators:
# [=]   assignment operator
# [+=]  addition assignment operator
# [-=]  subtraction assignment operator
# [*=]  multiplication assignment operator
# [**=] exponent assignment operator
# [/=]  division assignment operator
# [%=]  modulus assignment operator
# [//=] floor division assignment operator
# Syntax:
#   var1 = var1 [arithmatic operator] var2  <=> var1 [arithmatic operator]= var2
#
# Comparison Operators:
# [==]  equal
# [!=]  not equal
# [<]   less than
# [>]   greater than
# [<=]  less than or equal
# [>=]  greater than or equal
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('NUMBERS:\n')

print(type(0))
print(type(1012))
print(type(-1012))

print(type(0.0))
print(type(1012.23))
print(type(-1012.23))

print(type(0+ 5j))
print("The real part is: {}".format((0+ 5j).real) + ", it is: {}".format(type((0+ 5j).real)))
print("The imaginary part is: {}".format((0+ 5j).imag) + ", it is: {}".format(type((0+ 5j).imag)))

print('\n# ********************************************* #')
print('Types Casting:\n')

print('int:')
print(int(100.2))
print(int(100.9))
print(int(-100.2))
print(int(-100.9))
#print(int(100.9 + 5j))     # Error

print('float:')
print(float(0))
print(float(100))
print(float(-100))
#print(float(100.9 + 5j))   # Error

print('complex:')
print(complex(100.2))
print(complex(0))

# Assignment operators:
print('Assignment operators')
x = 1
y = 2

x += y
print(x)    #3
x -= y
print(x)    #1
x *= y
print(x)    #2
x **= y
print(x)    #4
x /= y
print(x)    #2
x %= y
print(x)    #0
x //= y
print(x)    #0

# Assignment operator:
print('Comparison operators')

print(10 == 50)
print(10 != 50)
print(10 > 50)
print(10 < 50)
print(10 >= 50)
print(10 <= 50)
