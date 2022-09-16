# -------------------------------------------------------------------------------------------------------------
# Project: Your Age Full Details
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# Input age
age = int(input("What is your age? ").strip())
print(age)
print(type(age))

# Get age in all time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You lived for: ")
print(f"{months} Months\n{weeks:,} Weeks\n{days:,} Days\n{hours:,} Hours\n{minutes:,} Minutes\n{seconds:,} Seconds")