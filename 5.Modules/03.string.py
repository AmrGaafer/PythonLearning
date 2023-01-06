# --------------------------------------------------------------------------------------------------
# string Module: holds pre-saved strings
# --------------------------------------------------------------------------------------------------

import os
import string           # string module
import random
os.system('cls')        # cls command

print('string module:')

print(dir(string))

print(string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.capwords)          # function capwords
print(string.digits)            # 0123456789
print(string.hexdigits)         # 0123456789abcdefABCDEF
print(string.octdigits)         # 01234567
print(string.printable)         # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)

# serial code generator
nr_letters = int(input('Enter an integer number defining the length of the serial number: '))
print(''.join(random.choice(string.ascii_letters+string.digits) for i in range(0, nr_letters)))
