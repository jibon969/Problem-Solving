
"""
Maximum Number
"""

a = -2
b = -4

output = max(a, b)
print(output)

# maximum


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


output = maximum(-50, -34)
print(output)


# Use of ternary operator
a = 2
b = 4
print(a if a >= b else b)


# Using lambda function
number = lambda a, b: a if a >= b else b
print(number(3, 8))


# Using list comprehension
a = 2
b = 4
x = [a if a > b else b]
print(x)


# maximum of two numbers
a = 12
b = -4
x =[a, b]
x.sort()
print(x[1])
