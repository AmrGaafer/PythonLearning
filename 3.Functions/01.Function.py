# -------------------------------------------------------------------------------------------------------------
# Functions: resuable block of code and does a certain task
#   - run when they are called
#   - parameter is the variable listed inside the parentheses in the function definition
#   - argument is the value that are sent to the function when it is called
#   - can return data when the routine is done / can perform a task without returning data
#   - pervent DRY (Don't Repeat Yourself)
#   - there are Built-in functions and user-defined functions
#   Syntax:
#       def functionName(argument(s)/parameter(s)):
#           Function body
#       - passing the value(s) to the arguments in two ways:
#           a. by position: the sequence of the arguments passing may differ than the defualt definition
#           b. by value:    the sequence of the arguments passing has to be similar to the defualt definition
#
#   NOTE: method is a function that is called using dot (.) opertator
#         e.g. string.capitalize()
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

def function_name():        # function without return data
    print('Hello World from a function without a return!')

function_name()

def function_name2():       # function with return data
    return 'Hello World from a finction with a return!'

text = function_name2()
print(text)

def say_hello(firstName, SecondName, LastName):
    print(f"Hello {firstName.strip().capitalize()} {SecondName.strip().capitalize():.1s}. {LastName.strip().capitalize()} from a function!")

# function call and passing arguments by value
say_hello("amr", "wael", "gaafer")
# function call and passinf arguments by position
say_hello(SecondName= 'wael', firstName= 'amr', LastName= 'gaafer')

def addition(a, b):
    if type(a) != int or type(b) != int:
        print('Only integers are allowed')
    else:
        return a + b

print(addition(4, 6))
print(addition("Amor", 6))  # None

# -------------------------------------------------------------------------------------------------------------
# Function documentation (Docstring):
#   Type of comment to explain the purpose of a function, module or class and how it should be used
#   It can be accessed from the help or Doc attributes (e.g. functionName.__doc__)
#   It can be a single line or multiple lines string
#   Syntax:
#       def functionName(arg1, arg2,...)
#           ''' single line function purpose explaination.
#           INPUT:
#               arg1: type. description
#               arg2: type. description
#               ...
#           OUTPUT:
#               description
#           '''
#           Function body
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function documentation (Docstring):\n')

def hi(s):
    '''saying hi
    Input:
    s: str. the name to be greated
    Output:
    message in title form'''
    return f'Hi {s.strip().title()}'

print(hi('  aMr  '))
help(hi)    # equivalent to hi.__doc__

# -------------------------------------------------------------------------------------------------------------
# Function default parameter(s)
#   The assignment operator (=) is used at the function definition header
#   Syntax:
#       def functionName(argument = default_value):
#           Function body
#   NOTE: the parameter with a default value can not be followed with other parameters without default value
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function default parameter(s):\n')

def say_hello(name = "unknown", age ="unknown", country ="unknown"):
    print(f'Hi {name.strip().capitalize()}, you are {age} years old and you are from {country}')

say_hello("amr", 34, "Egypt")
say_hello("HAitham", 28)
say_hello("nancY")
say_hello()

# -------------------------------------------------------------------------------------------------------------
# Function scope
#   there are two scopes: global scope and local scope
#   1. Global scope is outside the function
#   2. Local scope is inside the function
#       - locally defined varialbes are not callable form outside its scope
#       - to define a variable within the local (function) scope as a global scope variable
#           => add the word "global" before the variable name and in another line assign the value
#       - function can still access the value of the global variable(s) within the function,
#         however, the value of a global variable can not be modified inside the function
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function Scope:\n')

x = 1 # global scope
def zero():
    print(f'print from the fuction "zero" scope: {x}')
def one():
    x = 2
    print(f'print from the fuction "one" scope: {x}')
def two():
    global x    # overriding the previous global definition
    x = 4       # overriding the previous global value
    print(f'print from the fuction "two" scope: {x}')

zero()
print(f'print from the golbal scope: {x}')
one()
print(f'print from the golbal scope: {x}')
two()
print(f'print from the golbal scope: {x}')

# -------------------------------------------------------------------------------------------------------------
# Function Recursion
#   a function is called to be a recursive function if it calls itself from inside
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function Recursion:\n')

print('Example1:')
def factorial(x):
    return x * factorial(x-1) if x > 0 else 1

print(factorial(5))
print(factorial(2))
print(factorial(1))
print(factorial(0))

print('\nExample2:')
def cleanWord(txt):     # solution without function recursion
    prevChar = ''
    cleanedTxt = ''
    for char in txt:
        if char != prevChar:
            cleanedTxt = cleanedTxt + char
        prevChar = char
    return cleanedTxt

def cleanWord2(txt):    # solution with function recursion
    if len(txt) > 1:
        if txt[0] == txt[1]:
            return cleanWord2(txt[1:])          # ignore the duplicate character and test the rest
        else:
            return txt[0]+cleanWord2(txt[1:])   # consider that character and test the rest
    else:
        return txt

print(cleanWord('WWWooooooorrrrldd'))
print(cleanWord2('WWWooooooorrrrldd'))

# -------------------------------------------------------------------------------------------------------------
# Function packing and unpacking arguments (*Args)
#   the asterisk (*) operator before the argument unpacks the arguments (all iterables except dictionary)
#   Syntax:
#       def functionName(*argument):    # unpacks all the arguments in a tuple
#           Function body
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function packing and unpacking arguments (*Arguments):\n')

def print_list(*x):                     # unpacks the arguments and prints each single argument
    print(x)

def say_hello(name, *friends):          # unpacks all the arguments
    print(friends, end = ' ')
    print(f'is type: {type(friends)}')  # tuple
    print(name.strip().capitalize() + ' has this/these friend(s):')
    for member in friends:              # unpacks all the arguments
        print(f'{friends.index(member)+1}. {member.strip().capitalize()}')

def spell_word(*word):
    word_len = len(word)
    for char in word:
        if word.index(char) != word_len-1:
            print(char, end = ' - ')
        else:
            print(char)

# function call with arguments
print_list(34,"Do you like Python?", "Of course")

myList = [' hammam  ', 'shoka', '  sadek', 'ashraf']
print(myList)
print(*myList)      # asterisk operator unpacks the list
# function call with arguments
say_hello('Amr', ' hammam  ', 'shoka', '  sadek', 'ashraf')
# function call with parameters
say_hello('Amr', *myList)

myWord = 'Amor'
print(myWord)
print(*myWord)
# function call with arguments
spell_word('A', 'm', 'o', 'r')
# function call with parameters
spell_word(*myWord)

# -------------------------------------------------------------------------------------------------------------
# Function packing and unpacking arguments (**KWArgs)
#   the double asterisk (**) operator before the argument unpacks the dictionary
#   Syntax:
#       def functionName(**argument dictionary):    # unpacks all the arguments in a tuple
#           Function body
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function packing and unpacking keyword arguments (**Keyword Arguments (Dictionary)):\n')

def show_skills(**skills):
    print(type(skills))
    for key, value in skills.items():
        print(f'Skill: {key} is achieved with {value}%')

myDictionary = {'C++': 50, 'Python': 30, 'PLC': 82}
print(myDictionary)
# print(**myDictionary)
# function call with parameters
show_skills(**myDictionary)

print('\nExercise on packing and unpacking:\n')
def show_skills(name, *skills, **skillsDictionary):
    print(f'Hello {name}, you want to learn the following skills:')
    for skill in skills:
        if skill != skills[-1]:
            print(f'{skill}', end = ', ')
        else:
            print(f'{skill}')
    
    print('You have achieved these skills with a certain progress:')
    for key, value in skillsDictionary.items():
        print(f'Skill: {key} is achieved with {value}%')

# function call with arguments
show_skills('Amr', 'Machine Learning', 'SQL', 'Command line', Cpp= 50, Python= 30, PLC= 82)

# function call with parameters
mySkillsWish = ['Machine Learning', 'SQL', 'Command line']
mySkillsDictionary = {'C++': 50, 'Python': 30, 'PLC': 82}
show_skills('Amr', *mySkillsWish, **mySkillsDictionary)

# -------------------------------------------------------------------------------------------------------------
# Function Lambda (anonymous function) - function on the fly
#   - has no name
#   - can be called inline wihout pre-defining
#   - can be used in the return of another function
#   - used for simple functions, for large tasks define a normal function
#   - is a single expression not a block of code
#   - Lambda type is Function
#   Syntax:
#       variable = lambda input_parameter(s) : line of code using the input_parameter(s)
#           this variable has the type <class 'function'>
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('Function Lambda:\n')

# normal function inline definition
def say_hello(name, age): return(f"Hello {name}! Your age is {age} years old")
print(type(say_hello))
# lambda function
hello = lambda name, age: f"Hello {name}! Your age is {age} years old"
print(type(hello))

print(say_hello("Amr", 34))
print(hello("Amr", 34))

print(say_hello.__name__)       # function name
print(hello.__name__)           # function name (lambda)
