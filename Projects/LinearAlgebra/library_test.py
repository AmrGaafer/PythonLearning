# --------------------------------------------------------------------------------------------------
# Linear Algebra Library Testing
# Developer:    Amr Gaafer
# Date:         TBD
# --------------------------------------------------------------------------------------------------

import os
import sys
sys.path.append('C:/Users/Gerd1/Desktop/GitHub/PythonLearning/Projects/LinearAlgebra/LinearAlgebraLibrary')

from linear_algebra import Vector
import linear_algebra

os.system('cls')        # cls command


my_vector = Vector([8.218, -9.341])
my_vector2 = Vector([-1.129, 2.111])

print(my_vector.__str__())
print(my_vector2.__str__())
print(my_vector == my_vector2)

# vector_add() test:
my_vector =  Vector([8.218, -9.341])
my_vector2 = Vector([-1.129, 2.111])
print('vectors add: ', linear_algebra.vector_add(my_vector, my_vector2))

# vector_sub() test:
my_vector =  Vector([7.119, 8.215])
my_vector2 = Vector([-8.223, 0.878])
print('vectors subtract: ', linear_algebra.vector_sub(my_vector, my_vector2))

# vector_scale() test:
my_vector =  Vector([1.671, -1.012, -0.318])
print('vector scale: ', linear_algebra.vector_scale(my_vector, 7.41))

# vector_magnitude() test:
my_vector =  Vector([-0.221, 7.437])
my_vector2 = Vector([8.813, -1.331, -6.247])
print('vector magnitude: ', linear_algebra.vector_magnitude(my_vector))
print('vector magnitude: ', linear_algebra.vector_magnitude(my_vector2))

# vector_direction() test:
my_vector =  Vector([5.581, -2.136])
my_vector2 = Vector([1.996, 3.108, -4.554])
print('vector direction: ', linear_algebra.vector_direction(my_vector))
print('vector direction: ', linear_algebra.vector_direction(my_vector2))

# vector_dot_product() test:
my_vector =  Vector([7.887, 4.138])
my_vector2 = Vector([-8.802, 6.776])
print('vectors dot product: ', linear_algebra.vector_dot_product(my_vector, my_vector2))
my_vector =  Vector([-5.955, -4.904, -1.874])
my_vector2 = Vector([-4.496, -8.755, 7.103])
print('vectors dot product: ', linear_algebra.vector_dot_product(my_vector, my_vector2))

# vector_angle_rad() test:
my_vector =  Vector([3.183, -7.627])
my_vector2 = Vector([-2.668, 5.319])
print('angle in rad: ', linear_algebra.vector_angle_rad(my_vector, my_vector2))

# vector_angle_degree() test:
my_vector =  Vector([7.35, 0.221, 5.188])
my_vector2 = Vector([2.751, 8.259, 3.985])
print('angle in degree: ', linear_algebra.vector_angle_degree(my_vector, my_vector2))
