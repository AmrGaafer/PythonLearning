# --------------------------------------------------------------------------------------------------
# Exercise #20: Collection Of Modules
# Developer:    Amr Gaafer
# Date:         24.12.2022
# --------------------------------------------------------------------------------------------------
'''
Exercise #20 solutions
'''

import os
from PIL import Image
os.system('cls')        # cls command

print("Task#1: zip() application:")
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.extend(data)
FINAL_STRING = ''.join(my_data).capitalize()
print(FINAL_STRING) # Elzero

print("Task#2: zip() application:")
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if isinstance(item1, str):
        my_data.append(item1)
FINAL_STRING = ''.join(my_data).capitalize()
print(FINAL_STRING)

print("Task#3: Pillow module:")
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

original_image = Image.open(__location__ + r'\elzero-pillow.png')
original_image.show()

# sub-image#1
crop_window_1 = (400, 0, 800, 400)
sub_image_1 = original_image.crop(crop_window_1).convert('L')
sub_image_1.show()
sub_image_1.save(__location__ + r'\elzero-pillow-sub1.png')

# sub-image#2
crop_window_2 = (0, 400, 1200, 800)
sub_image_2 = original_image.crop(crop_window_2)
sub_image_2 = sub_image_2.convert('L').transpose(method=Image.Transpose.ROTATE_180)
sub_image_2.show()
sub_image_2.save(__location__ + r'\elzero-pillow-sub2.png')

print("Task#4: Doc String:")
# Write Function With Help To Get The Output
def say_hello_to(name):
    '''parameter(someone) => Person Name
    Function To Say Hello To Anyone'''
    return f'Hello {name}'

print(say_hello_to("Osama")) # "Hello Osama"
help(say_hello_to)

print("Task#5: Pylint:")
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    '''parameter(someone) => Person Name
    Function To Say Hello To Anyone'''
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)
