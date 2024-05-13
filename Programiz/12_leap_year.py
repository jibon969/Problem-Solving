
# Python program to check if year is a leap year or not

year = 2000

if year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap year !")  