# Python Program for cube sum of first n natural numbers

"""
1^3 + 2^3 + 3^3 + 4^3 + …….+ n^3 till the n-th term. 
Input: n = 5
Output: 225
"""


sum = 0
for i in range(6):
    sum += i * i * i
print(sum)
