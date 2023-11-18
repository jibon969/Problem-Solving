#  Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def sum_two_number(x, y):
    if x + y  <= 20:
        sum = 20
        return sum
    else:
        sum = x + y
        return sum

result = sum_two_number(10, 20)
print(result)