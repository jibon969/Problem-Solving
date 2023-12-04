# Sum of squares of first n natural numbers

# sum = 0
# for i in range(1, 6+1):
#         sum = i * i
# print(sum)

num = int(input("Enter your number : "))
sum = 0
for i in range(1, num+1):
        sum = i * i

print("Sum of squares : ", sum)