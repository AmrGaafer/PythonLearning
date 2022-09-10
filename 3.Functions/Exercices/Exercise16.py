# -------------------------------------------------------------------------------------------------------------
# Exercise #15: Map, Filter, Reduce
# Developer:    Amr Gaafer
# Date          10.09.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: map():")
def remove_chars(s):
    return s[slice(1,len(s)-1)]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Test 1
cleaned_list  = map(remove_chars, friends_map)
for s in cleaned_list:
    print(f'"{s}"')

# Test 2
cleaned_list  = map(lambda s: s[slice(1,len(s)-1)]+": from lambda", friends_map)
for s in cleaned_list:
    print(f'"{s}"')


print("Task#2: filter():")
def get_names(s):
    return s.endswith('m')
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Test 1
names = filter(get_names, friends_filter)
for s in names:
    print(f'"{s}"')

# Test 2
names = filter(lambda s: s.endswith('m'), friends_filter)
for s in names:
    print(f'"{s} : from lambda"')

print("Task#3: reduce():")
from functools import reduce

def my_multiplication(num1, num2):
    return num1 * num2
nums = [2, 4, 6, 2]

# Test 1
print(reduce(my_multiplication, nums))

# Test 2
print(reduce(lambda num1, num2: num1 * num2, nums))

print("Task#4: enumerate():")
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Solution 1
print("Solution 1:")
for count, skill in enumerate(reversed(skills), 50):
    if type(skill) == str:
        print('"', count, " - " ,skill, '"', sep='')

# Solution 2
print("Solution 2:")
for skill in enumerate(reversed(skills), 50):
    if(type(skill[1])) != int:
        print(skill)
