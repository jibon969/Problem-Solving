# How to check if a given number is Fibonacci number?

# n = int(input("Enter your number : "))

a = 0
b = 1

for i in range(10):
        i = a + b
        a = b
        b = i
        print(i)

print("\n ========================== ")
    

# Check Fibonacci number
# def isFibonacci(num):
#         fib1 = 0
#         fib2 = 1
#         sum =  fib1 + fib2

#         while (sum <= num):
#                 if num == sum:
#                         return True
#         return False

# output = isFibonacci(10)
# print(output)
        
      