# Add Two Numbers

# This program adds two numbers
num1 = 9
num2 = 5

# Add to number
sum =  num1 + num2

# Display the sum
print(sum)
print('{0} + {1} = {2}'.format(num1, num2, sum))


# Add Two Numbers With User Input

number1 = int(input("Enter your first number  : "))
number2 = int(input("Enter your second number : "))

result = number1 + number2
print('{0} + {1} = {2}'.format(number1, number2, result))


# Add Two Numbers With function

def add_two_number(num1, num2):
    return num1 + num2

output = add_two_number(9, 5)
print(output)
