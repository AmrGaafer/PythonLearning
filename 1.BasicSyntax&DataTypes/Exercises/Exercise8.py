# -------------------------------------------------------------------------------------------------------------
# Exercise #8:  User Input & Practice
# Developer:    Amr Gaafer
# Date          16.08.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: User string input:")
name = input("What is your name? ").strip().capitalize()
print(f"Hi {name}, happy to see you!")

print("Task#2: User integer input:")
age = int(input("How old are you? ").strip())
if age < 16:
    print("Your age is less than 16, this content isn't suitable for you")
else:
    print(f"Your age is {age}, access is granted")

print("Task#3: User string input with formating:")
first_name = input("What is your first name? ").strip().capitalize()
second_name = input("What is your second name? ").strip().capitalize()
print(f"Hi {first_name} {second_name:.1s}., happy to see you!")

print("Task#4: User string input with slicing:")
email = input("What is your e-mail? ").strip().lower()
print(f"Name:       {email[0 : email.find('@')]}")
print(f"Domain:     {email[email.find('@')+1 : email.find('.', email.find('@')+1 )]}")
print(f"Top Domain: {email[email.find('.', email.find('@')+1 )+1 : ]}")
