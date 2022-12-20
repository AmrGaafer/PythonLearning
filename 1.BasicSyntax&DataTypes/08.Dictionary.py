# -------------------------------------------------------------------------------------------------------------
# Dictionary: Mutable unordered sequences of elements
# 1. Dictionary items are enclosed in curly brackets {key:value}
# 2. Dictionary items are unordered
# 3. Dictionary items consist of key:value and seperated by ','
#       - key has to be hashable (immutable type) numbers, strings or tuples
#       - value can be any data type
# 4. Dictionary key must be unique, if the key is repeated, the last one is considered as un updated version
# 5. Dictionary items are mutable (editable) -> edit, delete and add
#
#   NOTE: Mutability: whether an object can change its values after it has been created
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('DICTIONARY:\n')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}

print(user)
print(len(user))        # number of key:value pairs
# get key's value
print(user['country'])
print(user.get('country'))
# get all keys
print(user.keys())
# get all values
print(user.values())

# Two-dimensional (nested) dictionary
languages = {
    'one': {'name': 'python',
            'progress': '70%'},
    'two': {'name': 'PLC',
            'progress': '90%'},
    'three': {'name': 'C++',
            'progress': '75%'},
}

print(languages)
print(len(languages))   # number of key:value pairs
# get key's value
print(languages['one'])
print(languages.get('two'))
print(languages['one']['name'])

# Dictionary creation
framework1 = {  'name': 'python',
                'progress': '70%'}
framework2 = {  'name': 'PLC',
                'progress': '90%'}

framework = {   'one': framework1,
                'two': framework2}
print(framework)

# -------------------------------------------------------------------------------------------------------------
# Dictionary Methods:
# 1.  update({key:value})
#   adds an dictionary element
# 2.  setdefault(key,value)
#   sets the given key with the given value if the key is not found in the dictionary 
#
# 3.  popitem()
#   removes and returns the last dictionary item
# 4.  clear()
#   clears the dictionray
#
# 5.  copy()
#   returns a shallow copy of the dictionray
#
# 6.  keys()
#   returns a list of all the dictionry keys
# 7.  values()
#   returns a list of all the dictionary values
# 8.  items()
#   returns a list of tuple holding all the dictionray items
# 9.  dictionary.get(key)
#   returns the values of the given key
#
# 10.  dict.fromkeys(keys, value)
#   creates a dictionary from given keys and value
# -------------------------------------------------------------------------------------------------------------

print('\n# ********************************************* #')
print('LISTS METHODS:\n')
print('update method:')
user = {
    'name': 'Amr',
}
user['age'] = 34                    # update without update() method
print(user)
user.update({'country': 'Egypt'})   # update with update() method
print(user)
print('# --------------------------------------------- #')

print('setdefault method:')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}
user.setdefault('name' , 'Lina')
user.setdefault('name2' , 'Lina')
user.setdefault('name3')
print(user)
print('# --------------------------------------------- #')

print('popitem method:')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}
print(user.popitem())
print(user)
print('# --------------------------------------------- #')

print('clear method:')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}
user.clear()
print(user)
print('# --------------------------------------------- #')

print('copy method:')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}
user2 = user.copy()
print(user2)
user.update({'skill': 'programming'})
print(user2)
print('# --------------------------------------------- #')

print('keys/values/items methods:')
user = {
    'name': 'Amr',
    'age': 34,
    'country': 'Egypt'
}
print(user.keys())
print(user.values())
print(user.items())
print('# --------------------------------------------- #')

print('fromkeys method:')
keys = ['a', 'b', 'c']
value = 1
myDict = dict.fromkeys(keys, value)
print(myDict)
