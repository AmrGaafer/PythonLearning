# -------------------------------------------------------------------------------------------------------------
# If, Elif, Else:
# if (condition1):
#   statement(s) to be executed
# elif (condition2):
#   statement(s) to be executed
# else:
#   statement(s) to be executed
#
# if (condition1): statement to be executed
# elif (condition2): statement to be executed
# else: statement to be executed
#
# Python supports nested-if-statement
#
# Ternary conditional operator (short if):
# statement if True | if (condition) | else statement if False
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

# Collect age date
age = int(input("What is your age? ").strip())

# Collect time unit
print(" Enter the wished unit in full name or short form ".center(100, "#"))
unit = input("What is the required time unit? ").strip().lower()

# Get age in all time units
if unit == "month" or unit == "months" or unit == "m":
    value = age * 12
    print(f"You lived for: {value} Months")
elif unit == "week" or unit == "weeks" or unit == "w":
    value = age * 12 * 4
    print(f"You lived for: {value} Weeks")
elif unit == "day" or unit == "days" or unit == "d":
    value = age * 365
    print(f"You lived for: {value:,} Days")
elif unit == "hour" or unit == "hours" or unit == "h":
    value = age * 365 * 24
    print(f"You lived for: {value:,} Hours")
elif unit == "minute" or unit == "minutes" or unit == "min":
    value = age * 365 * 24 * 60
    print(f"You lived for: {value:,} Minutes")
elif unit == "secoond" or unit == "seconds" or unit == "s":
    value = age * 365 * 24 * 60 * 60
    print(f"You lived for: {value:,} Seconds")
else:
    print("Invalid entered time unit!")
