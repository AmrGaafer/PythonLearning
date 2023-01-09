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
# --------------------------------------------------------------------------------------------------

import os
import numpy as np      # numpy module
from time import time
import sys
os.system('cls')        # cls command

print('numby:\n')
print('numpy version: ', np.__version__)
#print(dir(np))

my_list = [1, 2, 3, 4]          # create a list
my_array = np.array(my_list)    # create an array

print(my_list)
print(my_array)
print(type(my_list))
print(type(my_array))

# Accessing Elements
print('accessing elements:')
print(my_list[0])
print(my_list[1])
print(my_array[0])
print(my_array[1])

# Elements Id
print('elemtents id:')
print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))

# Types Unify
print('\ntypes unify:')
my_list = [1, 2, 3, 4, 3.15, 'A']
my_array = np.array(my_list)    # create an array
print(type(my_array[0]))
my_list = [1, 2, 3, 4, 3.15]
my_array = np.array(my_list)    # create an array
print(type(my_array[0]))
my_list = [True, False, True]
my_array = np.array(my_list)    # create an array
print(type(my_array[0]))
my_list = [True, False, True, 1]
my_array = np.array(my_list)    # create an array
print(type(my_array[0]))

# Creating multi-dimensional array
print('\nmulti-dimensional arrays:')
a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1,11], [2, 12]], [[3, 13], [4, 14]]])

# Accessing Elements
print(a)
print(b[0])
print(c[0][0])
print(d[0][0][0])
print(d[1, 1, 1])

# Dimensions
print('dimensions:')
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Creating custom-dimensional array:
print('\ncustom-dimensional arrays:')
my_custom_array = np.array([1, 2, 3], ndmin= 3)
print('dimension: ', my_custom_array.ndim)
print(my_custom_array)
print(my_custom_array[0])
print(my_custom_array[0][0])
print(my_custom_array[0][0][0])

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
print(f'item size: {sys.getsizeof(list_result[0])}')                          # item size in Byte
print(f'list size: {len(list_result)}')                                       # no of elements
print(f'total list size: {sys.getsizeof(list_result[0]) * len(list_result)} Byte')

array_start = time()
array_result = my_array1 + my_array2
print(f'array time: {time() - array_start} ')
print(f'item size: {array_result.itemsize}')                                # item size in Byte
print(f'array size: {array_result.size}')                                   # no of elements
print(f'total array size: {array_result.itemsize * array_result.size} Byte')
