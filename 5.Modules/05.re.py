# --------------------------------------------------------------------------------------------------
# Regular Expressions: Sequence of characters that define a search pattern (general concept)
#   - used in credit card validation, IP address validation, e-mail validation,.. etc.
#   Resources:
#       Test RegEx: https://pythex.org/
#       Characters cheat sheet: https://www.debuggex.com/cheatsheet/regex/python
#       Regular Expression explanation: https://regex101.com/
#
#   Basics:
#       .	    any character except newline
#       a	    character a
#       ab	    string ab
#       a|b	    a or b (pipeline operator)
#       a*	    0 or more a's
#       \	    escapes a special character
#       |       or
#
#   Quantifiers (given after a RegEx to quantify it):
#       *       0 or more
#       +       1 or more
#       ?       0 or 1
#       {n}     exactly n
#       {n,m}   between n and m
#       {n,}    n or more
#       {,m}    up to m
#
#   Regular Expression Groups:
#       ()      Capturing group,
#               this helps to quantify the whole group not only the last character brfore quatifier
#
#   Character Classes:
#       [016]   0, 1 or 6
#       [0-9]   any character from 0 to 9
#       [^0-9]  any character other than from 0 to 9
#       [abc]   a, b or c
#       [a-m]   any character from a to m
#       [^a-m]  any character other than from a to m
#       [A-M]   any character from A to M
#       [^A-M]  any character other than from A to M
#       \d      one digit
#       \D      one non-digit
#       \s      one whitespace
#       \S      one non-whitespace
#       \w      one word character
#       \W      one non-word character
#
#   Assertions:
#       ^       start of string
#       $       end og string
#
#   Flags:
#       re.I    ignore case
#       re.M    multiline
#       re.DOTALL
#               (.) dot will be matching all characters including new line
#       re.VERBOSE
#               ignore comments in regular expression (rare to use)
#
# Regular Expressions Methods:
#   search(pattern, string, flag)
#       searches a pettern in a given string and returns the firs match only
#       returns None if no matching found
#   findall(pattern, string, flag)
#       searches a pattern in a given string and returns a list of all matching
#       returns an empty list if no matching found
#   split(pattern, string, MaxSplit, flag)
#       returns a list of elements split at each match
#       if no matches found, it returns the whole string in a one element list
#   sub(pattern, replace, string, ReplaceCount, flag):
#       replaces matches with a given replacement string
#       returns the modified string
# --------------------------------------------------------------------------------------------------
''' RE module '''

import os
import re               # Regular Expression module
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Regular Expressions:\n')

# e-mail pattern assertion:
#   ^[A-z0-9\.]+@[A-z]+\.[A-z]{,3}$
#   ^[A-z0-9\.]+@[A-z]+\.(com|net|org|de)$

print('\n# ********************************************* #')
print('RE Methods:\n')
print('search method:')

my_string = re.search(r'[A-Z]', 'Amr Gaafer')
print(type(my_string))
print(my_string.string)     # returns the original string
print(my_string.span())     # returns span of the matching string
print(my_string.group())    # returns the matching string
print(my_string.groups())   # returns the matching string

is_email = re.search(r'[A-z0-9\.]+@[A-z]+\.(com|net|org|de)', 'a@a.com')
if is_email:
    print('this is a valid e-mail')
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())
else:
    print('this is not a valid e-mail')
print('# --------------------------------------------- #')

print('findall method:')
email_input = input('please enter your e-mail: ')
search = re.findall(r'[A-z0-9\.]+@[A-z]+\.com|net|org|de', email_input)
email_list = []
if search:
    email_list.append(search)
    print('e-mail added')
else:
    print('invalid e-mail')
for email in email_list:
    print(email)
print('# --------------------------------------------- #')

print('split method:')
string_one = 'I Love Python'
search1 = re.split(r'\s', string_one, 1)
print(search1)

string_two = 'How-to_Write_a_very-good-article'
search2 = re.split(r'-|_', string_two)
print(search2)
print('# --------------------------------------------- #')

print('sub method:')
string_three = 'I love Python'
search3 = re.sub(' ', '-', string_three, 5)
print(search3)
