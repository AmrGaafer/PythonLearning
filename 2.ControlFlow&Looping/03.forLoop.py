# -------------------------------------------------------------------------------------------------------------
# for item in iterable_object:
#   code to be executed as long as while condition is True
# else:
#   code to be executed once the for loop is done
# item:             user-defined variable, doesn not have to be predefined before the for loop
# iterable_object:  sequences like list, tuples, sets, dictionaries or string of characters
#                   range(start,stop) can be used to loop over a certain range
#   NOTE: if item iterate over a dictionary, it iterates over the keys
#
# special syntax (List Comprehension):
#   Template#1: value for item initerable_object
#   e.g: x for x in range(n)
#       - returns sequence of value calculations for each for-loop iteration
#       - to save the output as a list put the above syntax in []
#       - to save the output as a set put the above syntax in {}
#   Template#2: value for item initerable_object if condition
#   e.g: x for x in range(n) if x > 0
#       - returns sequence of value calculations for each for-loop iteration if the condition is satisfied
#   Template#3: value1 if condition else value2 for item initerable_object
#   e.g: a if x > 0 else b for x in range(n)
#       - returns sequence of value calculations (a or b) for each for-loop iteration based on the shorthand If Else
#
# break:    stop the loop
#   NOTE: it stops the whole loop including the else statement(s)
# continue: stop the current iteration and start the next one if possible
# pass:     skip a required block of code
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# Emample #1: Numbers list
print('Emample #1: Numbers list:')
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10, 10]
for number in myNumbers:
    print(number, end = ' ')    # end argument allows the following print to write on the same line
    if number < 0:
        print('Negative number detected! STOP!')
        break
    elif number % 2 == 0:
        print("Even")
    elif number % 2 == 1:
        print("Odd")
else:
    print('Loop is finished')

# Emample #2: Range Loop:
print('Emample #2: Range Loop:')
myRange = range(1, 10, 2)
for number in myRange:
    print(number)

# Emample #3: Dictionary Loop:
print('Emample #3: Dictionary Loop:')
mySkills = {'C++':50, 'Python':25, 'Plc': 80}
for skill in mySkills:  # it iterate over the key!
    print(f'My progress in the language {skill} is {mySkills.get(skill)}')

# Emample #4: Nested Loop:
print('Emample #4: Nested Loop:')
outerElements = ['A', 'B', 'C']
innerelements = [1, 2, 3]
for outerelement in outerElements:
    for innerelement in innerelements:
        print(outerelement+str(innerelement))

# Emample #5: Dictionary Nested Loop:
print('Emample #5: Dictionary Nested Loop:')
members = {
    "Amr":      {'C++':50,     'Python':25, 'Plc': 80},
    "Hammam":   {'Matlab':100, 'Python':50, 'Plc': 20},
    "Sadek":    {'Matlab':90,  'Python':80, 'Plc': 70},
}
print('Method#1:')
for member in members:
    print(f'{member} has the following skills:')
    for skillKey in members[member]:
        print(f'\t{skillKey} with {str(members[member][skillKey])}%')

print('Method#2:')
for member, skills in members.items():
    print(f'{member} has  has the following skills:')
    for skillKey in skills:
        print(f'\t{skillKey} with {str(skills[skillKey])}%')

# Emample #6: List Comprehension:
print('Emample #6: List Comprehension:')
print([x for x in range(10)])
print({x for x in range(10)})

print([x for x in range(10) if x > 5])
print({x for x in range(10) if x > 5})

print([1 if x > 5 else 0 for x in range(10)])
print({1 if x > 5 else 0 for x in range(10)})
