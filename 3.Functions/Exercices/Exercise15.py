# -------------------------------------------------------------------------------------------------------------
# Exercise #15: Built In Functions
# Developer:    Amr Gaafer
# Date          09.09.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: Code tracing (all(), any()):")
values = (0, 1, 2)

if any(values):     # condition statisfied
    my_var = 0
    print(my_var)

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
print(all(my_list[:4]))     # True
print(all(my_list[:6]))     # False
print(all(my_list[:]))      # False
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")   # printed as the first or condition is True
else:
    print("Bad")

print("Task#2: Code tracing (range(), sum()):")
v = 40
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v))  # 820

print("Task#3: Code tracing (range(), sum()):")
n = 1
l = list(range(n))
iterate = True
while iterate:
    if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
        iterate = False
        print("Good")
    else:
        n += 1
        l = list(range(n))
else:
    print(f'The value of \'n\' = {n}')

print("Task#4: Coding Built-In functions (all(), any(), min(), max()):")
def my_all(arguments):
    for element in arguments:
        if (((type(element)==int or type(element)==float) and element == 0) or
        (type(element)==bool and element == False) or
        (type(element)==list and element == []) or
        (type(element)==tuple and element == ()) ):
            return False
    return True

def my_any(arguments):
    for element in arguments:
        if (((type(element)==int or type(element)==float) and element != 0) or
        (type(element)==bool and element == True) or
        (type(element)==list and element != []) or
        (type(element)==tuple and element != ()) ):
            return True
    return False

def my_min(arguments):
    container = arguments[0]
    for i in arguments:
        if container > i: container = i
    return container

def my_max(arguments):
    container = arguments[0]
    for i in arguments:
        if container < i: container = i
    return container

# my_all Test
print('my_all Test:')
print(my_all([1, 2, 3]))            # True
print(my_all([1, 2, 0]))            # False; 0
print(my_all([1.0, 2.0, 3.1]))      # True
print(my_all([1.0, 2.0, 0.0]))      # False; 0.0
print(my_all([1, 2, 3, []]))        # False; []
print(my_all([1, 2, (), 4]))        # False; ()

# my_any Test
print('my_any Test:')
print(my_any([0, 1, [], False]))    # True
print(my_any([0, 0, [1], False]))   # True
print(my_any([0, 0, (-1), False]))  # True
print(my_any([(),[] , 0.0, False])) # False

# my_min Test
print('my_min Test:')
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max Test
print('my_max Test:')
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
