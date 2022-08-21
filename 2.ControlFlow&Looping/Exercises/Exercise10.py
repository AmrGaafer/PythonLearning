# -------------------------------------------------------------------------------------------------------------
# Exercise #10: Loop While & Training
# Developer:    Amr Gaafer
# Date          21.08.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: Numbers printer:")
num = int(input('Enter an integer larger than 0... ').strip())
if num > 0:
    counter = 0
    while num > 1:
        num = num - 1
        if num != 6:
            print(num)
            counter += 1
        else:
            continue
    else:
        print(f"{counter} number(s) has/have been printed")
else:
    print("This entry doesn't satisfy the input requirements!")

print("Task#2: Strings printer:")
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
counter = 0
while  i< len(friends):
    if friends[i].islower():
        counter += 1
    else:
        print(friends[i])
    i += 1
else:
    print(f"Friends list has been printed, {counter} friend(s) has/have been ignored")

print("Task#3: Strings list printer:")
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(0))

print("Task#4: Strings list editor:")
my_friends = []
i = 4
while i > 0:
    name = input(f"You still have {i} friend(s) to assign. Enter your friend's name: ").strip()
    if name.isupper():
        print("Invalid name entry, try another name!")
        continue
    elif name.islower():
        my_friends.append(name.capitalize())
        print(f"Valid name entry, name \"{name}\" capitalized and added!")
        i -= 1
    elif name.istitle():
        my_friends.append(name)
        print(f"Valid name entry, name \"{name}\" added!")
        i -= 1
    else:
        continue
else:
    print(f"here are my friends:\n{my_friends}")
