# -------------------------------------------------------------------------------------------------------------
# Exercise #13: Function Packing, Recursion, Lambda
# Developer:    Amr Gaafer
# Date          23.08.2022
#
# NOTE: How do you make an argument in function optional?
# You can define Python function optional arguments by 
#   1. specifying the name of an argument followed by a default value when you declare a function. 
#   2. You can also use the **kwargs method to accept a variable number of arguments in a function.
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Function packing and unpacking dictionary:")
def get_score(**SubjectsRatings):
    for subject, rating in SubjectsRatings.items():
        print(f'{subject} => {rating}')

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

print("Task#2: Function packing and unpacking with multitype inputs:")
def get_people_scores(name = '', **SubjectsRatings):
    if name != '' and len(SubjectsRatings) != 0:
        print(f'Hello {name}, this is your score table:')
    elif name != '':
        print(f'Hello {name}, you have no scores to show')
    if len(SubjectsRatings) != 0:
        for subject, rating in SubjectsRatings.items():
            print(f'{subject} => {rating}')

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)
# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)
# Test 3
get_people_scores(Logic=70, Problems=60)
# Test 4
get_people_scores("Ahmed")

print("Task#3: Function input parameters definition:")
def get_the_scores(name = '', **SubjectsRatings):
    if name != '' and len(SubjectsRatings) != 0:
        print(f'Hello {name}, this is your score table:')
    elif name != '':
        print(f'Hello {name}, you have no scores to show')
    if len(SubjectsRatings) != 0:
        for subject, rating in SubjectsRatings.items():
            print(f'{subject} => {rating}')

scores_list = {'Math': 90, 'Science': 80, 'Language': 70}
# Test 1
get_the_scores("Osama", **scores_list)
# Test 2
get_the_scores("Osama")
# Test 3
get_the_scores(**scores_list)
