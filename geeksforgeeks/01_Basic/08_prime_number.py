# check whether a number is Prime or not

# is_prime = int(input("Enter your number : "))

# if is_prime % 2 == 0:
#     print("Not Prime number")
#     break
# else:
#     print("Prime Number ")
	


# Prime Number

"""
step 1 : input 
step 2 : division
step 3 : input / number (between 1 & give number)
"""
# number = 17
# flag = False

# for i, v in enumerate(range(2, number)):
#     if number % v == 0:
#         # print("Not prime !")
#         break
#     else:
#         # print(i, number-2)
#         if i == (number - 3):

#             flag = True
# print(flag)


# number = 1

# for i in range(2, number+1):
#     if number != i:
#         if number % i == 0:
#             print("Not Prime !")
#             break
#     else:
#         print("prime")
#         break



# Prime number in range
my_list = []
for i in range(10, 20+1):
    number = i
    for j in range(2, number):
        if number % j == 0:
            break
    else:
        my_list.append(i)

print(my_list)