# -------------------------------------------------------------------------------------------------------------
# Exercise #11: Loop For & Training
# Developer:    Amr Gaafer
# Date          21.08.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Numbers printer:")
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse = True)

index = 0
for my_num in my_nums:
    index += index
    if my_num % 5 == 0:
        print(f'{index}. {my_num}')
else:
    print('All numbers printed')

print("Task#2: Numbers printer:")
start = 1
end = 20
myRange = range(start, end+1, 1)
for num in myRange:
    if not(num == 6 or num == 8 or num == 12):
        print(str(num).zfill(2))
else:
    print('All numbers printed')

print("Task#3: Dictionary printer:")
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
my_points = 0
for key, value in my_ranks.items():
    if value == 'A':
        print(f'My rank in {key} is A and this equals 100 points')
        my_points += 100
    elif value == 'B':
        print(f'My rank in {key} is B and this equals 80 points')
        my_points += 80
    elif value == 'C':
        print(f'My rank in {key} is C and this equals 40 points')
        my_points += 40
else:
    print(f'My total: {my_points}')

print("Task#4: Dictionary printer in nested loop:")
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
        },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
        },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
        }
}
for student, results in students.items():
    print('"' + 30*'-' + '"')
    print(f'"-- Student Name => {student}"')
    print('"' + 30*'-' + '"')
    points = 0
    for subject, rank in results.items():
        if rank == 'A':
            print(f'"- {subject} => 100 points')
            points += 100
        elif rank == 'B':
            print(f'"- {subject} => 80 points')
            points += 80
        elif rank == 'C':
            print(f'"- {subject} => 40 points')
            points += 40
        elif rank == 'D':
            print(f'"- {subject} => 20 points')
            points += 20
    else:
        print(f'"Total score for {student} is {points}"')
