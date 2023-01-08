# --------------------------------------------------------------------------------------------------
# Linear Algebra Library Testing
# Developer:    Amr Gaafer
# Date:         08.01.2023
# --------------------------------------------------------------------------------------------------

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/LinearAlgebraLibrary')
from linear_algebra import Vector
import linear_algebra

os.system('cls')        # cls command

# vectors equality test:
my_vector =  Vector([8.218, -9.341])
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

# vector_is_parallel() & vector_is_orthogonal() test:
my_vector =  Vector([-7.579, -7.88])
my_vector2 = Vector([22.737, 23.64])
print('vectors parallel: ', linear_algebra.vector_is_parallel(my_vector, my_vector2))
print('vectors parallel: ', linear_algebra.vector_is_orthogonal(my_vector, my_vector2))
my_vector =  Vector([-2.029, 9.97, 4.172])
my_vector2 = Vector([-9.231, -6.639, -7.245])
print('vectors parallel: ', linear_algebra.vector_is_parallel(my_vector, my_vector2))
print('vectors parallel: ', linear_algebra.vector_is_orthogonal(my_vector, my_vector2))
my_vector =  Vector([-2.328, -7.284, -1.214])
my_vector2 = Vector([-1.821, 1.072, -2.94])
print('vectors parallel: ', linear_algebra.vector_is_parallel(my_vector, my_vector2))
print('vectors parallel: ', linear_algebra.vector_is_orthogonal(my_vector, my_vector2))
my_vector =  Vector([2.118, 4.827])
my_vector2 = Vector([0, 0])
print('vectors parallel: ', linear_algebra.vector_is_parallel(my_vector, my_vector2))
print('vectors parallel: ', linear_algebra.vector_is_orthogonal(my_vector, my_vector2))

# vector_projection() & vector_orthogonal() test:
my_vector =  Vector([3.039, 1.879])
my_vector2 = Vector([0.825, 2.036])
print('vectors projection: ', linear_algebra.vector_projection(my_vector, my_vector2))
print('vectors orthogonal: ', linear_algebra.vector_orthogonal(my_vector, my_vector2))
my_vector =  Vector([-9.88, -3.264, -8.159])
my_vector2 = Vector([-2.155, -9.353, -9.473])
print('vectors projection: ', linear_algebra.vector_projection(my_vector, my_vector2))
print('vectors orthogonal: ', linear_algebra.vector_orthogonal(my_vector, my_vector2))
my_vector =  Vector([3.009, -6.172, 3.692, -2.51])
my_vector2 = Vector([6.404, -9.144, 2.759, 8.718])
print('vectors projection: ', linear_algebra.vector_projection(my_vector, my_vector2))
print('vectors orthogonal: ', linear_algebra.vector_orthogonal(my_vector, my_vector2))

# vector_cross_product() test:
my_vector =  Vector([5, 3, -2])
my_vector2 = Vector([-1, 0, 3])
print('vectors cross product: ', linear_algebra.vector_cross_product(my_vector, my_vector2))
my_vector =  Vector([8.462, 7.893, -8.187])
my_vector2 = Vector([6.984, -5.975, 4.778])
print('vectors cross product: ', linear_algebra.vector_cross_product(my_vector, my_vector2))

# vector_parallelogram_area() test:
my_vector =  Vector([5, 3, -2])
my_vector2 = Vector([-1, 0, 3])
print('parallelogram area: ', linear_algebra.vector_parallelogram_area(my_vector, my_vector2))
my_vector =  Vector([-8.987, -9.838, 5.031])
my_vector2 = Vector([-4.268, -1.861, -8.866])
print('parallelogram area: ', linear_algebra.vector_parallelogram_area(my_vector, my_vector2))

# vector_triangle_area() test:
my_vector =  Vector([5, 3, -2])
my_vector2 = Vector([-1, 0, 3])
print('triangle area: ', linear_algebra.vector_triangle_area(my_vector, my_vector2))
my_vector =  Vector([1.5, 9.547, 3.691])
my_vector2 = Vector([-6.007, 0.124, 5.772])
print('triangle area: ', linear_algebra.vector_triangle_area(my_vector, my_vector2))
