# -------------------------------------------------------------------------------------------------------------
# Exercise #2:  Strings And Methods
# Developer:    Amr Gaafer
# Date          15.08.2022
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print("Task#1: concatenate:")
name = 'Amr'
age = 34
country = 'Egypt'

print(f"Hello '{name}', how are you doing \\ \"\"\" Your age is \"{age}\"\" and your country is: {country}")

print("Task#2: new line:")
print(f"Hello '{name}', how are you doing \\\n\"\"\" Your age is \"{age}\"\" \nand your country is: {country}")

print("Task#3: indexing:")
name = 'Elzero'
print(f"The second letter is \"{name[1]}\"")
print(f"The third letter is \"{name[2]}\"")
print(f"The last letter is \"{name[-1]}\"")

print("Task#4: slicing:")
print(name[1:4])
print(name[0::2])
print(name[-2::-2])

print("Task#5: strip method:")
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

print("Task#6: zfill method:")
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

print("Task#7: rjust method:")
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

print("Task#8: swapcase method:")
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

print("Task#9: count method:")
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

print("Task#10: index/find method:")
name = "Elzero"
print(name.index("z"))
print(name.find("z"))

print("Task#11/12: replace method:")
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "love", 1))
print(msg.replace("<3", "love"))

print("Task13: string format in Python:")
name = "Osama"
age = 38
country = "Egypt"
print("The old way: My Name Is %s, And My Age Is %d, And My Country Is %s"%(name, age, country))
print("The new way: My Name Is {}, And My Age Is {}, And My Country Is {}".format(name, age, country))
print(f"The newest way: My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
