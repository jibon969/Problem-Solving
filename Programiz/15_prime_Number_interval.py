# Print all Prime Numbers in an Interval


lower = 10
upper = 100

for num in range(lower, upper+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
    