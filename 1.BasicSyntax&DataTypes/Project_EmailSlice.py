# -------------------------------------------------------------------------------------------------------------
# Project: E-Mail Slice
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

name = input("What is your name? ").strip().capitalize()
email = input("What is your email? ").strip().lower()

user =   email[:email.index('@')]
domain = email[email.index('@')+1 : email.find(".",email.index('@'))]

print(f"Hi {name}, your registered E-Mail is: {email}\nYour username is {user}\nyour domain is {domain}")
