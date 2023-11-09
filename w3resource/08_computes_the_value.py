# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""
Sample value of n is 5
Expected Result : 615
"""

number = int(input("Enter your number : "))
n1 = int("%s" % number)
n2 = int("%s%s" % (number, number))
n3 = int("%s%s%s" % (number, number, number))
print(n1+n2+n3)


