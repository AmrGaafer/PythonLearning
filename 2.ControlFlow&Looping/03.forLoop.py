# -------------------------------------------------------------------------------------------------------------
# DEFINITE ITERATION: for loops are ideal when the number of iterations is known or finite
# for iterator in iterable:
#   code to be executed as long as the iterator iterates over the iterable
# else:
#   code to be executed once the for loop is done
# iterator:         user-defined variable, doesn not have to be predefined before the for loop
# iterable:         object that can return one of its elements at a time
#                   - sequence types like strings, list, tuples or sets
#                   - non-sequence types like dictionaries or files
#                   - range(start, stop, step) can be used to loop over a certain range
#   NOTE: if iterator iterates over a dictionary, it iterates over the keys
#
# special syntax (List Comprehension):
#   Template#1: value for iterator in iterable
#   e.g: x for x in range(n)
#       - returns sequence of value calculations for each for-loop iteration
#       - to save the output as a list put the above syntax in []
#       - to save the output as a set put the above syntax in {}
#   Template#2: value for iterator in iterable if condition
#   e.g: x for x in range(n) if x > 0
#       - returns sequence of value calculations for each for-loop iteration if the condition is satisfied
#   Template#3: value1 if condition else value2 for iterator in iterable
#   e.g: a if x > 0 else b for x in range(n)
#       - returns sequence of value calculations (a or b) for each for-loop iteration based on the shorthand If Else
#
# break:    stop the loop, including the else statement(s)
# continue: stop the current iteration and start the next one if possible
# pass:     skip a required block of code
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# Example #1: Numbers list
print('Example #1: Numbers list:')
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

# Example #2: Range Loop:
print('Example #2: Range Loop:')
myRange = range(1, 10, 2)
for number in myRange:
    print(number)

# Example #3: Nested Loop:
print('Example #3: Nested Loop:')
outerElements = ['A', 'B', 'C']
innerelements = [1, 2, 3]
for outerelement in outerElements:
    for innerelement in innerelements:
        print(outerelement+str(innerelement))

# Example #4: Dictionary Loop:
print('Example #4: Dictionary Loop:')
mySkills = {'C++':50, 'Python':25, 'Plc': 80}
for skill in mySkills:                      # iterates over the keys!
    print(f'My progress in the language {skill} is {mySkills.get(skill)}%')
for skill, progress in mySkills.items():    # iterates over the keys and the corresponding values!
    print(f'My progress in the language {skill} is {progress}%')

# Example #5: Dictionary Nested Loop:
print('Example #5: Dictionary Nested Loop:')
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
    print(f'{member} has the following skills:')
    for skillKey in skills:
        print(f'\t{skillKey} with {str(skills[skillKey])}%')

# Example #6: Building a dictionary:
print('Example #6: Building a dictionary:')
print('Method#1:')
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1      # add key to the dictionary and assign initial value (1)
    else:
        word_counter[word] += 1     # increament value of the key by (1)
print(word_counter)

print('Method#2:')
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)

# Example #7: List Comprehension:
print('Example #7: List Comprehension:')
print([x for x in range(10)])
print({x for x in range(10)})

print([x for x in range(10) if x > 5])
print({x for x in range(10) if x > 5})

print([1 if x > 5 else 0 for x in range(10)])
print({1 if x > 5 else 0 for x in range(10)})

# Example #8: For loop break:
print('Example #8: For loop break:')
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num -1:    
            print("{} is a prime number".format(num))
