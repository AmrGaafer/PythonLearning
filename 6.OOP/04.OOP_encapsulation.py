# --------------------------------------------------------------------------------------------------
# Encapsulation:
#   access restriction to the data stored in attributes and methods
#   Public [default]:
#       attributes and methods can be called or modified from everywhere (inside and outside class)
#   Protected:
#       attributes and methods can be accessed from within the class and sub-classes (derived classes)
#       Syntax: protected attributes and methods start with prefis one underscore '_'
#   Private:
#       attributes and methods can be accessed from within the class or object only
#       attributes and methods can not be modified from outside the class
#       Syntax: protected attributes and methods start with prefis two underscores '__'
#       - to access a private member '__dummy', it could be called by the syntax '_ClassName__dummy'
#
# NOTE: the restrictions proposed at the protected and private access are conventional,
#       this means the developer can ovveride these limitations in the code!!
#       In other words the underscore notation is just a naming convention for the developer
#       and does not actually restrict the developer in the code!!
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Encapsulation:\n')

# public
class Member:
    def __init__(self, name):
        self.name = name

one = Member('Amr')     # instantization
print(one.name)
one.name = 'Wael'       # modify
print(one.name)

# protected
class Member:
    def __init__(self, name):
        self._name = name

one = Member('Amr')     # instantization
print(one._name)
one._name = 'Wael'      # modify
print(one._name)

# private
class Member:
    def __init__(self, name):
        self.__name = name

one = Member('Amr')
#print(one.__name)       # no access on private member
print(one._Member__name)    # how to access private member

class Member:
    def __init__(self, name):
        self.__name = name
    def say_hello(self):
        return f'Hello {self.__name}'

one = Member('Amr')
#print(one.__name)
#one.__name = 'Wael'
#print(one.__name)
print(one.say_hello())
