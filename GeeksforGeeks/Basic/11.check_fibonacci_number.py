# How to check if a given number is Fibonacci number?


a = 0
b = 1

for i in range(10):
        i = a + b
        a = b
        b = i
        print(i)