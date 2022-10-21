# -------------------------------------------------------------------------------------------------------------
# User Input:
# input(message)    receives the user input from the terminal and sends it to the assigned parameter
#
# NOTE: Python supports methods chain
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

firstName = input("what is your first name? ")
secondName = input("what is your first name? ")
lastName = input("what is your first name? ")

firstName = firstName.strip().capitalize()
secondName = secondName.strip().capitalize()[0]+"."
lastName = lastName.strip().capitalize()

print(f"Hello {firstName} {secondName} {lastName}!")
