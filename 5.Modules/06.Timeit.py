# --------------------------------------------------------------------------------------------------
# Timing code with timeit: Code performance checker module
#   gets the minimal execution time in milli-seconds of code by running it 1 million time
#   needed functions from this module are: timeit & repeat
#   - repeat is an extended version of the timeit function, it repeat its performance test
#   Syntax:
#       timeit(stmt, setup, timer, number)
#       repeat(stmt, setup, timer, repeat, number)
#           stmt:   statement of code to be tested
#           setup:  needed setup before code execution (module import)
#           timer:  timer value
#           repeat: number of tests to be executed
#           number: execution cycles to be peroformed pro test
#       [default values]
#           timeit(pass, pass, default, 1000000)
#           repeat(pass, pass, default, 5, 1000000)
# --------------------------------------------------------------------------------------------------

import os
import timeit           # timeit module
import time
os.system('cls')        # cls command

print(dir(timeit))

# test print string
print(timeit.timeit('name = "Amr"; name *100'))
# test random number generation
print(timeit.timeit(stmt= 'random.randint(0, 1000)', setup = 'import random'))
# test random number generation with repeat
print(timeit.repeat(stmt= 'random.randint(0, 1000)', setup = 'import random'))

# alternative method for timing measurement using time module
def time_checker(f):
    def wrapper(n):
        start = time.time()
        f(n)
        end = time.time()
        print(f'The function execution time is {end - start} sec')
    return wrapper

@time_checker
def say_hello(n):
    return 'Hello'*n

say_hello(100000000)
