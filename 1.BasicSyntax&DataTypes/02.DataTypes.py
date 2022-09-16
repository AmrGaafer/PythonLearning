# -----------------------------------------------------------------------------
# type(var): returns the data type of the input variable
#
# Variable Naming Conventions:
# 1. singleword
# 2. camelCase
# 3. snake_case
# 4. PascalCase
# -----------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print(type(10))
print(type(655360))
print(type(-655360))

# Float:
print(type(10.0))
print(type(655360.1))
print(type(-655360.2222))

# String (str):
print(type("Hi!"))

# List:
print(type([1, 2, 3]))

# Tuple:
print(type((1, 2, 3)))

# Set:
print(type({1, 2, 3}))

# Dictionary (dict):
print(type({"Amr": "first", "Sara": "second", "Haitham": "third"}))

# Boolean (bool):
print(type(2 == 2))

# Testing 1
x = 10
x = "Amr is learnign Python"

print(x)

# Reserved Words:
help("keywords")

# Testing 2
a, b, c = 1, 2, 5
