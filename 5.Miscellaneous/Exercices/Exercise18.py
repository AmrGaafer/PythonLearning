# -------------------------------------------------------------------------------------------------------------
# Exercise #18: Date & Time 
# Developer:    Amr Gaafer
# Date:         28.09.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: datatime module:")
import datetime
referenceDate = datetime.date(2021, 6, 25)
currentDate = datetime.date.today()
print(f'Days From {referenceDate} To {currentDate}: {(currentDate-referenceDate).days} days')

print("Task#2: datetime formating:")
print(currentDate.strftime('%Y-%m-%d'))
print(currentDate.strftime('%b %d,%Y'))
print(currentDate.strftime('%d - %b - %Y'))
print(currentDate.strftime('%d / %b / %y'))
print(currentDate.strftime('%d / %B / %Y'))
print(currentDate.strftime('%a, %d %B %Y'))
