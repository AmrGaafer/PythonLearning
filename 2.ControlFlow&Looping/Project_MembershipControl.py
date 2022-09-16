# -------------------------------------------------------------------------------------------------------------
# Project: Membership Control
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# List of admins
adminsList = ['Amr', 'Adam', 'Yousuf', 'Younus', 'Maria']

# Login
name = input('Please, type your name: ').strip().capitalize()

if name in adminsList:
    print(f'Hello {name}, you are an admin')
    option = input('delete or update your name? ').strip().lower()
    print(f'You have selected: {option}')
    
    if option == 'update' or option == 'u':
        newName = input('Please, type your new name: ').strip().capitalize()
        adminsList[adminsList.index(name)] = newName
        print('Username updated...')
        print(adminsList)
        
    elif option == 'delete' or option == 'del' or option == 'd':
        adminsList.pop(adminsList.index(name))
        print('Username deleted...')
        print(adminsList)
        
    else:
        print('Wrong option!!')
else:
    request = input('You are not an admin, want to be added (yes/no)? ')
    
    if request == 'yes' or request == 'y':
        adminsList.append(name)
        print('Username added...')
        print(adminsList)
        
    elif request == 'no' or request == 'n':
        print('Username not added...')
        
    else:
        print('Wrong option!!')