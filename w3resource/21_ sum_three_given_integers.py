#  Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum_number(num1, num2, num3):
    if num1 == num2:
        print("Zero")
    else if num2 == num3:
        print("Zero")
    result = num1 + num2 +num3
    print(result)

sum_number(10, 20, 10)