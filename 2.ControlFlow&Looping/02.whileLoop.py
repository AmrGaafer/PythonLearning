# -------------------------------------------------------------------------------------------------------------
# while condition_is_True:
#   code to be executed as long as while condition is True
# else:
#   code to be executed once the while condition is False
#
# break:    stop the loop
#   NOTE: it stops the whole loop including the else statement(s)
# continue: stop the current iteration
# pass:     skip a required block of code
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# Emample #1: Friends list
print('Emample #1: Friends list:')
myFriends = ['Abdelmaged', 'Hammam', 'Shoka', 'Sadek', 'Hany', 'Ashraf', 'Othamn', 'Ruby', 'Karem', 'Sherif', 'Hosny']

print(f'List length = {len(myFriends)}')

i = 0
while i < len(myFriends):
    print(f'{str(i+1).zfill(2)}. {myFriends[i]} is my friend!')
    i += 1  # i = i+1
else:
    print('Friends list came to an end!')

# Example #2: Simple bookmark manager
print('Example #2: Simple bookmark manager:')
myFavWeb = []   # to be filled later
maxWebs = 5 

while maxWebs > 0:
    web = input('Input a valid website: ').strip().lower()
    myFavWeb.append(f'https://{web}')
    maxWebs -= 1
else:
    print(f'Bookmark is full, here is your list:\n{myFavWeb}')

if len(myFavWeb) > 0:
    myFavWeb.sort()
    i = 0
    while i < len(myFavWeb):
        print(f'{str(i+1).zfill(2)}. {myFavWeb[i]}')
        i += 1  # i = i+1

# Example #3: Simple password guess
print('Example #2: Simple password guess:')

tries = 5
savedPassword = '12345678'
password = input(f'Please enter your access password, you still have {tries} tries: ')
tries -= 1

while password != savedPassword and tries > 0:
    print('Access denied!')
    password = input(f"Please enter your access password, you still have {str(tries) if tries>1 else 'Last' } tries: ")
    tries -= 1
else:
    if password != savedPassword:
        print('Access denied!... No more trials left!')
    else:
        print('Access granted!')
