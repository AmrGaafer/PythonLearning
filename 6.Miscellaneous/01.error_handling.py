# --------------------------------------------------------------------------------------------------
# Exceptions:
#   1. Exceptions are runtime error reporting mechanism
#   2. Exceptions give messages to understand the problem
#   3. Exceptions messages give traceback highlighting the line causing the error
#   4. Exceptions have many types (e.g. SyntaxError, IndexError, KeyError,... etc.)
#   Resource: https://docs.python.org/3/tutorial/errors.html
#             https://docs.python.org/3/library/exceptions.html
#
# Exceptions Raising using a user-defined exception (keyword raise):
#   Syntax: raise Exception('message')
#           raise Exception_Type('message')
#
# Exceptions Handling:
#   Syntax: 
#       try:
#           Test the code for errors
#       except ErrorType:
#           handle the errors (if error exists)
#       [Optional] else:
#           execute if no error exists
#       [Optional] finally:
#           run the code anyway
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Exception Raise:\n')

x = 10      # -10 causes Exception raising
if x < 0:
    raise Exception( 'Number is less than zero')

y = 10      # 'Amr' causes TypeError Exception raising
if not isinstance(y, int):
    raise TypeError('Type should be an integer')

print('\n# ********************************************* #')
print('Exception Handling:\n')

try:
    age = int(input('enter your age: '))
except:
    print('invalid age entry, it has to be an integer value')
else:
    print('good age entry')
finally:
    print('program end')

try:
    #print(10/0)
    #print(a)
    #print(int('Hi!'))
    pass
except ZeroDivisionError:
    print('ZeroDivisionError exception')
except NameError:
    print('identifier not found')
except:
    print('error catched')

my_file = None
tries = 5

while tries > 0:
    try:
        print('enter the file name with absolute path')
        print(f'number of remaining tries is: {tries}')
        print('(e.g) C:\Python_Test\MyFile.txt')
        file_name = input('File: ')
        my_file = open(file_name, mode= 'r')
        print(my_file.read())
        break
    except FileNotFoundError:
        print('invalid file name and path entry')
        tries -= 1
    except:
        print('error case triggered!')
    finally:
        if my_file is not None:
            my_file.close()
            print('file closed')
else:
    print('number of tries has been reached!...Sorry')
