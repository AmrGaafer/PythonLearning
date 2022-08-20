# -------------------------------------------------------------------------------------------------------------
# Exercise #9:  Control Flow
# Developer:    Amr Gaafer
# Date          20.08.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: Calculator:")
num1 = int(input('Enter number#1: ').strip())
num2 = int(input('Enter number#2: ').strip())
operation = input('Enter the required operation: ').strip().lower()

if operation == '+' or operation == 'add':
    print(num1 + num2)
elif operation == '-' or operation == 'subtract':
    print(num1 - num2)
elif operation == '*' or operation == 'multiply':
    print(num1 * num2)
elif operation == '**' or operation == 'exponent':
    print(num1 ** num2)
elif operation == '/' or operation == 'divide':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('NA')
elif operation == '%' or operation == 'modulo':
    print(num1 % num2)
elif operation == '//'or operation == 'floor division':
    print(num1 // num2)
    if num2 != 0:
        print(num1 / num2)
    else:
        print('NA')
else:
    print('operation not available')

print("Task#2: Short if (trenary conditional operator):")
age = int(input('Enter your age: ').strip())
print("App is suitable for you") if age > 16 else print("App is not suitable for you")

print("Task#3: Age calculator:")
age = int(input('Enter your age in years: ').strip())
if age > 10 and age < 100:
    print('Your age in months:   '+ f'{age * 12}')
    print('Your age in weeks:    '+ f'{age * 54}')
    print('Your age in days:     '+ f'{age * 365}')
    print('Your age in hours:    '+ f'{age * 365 * 24}')
    print('Your age in minutess: '+ f'{age * 365 *24 * 60}')
    print('Your age in seconds:  '+ f'{age * 365 *24 * 60 * 60}')
else:
    print('Age is out of range')

print("Task#4: Discount calculator:")
countries = ['Egypt', 'Libya', 'Sudan', 'Iraq', 'Palestine', 'Germany', 'Slovakia', 'Italy']
discount = 50
country = input("Enter your country name: ").strip().capitalize()
if country in countries:
    print(f'Your are from {country}! you have a {discount}% discount')
else:
    print(f'Your are from {country}! your country is not eligible for oue discount.... use VPN :)')
