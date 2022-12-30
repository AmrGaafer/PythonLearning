# --------------------------------------------------------------------------------------------------
# Inheritance:
#   concept of inheritance of a base/parent class to a derived class
#
#   - by defult inherits the derived class all the base class attributes and methods
#     (including the __init__() constructor)
#   - Method Override: if a method from the base class is re-defined in the derived class,
#     the derived calss' definition overrides the base class' definition
#
#   - derived class constructor __init__() overrides the base class constructor
#     to overcome this limitation: call the base class constructor within the derived class constructor
#       BaseClass.__init__(self, inherited_attributes)
#       OR
#       super().__init__(inherited_attributes)
#
#   Syntax:
#       def BaseClass:
#           def __init__(self,...):
#               ...
#           class body
#
#       def DerivedClass(BaseClass):
#           def __init__(self,...):
#               BaseClass.__init__(self,...) | super().__init__(...)
#           class body
#
# Multiple Inheritance:
#   the concept of inheritance of multiple base/parent classes to a derived class
#
#   Syntax:
#       def BaseClass1:
#           def __init__(self,...):
#               ...
#           class body
#
#       def BaseClass2:
#           def __init__(self,...):
#               ...
#           class body
#
#       def DerivedClass(BaseClass1, BaseClass2):
#           class body
#
# NOTE: Class.mro() returns the method resolution order (the order of class executions)
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Inheritance:\n')

class Food:                 # base class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f'{self.name} is created from base class')
    
    def eat(self):
        print('eat method from base class')

class Apple(Food):          # derived class
    def __init__(self, name, price, amount):
        #Food.__init__(self, name)   # create an instance from base class
        super().__init__(name, price)
        self.amount = amount
        print(f'{self.name} is created from derived class, its price is {self.price} and there is {self.amount}')
    
    def eat(self):
        print('eat method from derived class')
    
    def get_from_tree(self):
        print('get from tree from derived class')

food_1 = Food('Pizza', 15)
food_2 = Apple('Apple', 20, 5)
food_2.eat()
food_2.get_from_tree()

print('\n# ********************************************* #')
print('Multiple Inheritance:\n')

class BaseOne:
    def __init__(self):
        print('base one')
    def func_one(self):
        print('one')

class BaseTwo:
    def __init__(self):
        print('base one')
    def func_two(self):
        print('one')

class Derived(BaseOne, BaseTwo):
    pass

my_var = Derived()
print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

# Multiple inheritance model#2
class Base:
    pass

class DerivedOne(Base):
    pass

class DerivedTwo(DerivedOne):
    pass
