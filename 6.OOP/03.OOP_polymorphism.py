# --------------------------------------------------------------------------------------------------
# Plymorphism:
#   concept of many forms of the same method. The method has many definitions
#   HINT: to force the developer to implement a pre-defined method from the base class
#
#   in the derived class, raise an exception in the base class definition
#       raise NotImplementedError('Derived class must implement this method')
#   in this case, the method is like an abstract method
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Polymorphism:\n')

# example of '+' opertor:
n1, n2 = 10, 20
print(n1 + n2)
s1, s2 = 'Hello', 'Python'
print(s1 + s2)

# example of len function:
print(len([1, 2, 3]))
print(len('Gaafer'))

# example on classes:
class A:
    def do_something(self):
        print('from class A')
        raise NotImplementedError('Derived class must implement this method')

class B(A):
    def do_something(self):
        print('from class B')

class C(A):
    def do_something(self):
        print('from class C')

my_instance = B()
my_instance.do_something()
