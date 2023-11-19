#  Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.

"""_summary_
The formula for future value with compound interest is FV = P(1 + r/n)^nt.
FV = the future value;
P = the principal;
r = the annual interest rate expressed as a decimal;
n = the number of times interest is paid each year;
t = time in years.
"""

amt = 10000, 
int = 3.5, 
years = 7

result = amt * ((1 + (0.01 * int)) ** years)
print(result)


