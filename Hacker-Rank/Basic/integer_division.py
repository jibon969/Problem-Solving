"""
The provided code stub reads two integers, a  and b, from STDIN.

Add logic to print two lines.
The first line should contain the result of integer division,  a//b . 
The second line should contain the result of float division, a / b .
No rounding or formatting is necessary.
"""

# a = int(input())
# b = int(input())

# integer_division = a // b
# float_division = a / b

# print(integer_division)
# print(float_division)


def integer_float_division(a, b):
    integer_division = a // b
    float_division = a / b

    print(integer_division)
    print(float_division)

integer_float_division(10, 10)
