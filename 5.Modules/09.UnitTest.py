# --------------------------------------------------------------------------------------------------
# Unit Teesting with Unittest:
#   Test Runner:
#       - The module that runs the unit testing (unittest, pytest)
#   Test case:
#       - smallest unit of testing
#       - it uses Asserts methods to check for actions and responses
#   Test Suite:
#       Collection of multiple Tests or Test Cases
#   Test Report:
#       - full report containing the failure or success
#
#   unittest:
#       Implementation: add tests into Classes as Methods
#                       use a series of special Assertion Methods
#
#   Resource: https://docs.python.org/3/library/unittest.html
# --------------------------------------------------------------------------------------------------

import os
import unittest         # logging module
os.system('cls')        # cls command

print('Assertion without unittest module:')

assert 3*8 == 24, 'should be 24'    # if the assertion fail, it produces AssertionError 

def test_case1():
    assert 3*8 == 24, 'should be 24'

def test_case2():
    assert 5*50 == 250, 'should be 250'

if __name__ == '__main__':
    test_case1()
    test_case2()
    print('all tests without unittest passed')

print('\nAssertion with unittest module:')

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(100 > 97, 'should be True')
    def test2(self):
        self.assertEqual(100, 100, 'should be 100')

if __name__ == '__main__':
    unittest.main()
