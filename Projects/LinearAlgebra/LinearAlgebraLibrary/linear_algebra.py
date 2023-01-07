# --------------------------------------------------------------------------------------------------
# Linear Algebra User-defined Library 
# Developer:    Amr Gaafer
# Date:         TBD
# --------------------------------------------------------------------------------------------------
'''
Linear Algebra User-defined Library:
    1. vector_add(vector1, vector2)
    2. vector_sub(vector1, vector2)
    3. vector_scale(vector, scale)
    4. vector_magnitude(vector)
    5. vector_direction(vector)
    6. vector_dot_product(vector1, vector2)
'''

import os
from vector import Vector
from math import pi, acos
os.system('cls')        # cls command

###################### Data Check Decorators ######################
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


######################## Library Functions ########################
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
    return vector_scale(A, 1/vector_magnitude(A))

@vectors_check
def vector_dot_product(A, B):
    return sum(a*b for a, b in zip(A.coordinates, B.coordinates))

@vectors_check
def vector_angle_rad(A, B):
    return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))

@vectors_check
def vector_angle_degree(A, B):
    return acos(vector_dot_product(A, B) / (vector_magnitude(A) * vector_magnitude(B)))*180/pi
