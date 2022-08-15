# -------------------------------------------------------------------------------------------------------------
# Strings:
# 1. could be declared inside single quotes or double quotes
# 2. inside single quotes, the double quotes don't need Escape Character and vice verse
# 3. Concatenation is performed by using '+'
# 4. Triple single quotes or Triple double quotes:
#   a. are used for Multiple-line without '\n'
#   b. skip single and double quotes within
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRINGS:\n')
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
#   by default the ens is the end of the string
# 07. index("sub string", start index, end index)
#   returns the index of of the first incident of sub string in the whole string
#   by default the start is 0
#   by default the ens is the end of the string
#   NOTE: returns an error if the sub string is not found
# 08. find("sub string", start index, end index)
#   returns the index of of the first incident of sub string in the whole string
#   by default the start is 0
#   by default the ens is the end of the string
#   NOTE: returns -1 if the sub string is not found
#
# 09. title()
#   returns the string in a title form (words begin with capital and letters after numbers are capital)
# 10. capitalize()
#   returns the string in a capital form (first word begins with capital, the rest is small)
# 11. upper()
#   returns the string in a upper case form (words in capital letters)
# 12. lower()
#   returns the string in a lower case form (words in small letters)
# 13. swapcase()
#   returns a swapped case string
#
# 14. split("seperator", max split), rsplit("seperator", max split)
#   returns a list of strings
#   rsplit starts counting to max split from the right
#   by default the seperator is the blank space
#   by default the max split is infinity
# 15. 'seperator'.join(Iterable)
#   joins the elements of a list into one string
# 16. splitlines()
#   returns a list of strings, each line is a list element
#
# 17. expandtabs(tab size)
#   returns the string with the modified tab size
#
# 18. replace(old value, new value, count)
#   (optional) replaces certain count of incidents
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
#print(a.index('Amr', 17))       # Error
print('# --------------------------------------------- #')

print('find method:')
a = 'Amr amr AmR amr Amr aMr'
print(a.find('Amr'))           # 0
print(a.find('Amr', 1))        # 16
print(a.find('Amr', 17))       # -1
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

# -------------------------------------------------------------------------------------------------------------
# Strings Formating:
# Old Method: Using the place holder %:
#   %s      string place holder
#   %d      digit place holder
#   %f      float place holder
#   %.xs    truncated string place holder with a certain length
#   %.xf    float place holder with a certainn decimal point accuracy
#   Format: 'string with place holder(s) within' %(parameters corresponding of each holder)
#-------------------------------------------------------------
# New Method: Using the place holder {}:
#   {}      general purpose square brackets place holder
#   {:s}    string place holder
#   {:d}    digit place holder
#   {:f}    float place holder
#   {:_d}   digit place holder with seperator within afer every three digits (format money)
#   {:.xs}  truncated string place holder with a certain length
#   {:.xf}  float place holder with a certainn decimal point accuracy
#   Format: 'string with {}(s) within'.format(parameters corresponding of each holder)
#   Advantage: It could be used in items rearrangement by giving the index to the place holder {index}
#              The index precedes the column sign {index:formating}
#   in Python 3.6 and later:
#           using the format operator f
#           f'string with {variable} within'
# Resource: https://pyformat.info/
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRING OLD FORMATTING:\n')
name = 'Amr'
namelong = 'Amr Gaafer'
age = 34
experience = 5.5
print('My name is %s.' %(name))
print('My name is %s.' %name)   # in case of one parameter, the paranthesis could be removed
print('My name is %s. I\'m %d years old. I have %f years of experience' %(name, age, experience))
print('My name is %s. I\'m %d years old. I have %.2f years of experience' %(namelong, age, experience))
print('My name is %.10s. I\'m %.3d years old. I have %.2f years of experience' %(namelong, age, experience))
print('My name is %.3s. I\'m %d years old. I have %.1f years of experience' %(namelong, age, experience))
print('# --------------------------------------------- #')

print('STRING NEW FORMATTING:\n')
print('My name is {}.'.format(name))
print('My name is {}. I\'m {} years old. I have {} years of experience'.format(name, age, experience))
print('My name is {}. I\'m {} years old. I have {} years of experience'.format(namelong, age, experience))
print('My name is {:.3s}. I\'m {:d} years old. I have {:.1f} years of experience'.format(namelong, age, experience))
print('My name is {:.10s}. I\'m {:d} years old. I have {:.2f} years of experience'.format(namelong, age, experience))

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
print('The family members are: {}, {} and {}.'.format(a, b, c))
print('The family members are: {2}, {1} and {0}.'.format(a, b, c))
print('The family members are: {2:d}, {1:f} and {0:.2f}.'.format(a, b, c))
print('# --------------------------------------------- #')

print('format using the f operator:')
print('The family members are: {a}, {b} and {c}.')
print(f'The family members are: {a}, {b} and {c}.')
print(f'The family members are: {c}, {b} and {a}.')
