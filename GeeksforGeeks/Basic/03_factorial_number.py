# Factorial Number

factorial_number = 5
number = 1
for i in range(1, factorial_number+1):
    number = number * i
print(number)


# Using function ===========================
def factorial_number(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    
        return f

result = factorial_number(5)
print(result)