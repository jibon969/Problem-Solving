# Armstrong Number

"""
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
"""

number = 153
sum = 0
string_number = str(number)
power = len(string_number)

for i in string_number:
    sum = sum + pow(int(i), power)

if number == sum:
    print("yes")
else:
    print("No")