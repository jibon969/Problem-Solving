
"""
How to add two number
"""

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

result = num1 + num2
print("Sum of {0} and {1} is {2}" .format(num1, num2, result))


# Adding two numbers using by defining add function and return the result
def add_two_number(num1, num2):
    return num1 + num2


output = add_two_number(30, 34)
print('Sum of {0} and {1} is {2}'.format(num1, num2, output))


# Using operator.add() method
import operator
num1 = 10
num2 = 20
output = operator.add(num1, num2)
print('Sum of {0} and {1} is {2}'.format(num1, num2, output))
