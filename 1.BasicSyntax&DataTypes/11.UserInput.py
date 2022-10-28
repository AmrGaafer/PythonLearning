# -------------------------------------------------------------------------------------------------------------
# User Input:
# input(message)    receives the user input from the terminal and returns it as string
#
# NOTE: Python supports methods chain
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

firstName =     input("what is your first name? ")
secondName =    input("what is your second name? ")
lastName =      input("what is your last name? ")

firstName =     firstName.strip().capitalize()
secondName =    secondName.strip().capitalize()[0]+"."
lastName =      lastName.strip().capitalize()

print(f"Hello {firstName} {secondName} {lastName}!")

# Advanced:
names =         input('Students names: ').split(',')
assignments =   input('Assignment:   ').split(',')
grades =        input('Grade:        ').split(',')

print(names, assignments, grades)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for i in range(len(names)):
    print(message.format(names[i], assignments[i], grades[i], int(grades[i]) + int(assignments[i])*2))