# --------------------------------------------------------------------------------------------------
# Inheritance:
#   concept of inheritance of a base/parent class to a derived class
#
#   - by defult the derived class inherits all the base class attributes and methods
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
        #Food.__init__(self, name, price)   # create an instance from base class
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
        print('base two')
    def func_two(self):
        print('two')

class Derived(BaseOne, BaseTwo):
    pass

print(Derived.mro())
my_var = Derived()

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

# --------------------------------------------------------------------------------------------------
# Abstract Base Class (ABC):
#   class is called an ABC class if it has one or more abstract methods
#       - abstract methods are to be led by @abstractmethod Decorator
#       - abstract methods should not be implemented in abstract class (use keyword pass)
#       - abstract methods should be implemented in implementing class(es),
#         otherwise an error is triggerd
#       - other methods in abstract class must not be implemented in implementing class(es)
#
#   Implementation:
#   abc module provides infrastructure for defining custom ABC
#   ABCMeta class (from abc module) is a meta-cass used for defining ABC
#
#   Syntax:
#       class AbstractClass(metaclass = ABCMeta):
#           @abstractmethod                     #Decorator on the methods
#           def abstract_method(self,...):
#               pass
# --------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Abstract Base Class (ABC):\n')

from abc import ABCMeta, abstractmethod 

class Programming(metaclass = ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
    def has_name(self):
        pass

class Python(Programming):
    def has_oop(self):
        return 'yes'

class Pascal(Programming):
    def has_oop(self):
        return 'no'

one = Python()
print(one.has_oop())
two = Pascal()
print(two.has_oop())
