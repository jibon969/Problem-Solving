# Sum of squares of first n natural numbers

# sum = 0
# for i in range(1, 5+1):
#         sum = sum + (i * i)
# print(sum)

# num = int(input("Enter your number : "))
# sum = num
# for i in range(1, num+1):
#         sum = sum + (i * i)
#         # print(sum, i)

# print("Sum of squares : ", sum)


# Add to function ========================
number = int(input("Enter your number : "))

def sum_of_square(n):
        sum = 0
        for i in range(1, n+1):
                sum = sum + i * i
        return sum

output = sum_of_square(number)
print("Sum of squares : ", output)
