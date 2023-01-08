# --------------------------------------------------------------------------------------------------
# Linear Algebra User-defined Library 
# Developer:    Amr Gaafer
# Date:         08.01.2023
# --------------------------------------------------------------------------------------------------
'''
Linear Algebra User-defined Library:
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
from vector import Vector
from math import pi, acos, isclose
os.system('cls')        # cls command

###################################### Data Check Decorators ######################################
# decorator function to check the date types of the functions with input vectors
def vectors_check(fn):
    def wrapper(*vectors):
        elements_length = []
        for v in vectors:
            if isinstance(v, Vector):
                elements_length.append(len(v))
            else:
                raise ValueError('the input argument(s) must be vector(s)!')
        if len(set(elements_length)) != 1:
            raise ValueError('the input arguments must have the same dimension!')
        else:
            return fn(*vectors)
    return wrapper

# decorator function to check the date types of the functions with input vector ans scaling
def vector_check(fn):
    def wrapper(vector, scale):
        if isinstance(vector, Vector):
            return fn(vector, scale)
        else:
            raise ValueError('the input argument(s) must be vector(s)!')
    return wrapper

######################################## Library Functions ########################################

#*************************************** Vectors Operations **************************************#
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
    else:
        return A

@vectors_check
def vector_dot_product(A, B):
    return sum(a*b for a, b in zip(A.coordinates, B.coordinates))

@vectors_check
def vector_angle_rad(A, B):
    if vector_magnitude(A) != 0 and vector_magnitude(B) != 0:
        return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))
    else:
        return 0.0

@vectors_check
def vector_angle_degree(A, B):
    if vector_magnitude(A) != 0 and vector_magnitude(B) != 0:
        return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))*180/pi
    else:
        return 0.0

def vector_is_parallel(A, B):
    return isclose(abs(vector_dot_product(A, B)), vector_magnitude(A) * vector_magnitude(B), abs_tol= 1e-7)

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
