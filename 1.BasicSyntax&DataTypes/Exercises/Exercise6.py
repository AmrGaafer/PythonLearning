# -------------------------------------------------------------------------------------------------------------
# Exercise #6:  Set, Dictionary & Methods
# Developer:    Amr Gaafer
# Date          21.12.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: set creation:")
my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))
unique_list.sort()
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

print("Task#2: sets operation:")
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums ^ letters)
print(nums.symmetric_difference(letters))
print(nums.union(letters))

print("Task#3: sets operation:")
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.update('A', 'B')
print(my_set)
my_set.discard('C')

print("Task#4: sets operation with boolean output:")
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

print("Task#5: dictionary:")
my_Experience = {
    'HTML' : 70,
    'CSS' : 80,
    'Python' : 30
}
for language, progress in my_Experience.items():
    print(f'{language} progress is {progress}%')
my_Experience['AI'] = 20
print(f"AI progress is {my_Experience['AI']}%")
