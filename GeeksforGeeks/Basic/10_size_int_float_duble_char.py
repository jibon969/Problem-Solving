# Python Program to Find the Size of int, float, double, and char

"""_summary_
Computers can’t store integers directly. Instead, they only can store binary numbers such as 0 and 1.
To store integers, the computers need to use binary numbers to represent the integers.
For example, to store the number 5, the computers need to represent it using a base-2 number:
5 = 1 x 22 + 0 x 21 + 1 x 20
As you can see, it takes 3 bits to store the number 5 in the memory:
(101)2 = (5)10

Suppose that you have 8 bits, you can store up to 255 integers from zero to 255:
255= 1x 27 + 1 x 26 + 1 x 25 + 1x 24 + 1 x 23 + 1 x 22 + 1x 21 + 1 x 20
By using 8 bits, you can store up to 28 – 1 = 255 integers.

"""
# Getting the size of an integer
# To get the size of an integer, you use the getsizeof() function of the sys module.


from sys import getsizeof
counter = 2**128
size = getsizeof(counter)
print(size)