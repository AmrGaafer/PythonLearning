# -------------------------------------------------------------------------------------------------------------
# Exercise #1
# Developer:    Amr Gaafer
# Date          07.08.2022
# -------------------------------------------------------------------------------------------------------------
myName = "Amr"
myAge = "34"
myCountry = "Egypt"

print("Name: "+ myName)
print("Age: "+ myAge)
print("Country: "+ myCountry)

print(type(myName))
print(type(myAge))
print(type(myCountry))

# old format:
print('Hello, my name is %s, I\'m %s years old and I live in %s' %(myName, myAge, myCountry))
# new format:
print('Hello, my name is {:s}, I\'m {:s} years old and I live in {:s}'.format(myName, myAge, myCountry))
# Python 3.6 and later:
print(f'Hello, my name is {myName}, I\'m {myAge} years old and I live in {myCountry}')