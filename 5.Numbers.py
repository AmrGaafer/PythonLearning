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
# Arithmetic Operators:
# [+]   addition
# [-]   subtraction
# [*]   multiplication
# [**]  exponent
# [/]   division
# [%]   modulus
# [//]  floor division
# -------------------------------------------------------------------------------------------------------------

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
