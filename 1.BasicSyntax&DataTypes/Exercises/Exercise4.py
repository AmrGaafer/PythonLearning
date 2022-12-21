# -------------------------------------------------------------------------------------------------------------
# Exercise #4:  List & Methods 
# Developer:    Amr Gaafer
# Date          21.12.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: list indexing and slicing:")
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])                   # Method one: indexing
print(friends[::len(friends)-1][0]) # Method two: slicing
print(friends[-1])                  # Method one: indexing
print(friends[::len(friends)-1][1]) # Method two: slicing

print("Task#2: list slicing:")
print(friends[::2])
print(friends[1::2])

print("Task#3: list slicing:")
print(friends[1:-1])
print(friends[-2:])

print("Task#4: list editing:")
friends[-2:] = ['Elzero', 'Elzero']
print(friends)

print("Task#5: list extension:")
friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, 'Nasser')
print(friends)
friends.append('Salem')
print(friends)

print("Task#6: list reducing:")
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)
friends.pop()
print(friends)

print("Task#7: lists concatenate:")
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

print(friends + employees + school)

print("Task#8: lists sorting:")
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse= True)
print(friends)

print("Task#9: lists len:")
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

print("Task#10: sub-lists indexing:")
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
