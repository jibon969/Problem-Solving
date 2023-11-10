# Write a Python program that prints the calendar for a given month and year.
import calendar
year = int(input("Enter your year : "))
month = int(input("Enter your month : "))
x = calendar.month(year, month)
print(x)