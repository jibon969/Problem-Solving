# Display Calendar
# https://docs.python.org/3/library/calendar.html

import calendar

year = int(input("Enter year   : "))
month = int(input("Enter month : "))
result = calendar.month(year, month)
print(result)

