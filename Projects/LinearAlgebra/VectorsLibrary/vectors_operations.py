# --------------------------------------------------------------------------------------------------
# Linear Algebra User-defined Library - Vectors Operations
# Developer:    Amr Gaafer
# Date:         08.01.2023
# --------------------------------------------------------------------------------------------------
'''
Linear Algebra User-defined Library - Vectors Operations:
    Vectors Basic Operations:
        01. vector_add(vector1, vector2)
        02. vector_sub(vector1, vector2)
        03. vector_scale(vector, scale)
    Vector Basis Properties:
        04. vector_magnitude(vector)
        05. vector_direction(vector)
    Vectors Dot Product:
        06. vector_dot_product(vector1, vector2)
        07. vector_angle_rad(vector1, vector2)
        08. vector_angle_degree(vector1, vector2)
        09. vector_is_parallel(vector1, vector2)
        10. vector_is_orthogonal(vector1, vector2)
        11. vector_projection(vector1, vector2)
        12. vector_orthogonal(vector1, vector2)
    Vectors Cross Product:
        13. vector_cross_product(vector1, vector2)
        14. vector_parallelogram_area(vector1, vector2)
        15. vector_triangle_area(vector1, vector2)
'''

import os
from math import pi, acos, isclose
from vector import Vector
os.system('cls')        # cls command

###################################### Data Check Decorators ######################################
# decorator function to check the date types of the functions with input vectors
def vectors_check(fun):
    def wrapper(*vectors):
        elements_length = []
        for vector in vectors:
            if isinstance(vector, Vector):
                elements_length.append(len(vector))
            else:
                raise ValueError('the input argument(s) must be vector(s)!')
        if len(set(elements_length)) != 1:
            raise ValueError('the input arguments must have the same dimension!')
        return fun(*vectors)
    return wrapper

# decorator function to check the date types of the functions with input vector ans scaling
def vector_check(fun):
    def wrapper(vector, scale):
        if isinstance(vector, Vector):
            return fun(vector, scale)
        raise ValueError('the input argument(s) must be vector(s)!')
    return wrapper

######################################## Library Functions ########################################

@vectors_check
def vector_add(A, B):
    return Vector([a+b for a, b in zip(A.coordinates, B.coordinates)])

@vectors_check
def vector_sub(A, B):
    return Vector([a-b for a, b in zip(A.coordinates, B.coordinates)])

@vector_check
def vector_scale(A, scale):
    return Vector([scale*a for a in A.coordinates])

@vectors_check
def vector_magnitude(A):
    return sum(a**2 for a in A.coordinates)**0.5

def vector_direction(A):
    if vector_magnitude(A) != 0:
        return vector_scale(A, 1/vector_magnitude(A))
    return A

@vectors_check
def vector_dot_product(A, B):
    return sum(a*b for a, b in zip(A.coordinates, B.coordinates))

@vectors_check
def vector_angle_rad(A, B):
    if vector_magnitude(A) != 0 and vector_magnitude(B) != 0:
        return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))
    return 0.0

@vectors_check
def vector_angle_degree(A, B):
    if vector_magnitude(A) != 0 and vector_magnitude(B) != 0:
        return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))*180/pi
    return 0.0

def vector_is_parallel(A, B):
    return isclose(abs(vector_dot_product(A, B)), vector_magnitude(A) * vector_magnitude(B),
                   abs_tol= 1e-7)

def vector_is_orthogonal(A, B):
    return isclose(vector_dot_product(A, B), 0.0, abs_tol= 1e-7)

def vector_projection(A, B):
    return vector_scale(vector_direction(B), vector_dot_product(A, vector_direction(B)))

def vector_orthogonal(A, B):
    return vector_sub(A, vector_projection(A, B))

@vectors_check
def vector_cross_product(A, B):
    if len(A) != 3 or len(B) != 3:
        raise ValueError('the input vectors have to be 3-D vectors!')
    return Vector([A.coordinates[1]*B.coordinates[2]-A.coordinates[2]*B.coordinates[1],
                   -(A.coordinates[0]*B.coordinates[2]-A.coordinates[2]*B.coordinates[0]),
                   A.coordinates[0]*B.coordinates[1]-A.coordinates[1]*B.coordinates[0]])

def vector_parallelogram_area(A, B):
    return vector_magnitude(vector_cross_product(A, B))

def vector_triangle_area(A, B):
    return 0.5 * vector_parallelogram_area(A, B)

########################################## Library Tests ##########################################

print('Vectors Operations Test:')
if __name__ == '__main__':
    # vectors equality test:
    my_vector =  Vector([8.218, -9.341])
    my_vector2 = Vector([-1.129, 2.111])
    print(my_vector.__str__())
    print(my_vector2.__str__())
    print(my_vector == my_vector2)

    # vector_add() test:
    my_vector =  Vector([8.218, -9.341])
    my_vector2 = Vector([-1.129, 2.111])
    print('vectors add: ', vector_add(my_vector, my_vector2))

    # vector_sub() test:
    my_vector =  Vector([7.119, 8.215])
    my_vector2 = Vector([-8.223, 0.878])
    print('vectors subtract: ', vector_sub(my_vector, my_vector2))

    # vector_scale() test:
    my_vector =  Vector([1.671, -1.012, -0.318])
    print('vector scale: ', vector_scale(my_vector, 7.41))

    # vector_magnitude() test:
    my_vector =  Vector([-0.221, 7.437])
    my_vector2 = Vector([8.813, -1.331, -6.247])
    print('vector magnitude: ', vector_magnitude(my_vector))
    print('vector magnitude: ', vector_magnitude(my_vector2))

    # vector_direction() test:
    my_vector =  Vector([5.581, -2.136])
    my_vector2 = Vector([1.996, 3.108, -4.554])
    print('vector direction: ', vector_direction(my_vector))
    print('vector direction: ', vector_direction(my_vector2))

    # vector_dot_product() test:
    my_vector =  Vector([7.887, 4.138])
    my_vector2 = Vector([-8.802, 6.776])
    print('vectors dot product: ', vector_dot_product(my_vector, my_vector2))
    my_vector =  Vector([-5.955, -4.904, -1.874])
    my_vector2 = Vector([-4.496, -8.755, 7.103])
    print('vectors dot product: ', vector_dot_product(my_vector, my_vector2))

    # vector_angle_rad() test:
    my_vector =  Vector([3.183, -7.627])
    my_vector2 = Vector([-2.668, 5.319])
    print('angle in rad: ', vector_angle_rad(my_vector, my_vector2))

    # vector_angle_degree() test:
    my_vector =  Vector([7.35, 0.221, 5.188])
    my_vector2 = Vector([2.751, 8.259, 3.985])
    print('angle in degree: ', vector_angle_degree(my_vector, my_vector2))

    # vector_is_parallel() & vector_is_orthogonal() test:
    my_vector =  Vector([-7.579, -7.88])
    my_vector2 = Vector([22.737, 23.64])
    print('vectors parallel: ', vector_is_parallel(my_vector, my_vector2))
    print('vectors parallel: ', vector_is_orthogonal(my_vector, my_vector2))
    my_vector =  Vector([-2.029, 9.97, 4.172])
    my_vector2 = Vector([-9.231, -6.639, -7.245])
    print('vectors parallel: ', vector_is_parallel(my_vector, my_vector2))
    print('vectors parallel: ', vector_is_orthogonal(my_vector, my_vector2))
    my_vector =  Vector([-2.328, -7.284, -1.214])
    my_vector2 = Vector([-1.821, 1.072, -2.94])
    print('vectors parallel: ', vector_is_parallel(my_vector, my_vector2))
    print('vectors parallel: ', vector_is_orthogonal(my_vector, my_vector2))
    my_vector =  Vector([2.118, 4.827])
    my_vector2 = Vector([0, 0])
    print('vectors parallel: ', vector_is_parallel(my_vector, my_vector2))
    print('vectors parallel: ', vector_is_orthogonal(my_vector, my_vector2))

    # vector_projection() & vector_orthogonal() test:
    my_vector =  Vector([3.039, 1.879])
    my_vector2 = Vector([0.825, 2.036])
    print('vectors projection: ', vector_projection(my_vector, my_vector2))
    print('vectors orthogonal: ', vector_orthogonal(my_vector, my_vector2))
    my_vector =  Vector([-9.88, -3.264, -8.159])
    my_vector2 = Vector([-2.155, -9.353, -9.473])
    print('vectors projection: ', vector_projection(my_vector, my_vector2))
    print('vectors orthogonal: ', vector_orthogonal(my_vector, my_vector2))
    my_vector =  Vector([3.009, -6.172, 3.692, -2.51])
    my_vector2 = Vector([6.404, -9.144, 2.759, 8.718])
    print('vectors projection: ', vector_projection(my_vector, my_vector2))
    print('vectors orthogonal: ', vector_orthogonal(my_vector, my_vector2))

    # vector_cross_product() test:
    my_vector =  Vector([5, 3, -2])
    my_vector2 = Vector([-1, 0, 3])
    print('vectors cross product: ', vector_cross_product(my_vector, my_vector2))
    my_vector =  Vector([8.462, 7.893, -8.187])
    my_vector2 = Vector([6.984, -5.975, 4.778])
    print('vectors cross product: ', vector_cross_product(my_vector, my_vector2))

    # vector_parallelogram_area() test:
    my_vector =  Vector([5, 3, -2])
    my_vector2 = Vector([-1, 0, 3])
    print('parallelogram area: ', vector_parallelogram_area(my_vector, my_vector2))
    my_vector =  Vector([-8.987, -9.838, 5.031])
    my_vector2 = Vector([-4.268, -1.861, -8.866])
    print('parallelogram area: ', vector_parallelogram_area(my_vector, my_vector2))

    # vector_triangle_area() test:
    my_vector =  Vector([5, 3, -2])
    my_vector2 = Vector([-1, 0, 3])
    print('triangle area: ', vector_triangle_area(my_vector, my_vector2))
    my_vector =  Vector([1.5, 9.547, 3.691])
    my_vector2 = Vector([-6.007, 0.124, 5.772])
    print('triangle area: ', vector_triangle_area(my_vector, my_vector2))
