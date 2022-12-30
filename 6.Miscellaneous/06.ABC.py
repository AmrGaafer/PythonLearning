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

import os
from abc import ABCMeta, abstractmethod
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('ABC:\n')

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
