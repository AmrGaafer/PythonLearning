# --------------------------------------------------------------------------------------------------
# Object Oriented Programming (OOP):
#   Definition: paradigm or coding style
#
#   Paradigm:   structuring a programm so the Methods (Functions) and Attributes (Data or Property)
#               are bundled into Objects
#   Methods:    act as Fuction that use the information of the Object
#   Attributes: act as Object properties
#   Class:      template for creating Objects (Object constructor or Blueprint)
#   - OOP allows to organize code and make it readable und reusable
#
# Programming languages paradigms: (OOP, Procedual, Functional)
#   Procedual:  structure app like recipe, sets the steps to make the task
#   Functional: built on the concept of mathematical functions
#
# Python supports multi-language paradigms and consequently supports OOP
# Everything in Python is an object
# --------------------------------------------------------------------------------------------------
# Class Syntax and info:
#   Definition: Blueprint or constructor of the object, defined with the keyword class
#
#   Class name should be written in PascalCase (UpperCamelCase) style
#   Class instantiate means instance creation of a class
#   Instance:   it has the class' attributes and methods
#   By creating a class object, Python looks for the built-in method __init__
#       __init__ method is called everytime an instance is created (class constructor)
#       __init__ method initializes the date of an object
#   within the class 'self' refers to the current instance of the class
#   'self' can be named anything
#
#   Instance Attributes:
#       defined within the constructor
#   Class Attributes:
#       defined outside the constructor
#
#   Instance Methods:
#       take 'self' parameter which points to the instance created
#       can have more than one input parameter (like any function)
#       can freely access the class' attributes, other methods and class itself
#   Class Methods:
#       marked with @classmethod decorator to flag it as a class method
#       it takes 'cls' paramter not 'self' to point to the class not the instance
#       does not need class instantiation
#       used to do something in the class itself not the instances
#   Static Methods:
#       marked with @staticmethod decorator to flag it as a static method
#       it takes no parameters
#       it bounds to the class not the instance
#       used when doing something without class or object access, but related to the class
#   Magic Methods:
#       self.__class__ returns the class name of the instance
#       __str__ gives a human-readable output of the object
#               if it is not edited within the class,
#               the default return is the class name and the instance memory address
#       __len__ returns the length of the container
#               called when the built-in function len() is called on the object
#
#   Syntax:
#       class ClassName:
#           class attributes
#
#           def __init__(self,...):
#               ...
#               instance attributes initialzation using class constructor
#               ...
#
#           def get/set_instance_methods(self,...):
#               ...
#
#           @classmethod
#           def my_class_method(cls):
#               ...
#
#   NOTE: Methods with two underscore in the start and the end are called Dunder or Magic Method
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('OOP Basics:\n')

class Member:
    not_allowed_names = ['hell', 'shit', 'stupid']      # class atribute
    users_count = 0                                     # class atribute
    
    @classmethod
    def show_users_count(cls):                          # class method
        print(f'There is/are {cls.users_count} user(s)')
    
    @staticmethod
    def say_hello():                                    # static method
        print('Hello from a static method!')
    
    def __init__(self, first_name, middle_name, last_name, gender):
        self.first_name =   first_name if first_name not in Member.not_allowed_names else 'NA'
        self.middle_name =  middle_name if middle_name not in Member.not_allowed_names else 'NA'
        self.last_name =    last_name if last_name not in Member.not_allowed_names else 'NA'
        self.gender =       gender
        Member.users_count += 1
    
    def get_full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    
    def get_name_with_title(self):
        if self.gender == 'm':
            return f'Hello Mr. {self.first_name}'
        elif self.gender == 'f':
            return f'Hello Ms./Mrs. {self.first_name}'
        else:
            return f'Hello {self.first_name}'
    
    def get_all_info(self):
        return f'{self.get_name_with_title()}, your full name is {self.get_full_name()}'

# class testing:
Member.say_hello()
Member.show_users_count()
print('Number of users= ', Member.users_count)

member1 = Member('Amr', 'Wael', 'Gaafer', 'm')
member2 = Member('Wael', 'Ali', 'Gaafer', 'm')
member3 = Member('Lina', 'Amr', 'Gaafer', 'f')
member4 = Member('hell', 'shit', 'stupid', '-')

print(dir(member1))
print(member1.__class__)

print(member1.first_name)
print(member2.first_name)
print(member3.first_name)

print(member1.get_full_name())          # = print(Member.get_full_name(member1))
print(member1.get_name_with_title())
print(member1.get_all_info())
print(member2.get_full_name())
print(member2.get_name_with_title())
print(member2.get_all_info())
print(member3.get_full_name())
print(member3.get_name_with_title())
print(member3.get_all_info())
print(member4.get_full_name())
print(member4.get_name_with_title())
print(member4.get_all_info())

Member.show_users_count()
print('Number of users= ', Member.users_count)

class Skill():
    def __init__(self):
        self.skills = ['PLC', 'Cpp', 'Python']
    def __str__(self):
        return f'my skills are {self.skills}'
    def __len__(self):
        return len(self.skills)

profile = Skill()
print(profile.__class__)
print(profile)          # reflects __str__ return
print(len(profile))     # reflects __len__ return

profile.skills.append('MySQL')
print(profile)          # reflects __str__ return
print(len(profile))     # reflects __len__ return
