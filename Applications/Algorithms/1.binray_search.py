"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(l, number) -> int:
    l = sorted(l)
    lower_bound, upper_bound = 0, len(l)
    while upper_bound - lower_bound > 1:
        if l[(upper_bound + lower_bound) // 2] > number:
            upper_bound = (upper_bound + lower_bound) // 2
        elif l[(upper_bound + lower_bound) // 2] < number:
            lower_bound = (upper_bound + lower_bound) // 2
        else:
            return (upper_bound + lower_bound) // 2
    return -1

# Test case
if __name__ == '__main__':
    print(binary_search([1 , 2, 4 , 17, 6, 22, 1000, -5], 22))
    print(binary_search([1 , 2, 4 , 17, 6, 22, 1000, -5], -9))
    print(binary_search(list(range(1000)), 50))
    print(binary_search(list(range(1000)), -9))
    print(binary_search([1,3,9,11,15,19,29], 15))
    print(binary_search([1,3,9,11,15,19,29], 25))
