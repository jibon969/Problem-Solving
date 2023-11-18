#  Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum_number(num1, num2, num3):
    
   if num1 == num2 or num2 == num3 or num1 == num3:
        sum = 0
        return sum
    else:
        sum =  num1 + num2 + num3
        return sum

sum_number(10, 20, 10)