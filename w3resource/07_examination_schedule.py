# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# 11 / 12 / 2014

from datetime import datetime
now = datetime.now()

date_time = now.strftime("%m/%d/%Y")
print(date_time)