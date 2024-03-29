# -------------------------------------------------------------------------------------------------------------
# Strings:
# 1. could be declared inside single quotes or double quotes
# 2. inside single quotes, the double quotes don't need Escape Character and vice verse
# 3. Concatenation is performed by using '+' or '*'
# 4. Triple single quotes or Triple double quotes:
#   a. are used for Multiple-line without '\n'
#   b. skip single and double quotes within
# NOTE: Strings in Python are immutable
#
# NOTE: Mutability: whether an object can change its values after it has been created
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('STRINGS:\n')
print('Amr ' + "Gaafer")
print('Amr ' * 5)

msg = '"I" love'
language = "'Python'"
print(msg + ' ' + language)

myString = '''"Amr"
'Sara'
"Haitham"'''
print(myString)

myString2 = """"Noha"
'Amir'
"Nancy" """
print(myString2)

myString3 = """
This
is
a
Multiple-line
string
"""
print(myString3)

# -------------------------------------------------------------------------------------------------------------
# Escape Sequence Characters:
# \b:   Backspace
# \↵:   Escape New Line
# \\:   Escape Backslash
# \':   Escape Single Quote
# \":   Escape Double Quote
# \n:   New Line (Line Feed)
# \r:   Carriage Return (replaces "Charecter by Character" the operand to the left with that on the right)
# NOTE: \n\r guarantees that the following comes in a new line without any other precedent characters
# \t:   Horizontal Tab
# \xhh: Character with a Hex Value (ASCII Code)
#
# NOTE: to escape the escape sequence characters, use raw string "r" operator before the string
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('ESCAPE CHARACTERS:\n')

# Backspace:
print("Hello  \bWorld!\b ")

# Escape New Line:
print("Hello \
World")

# Escape Backslash:
print("I love Backslash, here it is: \\")

# Escape Single Quote:
print('I\'m Amr')

# Escape Double Quotes:
print("And I love escaping the \"double\" quotes")

# New Line:
print("Hello\nWorld")

# Carriage Return:
print("12345678901234567890\rCarriage Return")

# Horizontal Tab:
print("Hello\tWorld\twith\tTabs")

# Character with a Hex Value:
print("\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x20\x69\x6E\x20\x41\x53\x43\x49\x49")

print("\nPrint raw string using thr \"r\" operator:")
# Backspace:
print(r"Hello  \bWorld!\b ")

# Escape New Line:
print(r"Hello \
World")

# Escape Backslash:
print(r"I love Backslash, here it is: \\")

# Escape Single Quote:
print(r'I\'m Amr')

# Escape Double Quotes:
print(r"And I love escaping the \"double\" quotes")

# New Line:
print(r"Hello\nWorld")

# Carriage Return:
print(r"12345678901234567890\rCarriage Return")

# Horizontal Tab:
print(r"Hello\tWorld\twith\tTabs")

# Character with a Hex Value:
print(r"\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x20\x69\x6E\x20\x41\x53\x43\x49\x49")

# -------------------------------------------------------------------------------------------------------------
# Strings Indexing and Slicing:
# len(var): returns the length of the variable var
# Indexing (Access Single Item):
#   a. use Square brackets '[]' to access an element
#   b. Python uses zero based indexing
#   c. negative indecies count from the right side (counting from the end)
# Slicing (Access Multiple Sequence Items):
#   a. use Square brackets '[Start:End]' or '[Start:End:Steps]'. End is not included
#   b. default Start is interpreted as 0
#   c. default End is interpreted as last character
#   d. default Step is interpreted as 1
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRINGS INDEXING AND SLICING:\n')
print('len function:')
a = 'I want to learn Python'
b = '   I want to learn Python   '
print(len(a))
print(len(b))

# Indexing
print('Indexing:')
myString = 'I love Python'
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[-1])
print('# --------------------------------------------- #')

# Slicing
print('Slicing:')
print(myString[0:1])
print(myString[2:6])
print(myString[7:])
print(myString[::2])
print(myString[:])      # prints the whole string
print(myString[::-1])   # prints the whole string (reversed)
print('# --------------------------------------------- #')

# Mutation
a = '0123456789'
# a[0] = 'x'    # error
print(a)

# Reversing (Advanced)
a = 'abcd'
myList = [a[i:]+a[:i] for i in range(len(a))]
print(myList)

# -------------------------------------------------------------------------------------------------------------
# Strings Methods:
# 01. strip(argument), rstrip(argument), lstrip(argument)
#   returns a stripped string, removes the argeument characters from the right and/or the left side
#   by default they remove the blank space
# 02. center(number of letters, filling character)
#   the opposite of strip, returns a centered string with a filling charaters to the right and the left
#   by default it adds the blank space
# 03. rjust(number of letters, filling character)
#   the opposite of strip, returns a justified string with a filling charaters to the right
#   by default it adds the blank space
# 04. ljust(number of letters, filling character)
#   the opposite of strip, returns a justified string with a filling charaters to the left
#   by default it adds the blank space
# 05. zfill(width of string)
#   fills zeros to the left of the string to make the string with the given width argument
#   if the string in total is shorter than the required width, the original string is returned
#
# 06. count("searched text", start index, end index)
#   returns the number of incidents of the searched text in the whole string
#   by default the start is 0
#   by default the end is the end of the string
# 07. index("sub string", start index, end index)
#   returns the index of of the first incident of sub string in the whole string
#   by default the start is 0
#   by default the end is the end of the string
#   NOTE: returns an error if the sub string is not found
# 08. rindex("sub string", start index, end index)
#   returns the index of of the last incident of sub string in the whole string
#   by default the start is the end of the string
#   by default the end is 0
#   NOTE: returns an error if the sub string is not found
# 09. find("sub string", start index, end index)
#   returns the index of of the first incident of sub string in the whole string
#   by default the start is 0
#   by default the end is the end of the string
#   NOTE: returns -1 if the sub string is not found
# 10. rfind("sub string", start index, end index)
#   returns the index of of the first incident of sub string in the whole string
#   by default the start is end of the string
#   by default the end is the 0
#   NOTE: returns -1 if the sub string is not found
#
# 11. title()
#   returns the string in a title form (words begin with capital and letters after numbers are capital)
# 12. capitalize()
#   returns the string in a capital form (first word begins with capital, the rest is small)
# 13. upper()
#   returns the string in a upper case form (words in capital letters)
# 14. lower()
#   returns the string in a lower case form (words in small letters)
# 15. swapcase()
#   returns a swapped case string
#
# 16. split("seperator", max split), rsplit("seperator", max split)
#   returns a list of strings
#   rsplit starts counting to max split from the right
#   by default the seperator is the blank space
#   by default the max split is infinity
#   NOTE: [*my_string] or list(my_string) splits the string to single characters array
# 17. 'seperator'.join(Iterable)
#   joins the elements of a list or a string into one string
# 18. splitlines()
#   returns a list of strings, each line is a list element
#
# 19. expandtabs(tab size)
#   returns the string with the modified tab size
#
# 20. replace(old value, new value, count)
#   (optional) replaces certain count of incidents
#
# 21. ord('c')
#   returns an ASCII code for a given character 'c'
# 22. chr(i)
#   returns a character for a given integer ASCII code 'i'
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRING METHODS:\n')
print('strip method:')
a = '    I want to learn Python    '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = '####I want to learn Python####'
print(a.strip('#'))
print(a.lstrip('#'))
print(a.rstrip('#'))

a = '$#qI want to learn Python$#q'
print(a.strip('$#q'))
print(a.lstrip('$#q'))
print(a.rstrip('$#q'))
print('# --------------------------------------------- #')

print('center method:')
a = 'Amr'
print(a.center(9))      # spaces
print(a.center(9, '*'))
print(a.center(9, '@'))
# print(a.center(9, '/*/'))     # Error
print('# --------------------------------------------- #')

print('rjust method:')
a = 'Amr'
print(a.rjust(9))      # spaces
print(a.rjust(9, '*'))
print(a.rjust(9, '@'))
print('# --------------------------------------------- #')

print('ljust method:')
a = 'Amr'
print(a.ljust(9))      # spaces
print(a.ljust(9, '*'))
print(a.ljust(9, '@'))
print('# --------------------------------------------- #')

print('zfill method:')
a, b, c = '1', '10', '100'
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
print('# --------------------------------------------- #')

print('count method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.count('Amr'))           # 2
print(a.count('Amr', 1,))       # 1
print(a.count('amr', 4, 14))    # 1 (end is not included)
print(a.count('amr', 4, 15))    # 1
print(a.count('aMr'))           # 1
print('# --------------------------------------------- #')

print('index method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.index('Amr'))           # 0
print(a.index('Amr', 1))        # 16
#print(a.index('Amr', 17))      # Error
print('# --------------------------------------------- #')

print('rindex method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.rindex('Amr'))           # 16
print(a.rindex('Amr', 0, 7))     # 0
#print(a.rindex('Amr', 17))      # Error
print('# --------------------------------------------- #')

print('find method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.find('Amr'))             # 0
print(a.find('Amr', 1))          # 16
print(a.find('Amr', 17))         # -1
print('# --------------------------------------------- #')

print('rfind method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.rfind('Amr'))             # 16
print(a.rfind('Amr', 0, 7))       # 0
print(a.rfind('Amr', 17))         # -1
print('# --------------------------------------------- #')

print('title method:')
a = 'mY Name is aMr, aNd I LOve 3d and 2nc worK'
print(a.title())
print('# --------------------------------------------- #')

print('capitalize method:')
a = 'mY Name is aMr, aNd I LOve 3d and 2nc worK'
print(a.capitalize())
print('# --------------------------------------------- #')

print('upper method:')
a = 'mY Name is aMr, aNd I LOve 3d and 2nc worK'
print(a.upper())
print('# --------------------------------------------- #')

print('lower method:')
a = 'mY Name is aMr, aNd I LOve 3d and 2nc worK'
print(a.lower())
print('# --------------------------------------------- #')

print('swapcase method:')
a = 'mY Name is aMr, aNd I LOve 3d and 2nc worK'
print(a.swapcase())
print('# --------------------------------------------- #')

print('split method:')
a = 'My name is Amr, and I love 3d work'
print(a.split())
print(a.split(" ", 2))
a = 'My-name-is-Amr,-and-I-love-3d-work'
print(a.rsplit("-"))
print(a.rsplit("-", 2))
print('# --------------------------------------------- #')

print('join method:')
a = ['Amr', 'Sara', 'Haitham']
print('-'.join(a))
a = 'Amr'
print('-'.join(a.capitalize()))
print('# --------------------------------------------- #')

print('splitlines method:')
a = 'My name is Amr\n and I love 3d work'
print(a.splitlines())
print('# --------------------------------------------- #')

print('expandtabs method:')
a = 'My\tname\tis\tAmr'
print(a.expandtabs(2))
print(a.expandtabs(20))
print('# --------------------------------------------- #')

print('replace method:')
a = 'My name is Amr. Amr comes from Egypt. Amr is 34 years old.'
print(a.replace('Amr', 'Amoor'))
print(a.replace('Amr', 'Amoor', 1))
print(a.replace('Amr', 'Amoor', 2))
print('# --------------------------------------------- #')

print('ord method:')
a = 'a'
print(ord(a))      # 97
a = 'A'
print(ord(a))      # 65
print('# --------------------------------------------- #')

print('chr method:')
print(chr(97))      # 'a'
print(chr(122))     # 'z'
print('# --------------------------------------------- #')

# -------------------------------------------------------------------------------------------------------------
# Strings Methods with boolean return:
# 1. startswith(string, start index, end index)     checks if string starts with the given string
# 2. endswith(string, start index, end index)       checks it string ends with the given string
# 3. istitle()                                      checks if string is a title
# 4. isspace()                                      checks if string is a space
# 5. islower()                                      checks if string is a lower case string
# 6. isupper()                                      checks if string is an upper case string
# 7. isidentifier()                                 checks if string is a valid identifier
# 8. isalpha()                                      checks if string contains letters from a-z
# 9. isalnum()                                      checks if string contains letters from a-z and numbers 0-9
# 10.isnumeric()                                    checks if string contains numbers 0-9
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRING METHODS WITH BOOLEAN RETURN:\n')

print('startswith method:')
a = 'Amr Gaafer'
print(a.startswith('Amr'))          # True
print(a.startswith('amr'))
print(a.startswith('Gaafer'))
print(a.startswith('Gaafer', 4))    # True
print('# --------------------------------------------- #')

print('endswith method:')
a = 'xyz Test Ali Awad'
print(a.endswith('Awad'))       # True
print(a.endswith('awad'))
print(a.endswith('Ali',0 ,11))  # (end is not included)
print(a.endswith('Ali',0 ,12))  # True
print('# --------------------------------------------- #')

print('istitle method:')
a = 'Amr Wael 3D'
print(a.istitle())          # True
a = 'Amr Wael 3d'
print(a.istitle())
a = 'amr wael'
print(a.istitle())
print('# --------------------------------------------- #')

print('isspace method:')
a = '   '
print(a.isspace())          # True
a = '*'
print(a.isspace())
print('# --------------------------------------------- #')

print('islower method:')
a = 'AMR WAEL'
print(a.islower())
a = 'Amr Wael'
print(a.islower())
a = 'amr wael'
print(a.islower())          # True
print('# --------------------------------------------- #')

print('isupper method:')
a = 'AMR WAEL'
print(a.isupper())          # True
a = 'Amr Wael'
print(a.isupper())
a = 'amr wael'
print(a.isupper())
print('# --------------------------------------------- #')

print('isidentifier method:')
a = 'ää'
print(a.isidentifier())     # True
a = '123a'
print(a.isidentifier())
print('# --------------------------------------------- #')

print('isalpha method:')
a = 'AMRWAEL'
print(a.isalpha())          # True
a = 'Amr Wael'
print(a.isalpha())
print('# --------------------------------------------- #')

print('isalnum method:')
a = 'AMRWAEL'
print(a.isalnum())          # True
a = 'AMRWAEL3D'
print(a.isalnum())          # True
a = 'Amr Wael'
print(a.isalnum())
print('# --------------------------------------------- #')

print('isnumeric method:')
a = '123456'
print(a.isnumeric())        # True
a = '1234.56'
print(a.isnumeric())
a = 'Amr88'
print(a.isnumeric())
print('# --------------------------------------------- #')

# -------------------------------------------------------------------------------------------------------------
# Strings Formating:
# Old Method: Using the place holder %:
#   %s      string place holder
#   %d      digit place holder
#   %f      float place holder
#
#   %.xs    string place holder with a maximum strings number (truncated string)
#   %.xd    digit place holder with a minimum digits number
#   %.xf    float place holder with a certain floating point accuracy
#
#   Syntax: 'string with place holder(s) within' %(parameters corresponding of each holder)
# -------------------------------------------------------------------------------------------------------------
# New Method: Using the place holder {}:
#   {}      general purpose square brackets place holder
#   {:s}    string place holder
#   {:d}    digit place holder
#   {:f}    float place holder
#
#   {:.xs}  string place holder with a maximum strings number (truncated string)
#   {:.xd}  [ERROR] digit place holder with a minimum digits number
#   {:.xf}  float place holder with a certain floating point accuracy
#   {:_d}   digit place holder with seperator (_ or ,) within after every three digits (format money)
#
#   Syntax: 'string with {}(s) within'.format(parameters corresponding of each holder)
#           {variable:format} (eg. {x:,})
#
#   Advantage: It could be used in items rearrangement by giving the index to the place holder {index}
#              The index precedes the column sign {index:formating}
# -------------------------------------------------------------------------------------------------------------
#   In Python 3.6 and later: using the format operator f
#   Syntax: f'string with {variable:formating}'
#   Resource: https://pyformat.info/
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRING OLD FORMATTING:\n')
name = 'Amr'
namelong = 'Amr Gaafer'
age = 34
experience = 5.5
print('My name is %s.' %name)   # in case of one parameter, the paranthesis are not needed
print('My name is %s. I\'m %d years old. I have %f years of experience' %(namelong, age, experience))
print('My name is %.03s. I\'m %.1d years old. I have %.0f years of experience' %(namelong, age, experience))
print('My name is %.20s. I\'m %.4d years old. I have %.1f years of experience' %(namelong, age, experience))
print('# --------------------------------------------- #')

print('STRING NEW FORMATTING:\n')
print('My name is {}.'.format(name))
print('My name is {:s}. I\'m {:d} years old. I have {:f} years of experience'.format(namelong, age, experience))
print('My name is {:.03s}. I\'m {:d} years old. I have {:.0f} years of experience'.format(namelong, age, experience))
print('My name is {:.20s}. I\'m {:d} years old. I have {:.1f} years of experience'.format(namelong, age, experience))

print('# --------------------------------------------- #')

print('money format:')
money = 123456789
print('I\'m rich and I\'ve {} $'.format(money))
print('I\'m rich and I\'ve {:,d} $'.format(money))
#print('I\'m rich and I\'ve {:.d} $'.format(money))
print('I\'m rich and I\'ve {:_d} $'.format(money))
print('# --------------------------------------------- #')

print('items rearrange:')
a, b, c = 'Amr', 'Sara', 'Haitham'
print('The family members are: {}, {} and {}.'.format(a, b, c))
print('The family members are: {2}, {1} and {0}.'.format(a, b, c))

a, b, c =  1, 2, 3
print('The numbers members are: {}, {} and {}.'.format(a, b, c))
print('The numbers members are: {2}, {1} and {0}.'.format(a, b, c))
print('The numbers members are: {2:d}, {1:f} and {0:.2f}.'.format(a, b, c))
print('# --------------------------------------------- #')

print('format using the f operator:')
print('The numbers members are: {a}, {b} and {c}.')
print(f'The numbers members are: {a}, {b} and {c}.')
print(f'The numbers members are: {c:.1f}, {b:d} and {a:.2f}.')
