# -------------------------------------------------------------------------------------------------------------
# Strings:
# 1. could be declared inside single quotes or double quotes
# 2. inside single quotes, the double quotes don't need Escape Character and vice verse
# 3. Concatenation is performed by using '+'
# 4. Triple single quotes or Triple double quotes:
#   a. are used for Multiple-line without '\n'
#   b. skip single and double quotes within
# -------------------------------------------------------------------------------------------------------------

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

# Indexing
print('Indexing:')
myString = 'I love Python'
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[-1])

# Slicing
print('Slicing:')
print(myString[0:1])
print(myString[2:6])
print(myString[7:])
print(myString[::2])
print(myString[:])      # prints the whole string
