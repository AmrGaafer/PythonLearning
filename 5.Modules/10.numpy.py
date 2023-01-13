# --------------------------------------------------------------------------------------------------
# numpy: Numerical Python open-source external module 
#        to deal with large multi-dimentional arrays and matrices
# advantage of numpy arrays:
#   - easy to use
#   - elements are stored contigously
#   - space (memory) and time effiecient
#   - supports element wise operation
# Python list:
#   Homogeneous:    contain the same type of objects
#   Hetrogeneous:   contain different types of objects
# numpy arrays:
#   - have to be homogeneous, this helps to determine the storage size needed for the array
#     if the input elements to the array() method are mixed types, the method unites them in one type
#   - zero-based indexing
# Syntax:
#   np.array(iterator)  creates a numpy array
#   np_array.ndim       array dimension
#   np_array.itemsize   array item size in bytes
#   np_array.size       length of the array
#   np_array.dtype      array type read or write
#   np_array.astype()   change array type
#       numby Data types:
#           '?'         boolean
#           'b'         (signed) byte
#           'B'         unsigned byte
#           'i'         (signed) integer
#           'u'         unsigned integer
#           'f'         floating-point
#           'c'         complex floating-point
#           'm'         time-delta
#           'O'         Python objects
#           'S','a'     Zero-teminated bytes (not recommended)
#           'U'         Unicode string
#           'V'         raw data (void)
#
# Useful Operations:
#   Arithmatic operations (add, subtract,...) arrays have to be the same dimension
#   np_array.min()      min
#   np_array.max()      max
#   np_array.sum()      sum
#   np_array.ravel()    returns flattened array 1 dimension with same type
#
# Shape and Reshape:
#   np_array.shape      returns a tuple contains the number of elements in each dimension
#   np_array.reshape()  returns a reshaped array with the given dimensions
#                       np_array.reshape(-1) is equivalent to np_array.ravel()
#                       NOTE: the multiplication of the given dimensions should equal np_array.size
# --------------------------------------------------------------------------------------------------

import os
import numpy as np      # numpy module
from time import time
from sys import getsizeof
os.system('cls')        # cls command

print('numby:\n')
print('numpy version: ', np.__version__)
#print(dir(np))

# Creating array
my_list = [1, 2, 3, 4]          # create a list
my_array = np.array(my_list)    # create an array
print(my_list)
print(my_array)
print(type(my_list))
print(type(my_array))

# Elements Id -> array elements are contigous
print('elemtents id:')
print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))

# Accessing Elements
print('accessing elements (indexing):')
print(my_list[0])
print(my_list[1])
print(my_array[0])
print(my_array[1])

print('accessing elements (slicing):')
my_array = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
print(my_array.ndim)
print(my_array[1:4])
print(my_array[:4])

# Types Unify
print('\ntypes unify:')
my_list = [1, 2, 3, 4, 3.15, 'A']
my_array = np.array(my_list)
print(type(my_array[0]))
my_list = [1, 2, 3, 4, 3.15]
my_array = np.array(my_list)
print(type(my_array[0]))
my_list = [True, False, True]
my_array = np.array(my_list)
print(type(my_array[0]))
my_list = [True, False, True, 1]
my_array = np.array(my_list)
print(type(my_array[0]))

# Creating multi-dimensional array
print('\nmulti-dimensional arrays:')
a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1,11], [2, 12]], [[3, 13], [4, 14]]])

# Dimensions
print('dimensions:')
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Accessing Elements
print('accessing elements (indexing):')
print(a)
print(b[0])
print(c[0][0])
print(d[0][0][0])
print(d[1, 1, 1])   # equivalent indexing syntax

# Creating custom-dimensional array:
print('\ncustom-dimensional arrays:')
my_custom_array = np.array([1, 2, 3], ndmin= 3)
print('dimension: ', my_custom_array.ndim)
print(my_custom_array)
print(my_custom_array[0])
print(my_custom_array[0][0])
print(my_custom_array[0][0][0])

print('\naccessing elements (slicing):')
my_list = np.array([['A', 'B', 'X'],
                    ['C', 'D', 'Y'],
                    ['E', 'F', 'Z'],
                    ['M', 'N', 'O']])
print(my_list[0:3, 0:2])
print(my_list[1:3, 1:])
print(my_list[2:, :2])
print(my_list[0::2, :2])

# Performance check
print('\nperformance check (time and space):')
elements = 150
my_list1 = range(elements)
my_list2 = range(elements)
my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

list_start = time()
list_result = [n1 + n2 for n1, n2 in zip(my_list1, my_list2)]
print(f'list time: {time() - list_start} ')
print(f'item size: {getsizeof(list_result[0])} Byte')   # item size in Byte
print(f'list size: {len(list_result)}')                 # no of elements
print(f'total list size: {getsizeof(list_result[0]) * len(list_result)} Byte')

array_start = time()
array_result = my_array1 + my_array2
print(f'array time: {time() - array_start} ')
print(f'item size: {array_result.itemsize} Byte')       # item size in Byte
print(f'array size: {array_result.size}')               # no of elements
print(f'total array size: {array_result.itemsize * array_result.size} Byte')

# Data Types and Control Array
print('\nData Types and Control Array:')
my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 3.15, 22])
my_array3 = np.array(['Amr', 'Gaafer'])

print('Data Types:')
print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print('Data Type Control:')
my_array1 = np.array([1, 2, 3], dtype= float)           # float, 'float' or 'f'
my_array2 = np.array([1.5, 3.15, 22], dtype= int)       # 'int64', int, 'int' or i
my_array3 = np.array(['Amr', 'Gaafer'], dtype= '<U80')  # chnage unicode size
print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print('Data Type Control of Existing Array:')
my_array1 = my_array1.astype('int32')
print(my_array1)
print(my_array1.dtype)
print(my_array1.itemsize)
my_array1 = my_array1.astype('int64')
print(my_array1)
print(my_array1.dtype)
print(my_array1.itemsize)

print('\nArithmatic Operations:')
print('one dimensional array:')
my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])
print(my_array1 + my_array2)
print(my_array1 - my_array2)
print(my_array1 * my_array2)
print(my_array1 / my_array2)
print(my_array1 // my_array2)
print(my_array1 % my_array2)
print('min:', my_array1.min())
print('max:', my_array1.max())
print('sum:', my_array1.sum())
print('ravel:', my_array1.ravel())
print('min:', my_array2.min())
print('max:', my_array2.max())
print('sum:', my_array2.sum())
print('ravel:', my_array2.ravel())

print('two dimensional array:')
my_array1 = np.array([[1, 2], [3,4]])
my_array2 = np.array([[5, 6], [6, 7]])
print(my_array1 + my_array2)
print(my_array1 - my_array2)
print(my_array1 * my_array2)
print(my_array1 / my_array2)
print(my_array1 // my_array2)
print(my_array1 % my_array2)
print('min:', my_array1.min())
print('max:', my_array1.max())
print('sum:', my_array1.sum())
print('ravel:', my_array1.ravel())
print('min:', my_array2.min())
print('max:', my_array2.max())
print('sum:', my_array2.sum())
print('ravel:', my_array2.ravel())

print('\nArray shape and reshape:')
print('shape:')
my_array1 = np.array([1, 2, 3, 4])
print('ndim: ', my_array1.ndim)
print('shape: ', my_array1.shape)
my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print('ndim: ', my_array2.ndim)
print('shape: ', my_array2.shape)
my_array3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]])
print('ndim: ', my_array3.ndim)
print('shape: ', my_array3.shape)

print('reshape:')
my_array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print('ndim: ', my_array1.ndim)
print('shape: ', my_array1.shape)
print('size: ', my_array1.size)
print(my_array1.reshape(3, 4, 1))
my_array2 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print('ndim: ', my_array2.ndim)
print('shape: ', my_array2.shape)
print('size: ', my_array2.size)
print(my_array2.reshape(10, 2))
print(my_array2.reshape(2, 5, 2))
