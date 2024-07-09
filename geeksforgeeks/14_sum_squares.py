# Python Program for Sum of squares of first n natural numbers
"""
Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
"""

"""
sum = 0
for i in range(6):
    sum = sum + (i*i)
print(sum)
"""

# Added function 
def sum_squares(n):
    sum = 0
    for i in range(n):
        sum += i*i*i
    print(sum)

sum_squares(5)

