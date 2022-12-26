# --------------------------------------------------------------------------------------------------
# Exercise #22: Regular Expression 
# Developer:    Amr Gaafer
# Date:         26.12.2022
# --------------------------------------------------------------------------------------------------
'''
Exercise #22 solutions
'''

import re
import os
os.system('cls')        # cls command

print("Task#1: regular expressions basics")
string1 = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
result1 = re.findall(r'(\w\s)', string1)
for count, item in enumerate(result1, 1):
    print(f'Match{count}: {item}')

print("Task#2: regular expressions basics")
string2 = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
result2 = re.search('L(Elzero)', string2)
print(result2)
print(result2.span())
print(result2.group())

print("Task#3: regular expressions with telephone numbers")
string3= '''+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12
'''
result3 = re.findall(r'(\+?\(\d{4}\)\s\d{,4}-\d{4})', string3)
for count, item in enumerate(result3, 1):
    print(f'Match{count}: {item}')

print("Task#4: regular expressions with web links")
string4= '''http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net
'''
result4 = re.findall(r'(https?)://(www.)?\w+.\w{,3}(:\d{,4})?/link.\w+', string4, re.MULTILINE)
for count, item in enumerate(result4, 1):
    print(f'Match{count}: {item}')

print("Task#5: regular expressions challenge")
string5= '''http
https
abcd
abcd
'''
result5 = re.findall(r'https?', string5)
print(result5)
result5 = re.findall(r'http|https', string5)
print(result5)
result5 = re.findall(r'h\w\w\w\w?', string5)
print(result5)
result5 = re.findall(r'\w[e-z]{3,4}', string5)
print(result5)
result5 = re.findall(r'\w[^a-d]{3,4}', string5)
print(result5)
