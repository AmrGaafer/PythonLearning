# --------------------------------------------------------------------------------------------------
# Linear Algebra Library Testing
# Developer:    Amr Gaafer
# Date          06.01.2023
# --------------------------------------------------------------------------------------------------

import os
import sys
sys.path.append('C:/Users/Gerd1/Desktop/GitHub/PythonLearning/Projects/LinearAlgebra/LinearAlgebraLibrary')

from linear_algebra import Vector
import linear_algebra

os.system('cls')        # cls command


my_vector = Vector([1,2])
my_vector2 = Vector([1,2])

print(my_vector.__str__())
print(my_vector2.__str__())
print(my_vector == my_vector2)

my_vector3 = linear_algebra.vector_add(my_vector, my_vector2)
print(my_vector3)
