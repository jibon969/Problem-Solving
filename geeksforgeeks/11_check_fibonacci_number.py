def isFibonacci(num):
        fib1 = 0
        fib2 = 1
        sum =  fib1 + fib2

        while (sum <= num):
                if num == sum:
                        return True
        return False

output = isFibonacci(10)
print(output)