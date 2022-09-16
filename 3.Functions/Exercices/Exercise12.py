# -------------------------------------------------------------------------------------------------------------
# Exercise #12: Function
# Developer:    Amr Gaafer
# Date          22.08.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: Function definition:")
def calculate(num1, num2, op = '+'):
    op = op.strip().lower()
    if op == "+" or op == "add" or op == "a":
        return num1 + num2
    elif op == "-" or op == "subtract" or op == "s":
        return num1 - num2
    elif op == "-" or op == "multiply" or op == "m":
        return num1 * num2
    elif op == "/" or op == "devide" or op == "d":
        return num1 / num2

print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

print("Task#2: Function parameters packing and unpacking (numbers):")
def addition(*variables):
    result = 0
    for variable in variables:
        if variable == 10:
            continue
        elif variable == 5:
            result -= 5
        else:
            result += variable
    else:
        return result

print(addition(10, 20, 30, 10, 15)) # 65
myNumbers = [10, 20, 30, 10, 15, 5, 100]
print(addition(*myNumbers)) # 160

print("Task#3: Function parameters packing and unpacking (strings):")
def show_skills(name, *skills):
    if skills == ():
        print(f'Hello {name.strip().capitalize()}! you have no skills to show')
    else:
        print(f'Hello {name.strip().capitalize()}! you have the following skills:')
        for skill in skills:
            print(f'"- {skill.strip().upper()}"')

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print("Task#4: Function with default parameters values:")
def say_hello(name = 'Unknown', age = 'Unknown', country = 'Unknown'):
    return f'Hello {name.strip().capitalize()}, your age is {age} and you live in {country.strip().capitalize()}'
    
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
