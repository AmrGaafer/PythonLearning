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

# example to search if certain string exists in a string:
print(bool(re.search(r"Amr", 'Amr Gaafer')))
print(bool(re.search(r"Amr", 'Lina Gaafer')))

# example to replace
def purify(s: str) -> str:
    print(s)
    if 'i ' in s or 'I ' in s:
        s = re.sub(r'\wi\s|\wI\s','_ ', s)
    print(s)
    if ' i' in s or ' I' in s:
        s = re.sub(r'\si\w|\sI\w',' _', s)
    print(s)
    if 'i' in s or 'I' in s:
        s = re.sub(r'\wi\w|\wI\w','_', s)
    s = re.sub(r'_', '', s).strip()
    return s

#print(purify("STRING"))
#print(purify("1i2 33 i4i5 i555ii5"))
#print(purify("It is a bit chilly"))
#print(purify("Pineapple pizza is delicious"))
#print(purify("It is not there"))

def disemvowel(string_):
    return re.sub(r'[aeiouAEIOU]', '', string_)

print(disemvowel('This website is for losers LOL!'))
