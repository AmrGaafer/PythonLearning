"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    # 1. Base Case
    if position == 0:
        return 0
    elif position == 1:
        return 1
    # 2. Function calls itself
    else:
        output = get_fib(position-1) + get_fib(position-2)  # 3. alter input parameter
        return output

# Test cases
if __name__ == '__main__':
    print(get_fib(9))
    print(get_fib(11))
    print(get_fib(0))
