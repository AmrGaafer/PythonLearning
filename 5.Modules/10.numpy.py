# --------------------------------------------------------------------------------------------------
# numpy: Numerrical Python open-source module to deal with large multi-dimentional arrays and matrices
# advantage of numpy arrays:
#   - easy to use
#   - memory and space effiecient
#   - supports element wise opetation
#   - elements are stored contigously
# Python list:
#   Homogeneous:    contain the same type of objects
#   Hetrogeneous:   contain different types of objects
# numpy arrays:
#   have to be homogeneous, this helps to determine the storage size needed for the array
#   zero-based indexing
# --------------------------------------------------------------------------------------------------

import os
import numpy as np      # numpy module
os.system('cls')        # cls command

print('numby:')
#print(dir(np))
print('numpy version: ', np.__version__)

my_list = [1, 2, 3, 4]
my_array = np.array(my_list)

print(my_list)
print(my_array)
print(type(my_list))
print(type(my_array))

# Accessing Elements
print(my_list[0])
print(my_array[0])
