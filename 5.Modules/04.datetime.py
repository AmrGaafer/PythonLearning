# -------------------------------------------------------------------------------------------------------------
# datetime Module: has datetime method than contain date and time methods
#   Formating:
#       Python String-Format-Time (strftime) cheatsheet: https://strftime.org/
#       Syntax:
#           datetimeParameter.strftime('strftime code')
#   strptime(string, format)      String casting to datatime
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

import datetime
print('\n# ********************************************* #')
print('\ndatetime module content:')
print(dir(datetime))
print('\ndatetime.datetime method content:')
print(dir(datetime.datetime))
print('\ndatetime.datetime.now() method content:')
print(dir(datetime.datetime.now()))
print('\ndatetime.datetime.now().date() method content:')
print(dir(datetime.datetime.now().date()))
print('\ndatetime.datetime.now().time() method content:')
print(dir(datetime.datetime.now().time()))

print('\n# ********************************************* #')
print('\nCurrent Date and Time:')
print(datetime.datetime.now().now)
print('Current date:')
print(datetime.datetime.now().date())
print('Current time:')
print(datetime.datetime.now().time())
print('Current year:')
print(datetime.datetime.now().year)
print('Current month:')
print(datetime.datetime.now().month)
print('Current day:')
print(datetime.datetime.now().day)
print('Current weekday:')
print(datetime.datetime.now().weekday())
print('Current hour:')
print(datetime.datetime.now().hour)
print('Current minute:')
print(datetime.datetime.now().minute)
print('Current second:')
print(datetime.datetime.now().second)
print('Minimum/Maximum Date and Time:')
print(datetime.datetime.min)
print(datetime.datetime.max)

print('\n# ********************************************* #')
print('Current hour:')
print(datetime.datetime.now().time().hour)
print('Current minute:')
print(datetime.datetime.now().time().minute)
print('Current second:')
print(datetime.datetime.now().time().second)
print('Current microsecond:')
print(datetime.datetime.now().time().microsecond)
print('Minimum/Maximum Time:')
print(datetime.datetime.now().time().min)
print(datetime.datetime.now().time().max)

print('\n# ********************************************* #')
print('datetime formating:')
myBirthday = datetime.datetime(1988, 3, 11, 7, 30, 20)
print(f'my birthday: {myBirthday}')
print('my birthday formatted version: ' + myBirthday.strftime('%a, %d/%b/%Y'))
myAge = datetime.datetime.now() - myBirthday
print(f'my age: {myAge.days} days')      # .days to get an integer with the number of the days

print('\n# ********************************************* #')
print('string casting to datatime:')
datetime_str = '09/19/18 13:55:26'
datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print(type(datetime_object))
print(datetime_object)  # printed in default format

print('\n# ********************************************* #')
print('margin datatime:')
#margin = int(input('What is the age margin to be considered?... ')) #35 years: 12775
margin = datetime.timedelta(days= myAge.days - 1)
print('Am I older than the margin? Ans:... ', myAge > margin)
