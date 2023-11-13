"""
Python Program for Program to find area of a circle
Formula : pi * r2
where r is radius of circle
"""

PI = 3.142
r = 5

output = PI * (r * r)
print(output)


def area_of_circle(r):
    return PI * (r * r)


circle = int(input("Enter your area of a circle : "))
result = area_of_circle(circle)
print(result)
