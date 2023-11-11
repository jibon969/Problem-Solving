# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date
x = date(2014, 7, 2)
y = date(2014, 7, 11)
result = x - y
print(result)