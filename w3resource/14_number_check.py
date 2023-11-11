# Write a Python program to test whether a number is within 100 of 1000 or 2000.

# number = int(input("Enter your number : "))
# if number == 100:
#     print("100")
# elif number == 1000:
#     print("1000")
# elif number == 2000:
#     print("2000")
# else:
#     print("Not with this number")

def check_number(number):
    # return (number<=100) or (number<=200)
    return ((abs(1000 - number) <= 100) or (abs(2000 - number) <= 100))

result = check_number(200)
print(result)