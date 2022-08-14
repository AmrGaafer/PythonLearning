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
#   a. Use Square brackets '[]' to access an element
#   b. Python uses zero based indexing
#   c. Negative indecies count from the right side (counting from the end)
# Slicing (Access Multiple Sequence Items):
#   a. Use Square brackets '[Start:End]' or '[Start:End:Steps]'. End is not included
#   b. Not given Start is interpreted as 0
#   c. Not given End is interpreted as last character
#   d. Not given Step is interpreted as 1
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
# 1. strip(), rstrip(), lstrip()
#   These methods accept an argument of the strings that could be removed,
#   by default they remove the blank space
#
# 18. replace(old value, new value, count)
#   replaces certain count of incidents (optional) 
# 19. 'seperator'.join(Iterable)
#   joins the elements of a list into one string
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

print('replace method:')
a = 'My name is Amr. Amr comes from Egypt. Amr is 34 years old.'
print(a.replace('Amr', 'Amoor'))
print(a.replace('Amr', 'Amoor', 1))
print(a.replace('Amr', 'Amoor', 2))
print('# --------------------------------------------- #')

print('join method:')
a = ['Amr', 'Wael', 'Ali', 'Awad']
print('-'.join(a))
print('# --------------------------------------------- #')

# -------------------------------------------------------------------------------------------------------------
# Strings Methods with boolean return:
# 1. istitle()          checks if string is a title
# 2. isspace()          checks if string is a space
# 3. islower()          checks if string is a lower case string
# 4. isupper()          checks if string is an upper case string
# 5. isidentifier()     checks if string is a valid identifier
# 6. isalpha()          checks if string contains letters from a-z
# 7. isalnum()          checks if string contains letters from a-z and numbers 0-9
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('STRING METHODS WITH BOOLEAN RETURN:\n')

print('istitle method:')
a = 'Amr Wael Ali Awad 3D'
print(a.istitle())
a = 'Amr Wael Ali Awad 3d'
print(a.istitle())
a = 'amr wael ali awad'
print(a.istitle())
print('# --------------------------------------------- #')

print('istitle method:')
a = '   '
print(a.isspace())
a = '*'
print(a.isspace())
print('# --------------------------------------------- #')

print('islower method:')
a = 'AMR WAEL ALI AWAD'
print(a.islower())
a = 'Amr Wael Ali Awad'
print(a.islower())
a = 'amr wael ali awad'
print(a.islower())          # True
print('# --------------------------------------------- #')

print('isupper method:')
a = 'AMR WAEL ALI AWAD'
print(a.isupper())          # True
a = 'Amr Wael Ali Awad'
print(a.isupper())
a = 'amr wael ali awad'
print(a.isupper())
print('# --------------------------------------------- #')

print('isidentifier method:')
a = 'ää'
print(a.isidentifier())     # True
a = '123a'
print(a.isidentifier())
print('# --------------------------------------------- #')

print('isalpha method:')
a = 'AMRWAELALIAWAD'
print(a.isalpha())          # True
a = 'Amr Wael Ali Awad'
print(a.isalpha())
print('# --------------------------------------------- #')

print('isalnum method:')
a = 'AMRWAELALIAWAD'
print(a.isalnum())          # True
a = 'AMRWAELALIAWAD3D'
print(a.isalnum())          # True
a = 'Amr Wael Ali Awad'
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
namelong = 'Amr Wael Ali Awad'
age = 34
experience = 5.5
print('My name is %s.' %(name))
print('My name is %s.' %name)   # in case of one parameter, the paranthesis could be removed
print('My name is %s. I\'m %d years old. I have %.2f years of experience' %(name, age, experience))
print('My name is %s. I\'m %d years old. I have %.2f years of experience' %(namelong, age, experience))
print('My name is %.8s. I\'m %d years old. I have %.2f years of experience' %(namelong, age, experience))
print('# --------------------------------------------- #')

print('STRING NEW FORMATTING:\n')
print('My name is {}.'.format(name))
print('My name is {}. I\'m {} years old. I have {} years of experience'.format(name, age, experience))
print('My name is {}. I\'m {} years old. I have {} years of experience'.format(namelong, age, experience))
print('My name is {:.8s}. I\'m {:d} years old. I have {:.2f} years of experience'.format(namelong, age, experience))

print('# --------------------------------------------- #')

print('money format:')
money = 123456789
print('I\'m rich and I\'ve {} $'.format(money))
print('I\'m rich and I\'ve {:_d} $'.format(money))
#print('I\'m rich and I\'ve {:.d} $'.format(money))
print('I\'m rich and I\'ve {:,d} $'.format(money))

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
