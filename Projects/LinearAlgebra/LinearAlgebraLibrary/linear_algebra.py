# --------------------------------------------------------------------------------------------------
# Linear Algebra User-defined Library 
# Developer:    Amr Gaafer
# Date          06.01.2023
# --------------------------------------------------------------------------------------------------
'''
Linear Algebra User-defined Library:

'''

import os
from vector import Vector
os.system('cls')        # cls command

def vectors_check(fn):
    def wrapper(A, B):
        if isinstance(A, Vector) and isinstance(B, Vector) and len(A) == len(B):
            fn(A, B)
        elif isinstance(A, Vector) and isinstance(B, Vector) and len(A) != len(B):
            raise ValueError('')
        else:
            raise ValueError('the input arguments have to be vectors!')
    return wrapper

#@vectors_check
def vector_add(A, B):
    return Vector([a+b for a, b in zip(A.coordinates, B.coordinates)])
