# Sum of Cubes of n Natural Numbers
""" 
Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225

Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
"""

number = int(input("Enter your number : "))
def sum_of_cubes(n):
        sum = 0
        for i in range(1, n+1):
                sum = sum + i * i * i 
        return sum
output = sum_of_cubes(number)
print(output)


